import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime
from Tools import user_agents


def ttm(my_range):

    # list of user-agents
    userAgents = user_agents()

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    _dates = []
    _titles = []
    _urls = []
    
    status = ''
    for i in range(1, 100000):
        
        if status == 'break':
            break

        url = f'https://techtravelmonitor.com/2024/page/{i}/'
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            container = soup.find('div', class_="blog-archieve-layout")

            articles = container.find_all('article')
            for article in articles:
                _datestr = article.find('time').text
                _date = datetime.strptime(_datestr, '%Y-%m-%d').date()

                if _date > en_date:
                    continue
                elif _date >= st_date and _date <= en_date:
                    element = article.find('h2', class_='entry-title')
                    _title = element.text
                    _url = element.find('a').get('href')

                    _dates.append(_date)
                    _titles.append(_title)
                    _urls.append(_url)
                    
                elif _date < st_date:
                    status = 'break'
                    break            

        else:
            st.write(response.status_code)

        
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df

