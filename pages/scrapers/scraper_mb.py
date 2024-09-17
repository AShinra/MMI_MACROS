import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime


def mb(my_range):

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

        for i in range(1, 11):
            url = f'https://www.bworldonline.com//{_Y}/{_M}/{_D}/page/{i}'
            response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

            st.write(response.status_code)
            if response.status_code == 200:
                html_content = response.content

                soup = BeautifulSoup(html_content, 'html.parser')
                main_container = soup.find(class_='td-ss-main-content')
                containers = main_container.find_all(class_='td-block-row')
                for elements in containers:
                    for element in elements.find_all(class_='td-block-span6'):
                        link = element.find_all('a')[1].get('href')
                        _urls.append(link)
                        _titles.append(element.find_all('a')[1].text)
                
                        _day = int(link.split('/')[-4])
                        _month = int(link.split('/')[-5])
                        _year = int(link.split('/')[-6])
                        _date = datetime(_year, _month, _day)
                        _dates.append(_date)
            else:
                break
   

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    st.dataframe(df, hide_index=True)

    return df.shape[0]