import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver import ChromeOptions


def bm():
    
    urls = [
        'https://bilyonaryo.com/2024/08/20/'
    ]

    # urls = [
    #     'https://bilyonaryo.com/category/business/',
    #     'https://bilyonaryo.com/category/brand-news/',
    #     'https://bilyonaryo.com/category/social/',
    #     'https://bilyonaryo.com/category/video/',
    #     'https://bilyonaryo.com/category/money/',
    #     'https://bilyonaryo.com/category/property/',
    #     'https://bilyonaryo.com/category/technology/',
    #     'https://bilyonaryo.com/category/travel/',
    #     'https://bilyonaryo.com/category/health/',
    #     'https://bilyonaryo.com/category/lifestyle/',
    #     'https://bilyonaryo.com/category/food-nature/',
    #     'https://bilyonaryo.com/category/fine-works/',
    #     'https://bilyonaryo.com/category/golf/',
    #     'https://bilyonaryo.com/category/power/',
    #     'https://bilyonaryo.com/category/infrastructure/',
    #     'https://bilyonaryo.com/category/philanthropy/',
    #     'https://bilyonaryo.com/tag/burst-your-babble/',
    #     'https://bilyonaryo.com/category/nature/',
    #     'https://bilyonaryo.com/category/mobility/',
    #     'https://bilyonaryo.com/category/lifestyle/the-vines-that-bind/'
    # ]
    
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
    # st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    # en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    _dates = []
    _titles = []
    _urls = []
    
    for i in range(1, 31):
        url = f'https://bilyonaryo.com/2024/08/20/page/{i}/'

        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            article_group = soup.find(class_='elementor-posts-container')
            articles = article_group.find_all('article', class_='elementor-post')
            for article in articles:
                _title = article.find('h3').text
                _url = article.find('a').get('href')
                _datestr = article.find(class_='elementor-post-date').text.strip()
                _date = datetime.strptime(_datestr, '%B %d, %Y').date()


                st.write(_datestr)
                st.write(_date)
                st.write(_title)
                st.write(_url)
        elif response.status_code == 404:
            continue
        else:
            st.write(response.status_code)
            


    #         article_archive = soup.find(class_='archive-main')
    #         post_grids = article_archive.find_all(class_='post-grid')
    #         for post_grid in post_grids:
    #             _title = post_grid.find(class_='entry-title').text
    #             _url = post_grid.find(class_='entry-title').find('a').get('href')
    #             _datestr = post_grid.find(class_='meta-date').text
    #             _date = datetime.strptime(_datestr, '%B %d, %Y').date()

    #             if _date >= st_date and _date <= en_date:
    #                 if _url not in _urls:
    #                     _dates.append(_datestr)
    #                     _titles.append(_title)
    #                     _urls.append(_url)

    # df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    # st.dataframe(df, hide_index=True)

    # return df.shape[0]


bm()