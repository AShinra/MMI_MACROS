import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time


def bm():

    _dates = []
    _titles = []
    _urls = []
    

    for i in range(1, 2):
        time.sleep(20)
        url = f'https://businessmirror.com.ph/page/{i}/?s='
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            st.write(html_content)
        
        else:
            st.write(response.content)

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