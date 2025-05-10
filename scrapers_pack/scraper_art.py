import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime
from Tools import user_agents


def art(my_range):

    # list of user-agents
    userAgents = user_agents()

    _dates = []
    _titles = []
    _urls = []

    # initial url
    url = 'https://artplus.squarespace.com/features'

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # create list of dates
    D = 'D'
    date_list = pd.date_range(st_date, en_date, freq=D)

    status = ''
    for _date in date_list:
        _Y = _date.year
        _M = _date.month
        _D = _date.day

    with st.spinner('Processing Website'):
        for i in range(1,100000):

            if status == 'break':
                break
            
            response = requests.get(url)
            response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

            if response.status_code ==200:
                html_content = response.content
                soup = BeautifulSoup(html_content, 'html.parser')

                # get the next page url
                url = soup.find('div', class_='older').find('a').get('href')
                url = f'https://artplus.squarespace.com{url}'

                container = soup.find('div', class_='blog-basic-grid')

                articles = container.find_all('div', class_='blog-basic-grid--text')
                for article in articles:
                    _datestr = article.find('time').text
                    _date = datetime.strptime(_datestr, '%m/%d/%y').date()
                    # st.write(_date)

                    if _date > en_date:
                        continue
                    
                    elif _date >= st_date and _date <= en_date:
                        element = article.find('h1', class_='blog-title')
                        _title = element.find('a').text
                        _url = element.find('a').get('href')
                        _url = f'https://artplus.squarespace.com{_url}'

                        _dates.append(_date)
                        _titles.append(_title)
                        _urls.append(_url)
                
                    elif _date < st_date:
                        status = 'break'
                        break
                
            else:
                st.write(response.status_code)

        
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    # df = df.drop_duplicates(subset=['URL'])
    
    return df

