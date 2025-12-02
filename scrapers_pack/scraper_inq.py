import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime, timedelta
from Tools import user_agents


def inq(my_range):

    # list of user-agents
    userAgents = user_agents()

    now_0 = datetime.today()
    now_0_str = now_0.strftime('%Y-%m-%d')

    now_1 = now_0 - timedelta(days=1)
    now_1_str = now_1.strftime('%Y-%m-%d')

    now_2 = now_0 - timedelta(days=2)
    now_2_str = now_2.strftime('%Y-%m-%d')

    now_3 = now_0 - timedelta(days=3)
    now_3_str = now_3.strftime('%Y-%m-%d')

    now_4 = now_0 - timedelta(days=4)
    now_4_str = now_4.strftime('%Y-%m-%d')

    urls = {
        now_0:f'https://www.inquirer.net/article-index/?d={now_0_str}',
        now_1:f'https://www.inquirer.net/article-index/?d={now_1_str}',
        now_2:f'https://www.inquirer.net/article-index/?d={now_2_str}',
        now_3:f'https://www.inquirer.net/article-index/?d={now_3_str}',
        now_4:f'https://www.inquirer.net/article-index/?d={now_4_str}'
    }

    _dates = []
    _titles = []
    _urls = []

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()
    
    with st.spinner('Processing Website'):
        for k, v in urls.items():
            response = requests.get(v, headers={'User-Agent':random.choice(userAgents)})
            
            if response.status_code == 200:
                html_content = response.content
            
                soup = BeautifulSoup(html_content, 'html.parser')

                article_group = soup.find(id='index-wrap')
                articles = article_group.find_all('li')
                for article in articles:
                    _date = k.date()
                    if _date >= st_date and _date <= en_date:
                        date_str = _date.strftime('%B %d, %Y')
                        _title = article.find('a').text
                        _url = article.find('a').get('href')

                        if _url in _urls:
                            continue
                        else:
                            _dates.append(date_str)
                            _titles.append(_title)
                            _urls.append(_url)
            else:
                st.write(response.status_code)
            
            

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df