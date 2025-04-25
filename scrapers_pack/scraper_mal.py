import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from datetime import datetime
from Tools import user_agents


def mal(my_range):

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
        
        url = f'https://malaya.com.ph/page/{i}/?s=&et_pb_searchform_submit=et_search_proccess&et_pb_include_posts=yes&et_pb_include_pages=yes'
        # response = requests.get(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            container = soup.find('div', id="tdi_89")
            # inner_container = container.find('div', id='left-area')
            # articles = inner_container.find_all('article')

            articles = container.find_all('div', class_='td-module-meta-info')

            for article in articles:

                element2 = article.find('div', class_='td-editor-date')
                _datestr = element2.find('time').text
                _date = datetime.strptime(_datestr, '%B %d, %Y').date()

                if _date > en_date:
                    continue
                
                elif _date >= st_date and _date <= en_date:
                    element = article.find('a')
                    _title = element.text
                    _url = element.get('href')

                    _dates.append(_datestr)
                    _titles.append(_title)
                    _urls.append(_url)
            
                elif _date < st_date:
                    status = 'break'
                    break
        
        else:
            st.write(response.status_code)
            break

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df

