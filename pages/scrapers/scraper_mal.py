import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime


def mal(my_range):

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

    _dates = []
    _titles = []
    _urls = []
    
    for i in range(1, 51):
        url = f'https://archive.malaya.com.ph/page/{i}/?s'
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')
            
            articles = soup.find_all(class_='tdb_module_loop')
            for article in articles:
                _title = article.find(class_='entry-title').text
                _url = article.find('a').get('href')
                _datestr = article.find('time').text
                _date = datetime.strptime(_datestr, '%B %d, %Y').date()

                if _title not in ['', None]:
                    if _date >= st_date and _date <= en_date:
                        if _url not in _urls:
                            _dates.append(_datestr)
                            _titles.append(_title)
                            _urls.append(_url)
        else:
            st.write(response.status_code)

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df