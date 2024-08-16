import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime


def ps(my_range):

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

    urls = [
        'https://www.philstar.com/rss/headlines',
        'https://www.philstar.com/rss/opinion',
        'https://www.philstar.com/rss/nation',
        'https://www.philstar.com/rss/world',
        'https://www.philstar.com/rss/business',
        'https://www.philstar.com/rss/sports',
        'https://www.philstar.com/rss/entertainment',
        'https://www.philstar.com/rss/lifestyle'
        ]
    

    for url in urls:
        # url = f'https://www.philstar.com/rss/headlines'
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')
            items = soup.find_all('item')
            for item in items:
                _datestr = item.find('pubdate').text
                _datestr = _datestr.split('+')[0]
                _datestr = _datestr.split(',')[1].strip()
                st.write(_datestr)
                _dateday = _datestr.split(' ')
                st.write(_dateday)
                _date = datetime.strptime(_datestr, '%d %b %Y').date()

                _title = item.find('title').text
                _url = item.find('guid').text

                if _date >= st_date and _date <= en_date:
                    if _url not in _urls:
                        _dates.append(_date)
                        _titles.append(_title)
                        _urls.append(_url)

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    st.dataframe(df, hide_index=True)

    return df.shape[0]


# 16 Aug 2024 10:23:00