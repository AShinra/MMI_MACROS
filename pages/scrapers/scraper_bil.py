import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime

def bil(my_range):

    urls = [
        'https://bilyonaryo.com/category/business/',
        'https://bilyonaryo.com/category/brand-news/',
        'https://bilyonaryo.com/category/social/',
        'https://bilyonaryo.com/category/video/',
        'https://bilyonaryo.com/category/money/',
        'https://bilyonaryo.com/category/property/',
        'https://bilyonaryo.com/category/technology/',
        'https://bilyonaryo.com/category/travel/',
        'https://bilyonaryo.com/category/health/',
        'https://bilyonaryo.com/category/lifestyle/',
        'https://bilyonaryo.com/category/food-nature/',
        'https://bilyonaryo.com/category/fine-works/',
        'https://bilyonaryo.com/category/golf/'
    ]
    
    # list of user-agents
    userAgents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36	'
    ]

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    _year = my_range[1].split('-')[0]
    _month = my_range[1].split('-')[1]
    _day = my_range[1].split('-')[2]

    _dates = []
    _titles = []
    _urls = []
    
    for i in range(1, 30):
        url = f'https://bilyonaryo.com/{_year}/{_month}/{_day}/page/{i}/'
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            article_group = soup.find(class_='elementor-posts-container')
            articles = article_group.find_all('article')
            for article in articles:
                _title = article.find('h3').text.strip()
                _url = article.find('a').get('href')
                _datestr = article.find(class_='elementor-post-date').text.strip()
                
                if _url not in _urls:
                    _dates.append(_datestr)
                    _titles.append(_title)
                    _urls.append(_url)

        else:
            st.write(response.status_code)
            
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    st.dataframe(df, hide_index=True)
    return df.shape[0]    