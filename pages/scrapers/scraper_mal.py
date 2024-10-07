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
    
    status = ''
    for i in range(1, 100000):
        url = f'https://malaya.com.ph/page/{i}/?s=&et_pb_searchform_submit=et_search_proccess&et_pb_include_posts=yes&et_pb_include_pages=yes'
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            container = soup.find('div', id="content-area")
            inner_container = container.find('div', id='left-area')
            articles = inner_container.find_all('article')

            for article in articles:
                
                element = article.find_all('a')[1]
                _datestr = article.find_all('span')[-1].text
                _date = datetime.strptime(_datestr, '%b %d, %Y').date()
                _title = element.text
                _url = element.get('href')
        
                if _title not in ['', None]:
                    if _url not in _urls:
                        if _date < st_date:
                            status = 'break'
                            break
                        elif _date > en_date:
                            continue
                        elif _date >= st_date and _date <= en_date:
                            _dates.append(_datestr)
                            _titles.append(_title)
                            _urls.append(_url)
        else:
            st.write(response.status_code)
        
        if status == 'break':
            break

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df

