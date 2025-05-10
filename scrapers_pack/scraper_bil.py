import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime
from Tools import convert_to_date, user_agents

def bil(my_range):

    # list of user-agents
    userAgents = user_agents()

    _dates = []
    _titles = []
    _urls = []

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # create list of dates
    D = 'D'
    date_list = pd.date_range(st_date, en_date, freq=D)

    for _date in date_list:
        _Y = _date.year
        _M = _date.month
        _D = _date.day

    # _year = my_range[1].split('-')[0]
    # _month = my_range[1].split('-')[1]
    # _day = my_range[1].split('-')[2]
    
        for i in range(1, 30):
            with st.spinner('Processing Website', show_time=True):
                url = f'https://bilyonaryo.com/{_Y}/{_M}/{_D}/page/{i}/'
                # url = f'https://bilyonaryo.com/{_year}/{_month}/{_day}/page/{i}/'
                response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})
                time.sleep(30)

                if response.status_code == 200:
                    html_content = response.content

                    soup = BeautifulSoup(html_content, 'html.parser')

                    article_group = soup.find(class_='elementor-posts-container')
                    articles = article_group.find_all('article')
                    for article in articles:
                        _title = article.find('h3').text.strip()
                        _url = article.find('a').get('href')
                        _datestr = article.find(class_='elementor-post-date').text.strip()
                        _date = convert_to_date(_datestr)
                        
                        # if _url not in _urls:
                        _dates.append(_date)
                        _titles.append(_title)
                        _urls.append(_url)
                elif response.status_code == 404:
                    break
                else:
                    st.write(response.status_code)
            
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    df = df.drop_duplicates(subset=['URL'])

    return df