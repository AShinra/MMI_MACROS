import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random


def bm():

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
    

    for i in range(1, 2):
        url = f'https://businessmirror.com.phpage/{i}/?s='
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            st.write(html_content)
        
        

            # articles = soup.select('.td-module-meta-info')
            # for article in articles:
            #     _date = article.find('time').text
            #     _title = article.find('a').text
            #     _url = article.find('a').get('href')
            #     _url = re.sub('www.', '', _url)
                
            #     if _url in _urls:
            #         continue
            #     else:
            #         _dates.append(_date)
            #         _titles.append(_title)
            #         _urls.append(_url)

    # df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    # st.success(f'Total links collected for this session is {df.shape[0]}')
    # st.dataframe(df, hide_index=True)

    # return df.shape[0]