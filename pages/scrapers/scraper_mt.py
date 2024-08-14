import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def mt():

    _dates = []
    _titles = []
    _urls = []

    url = f'https://www.manilatimes.net/search?query='
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        article_group = soup.select('.item-row-2.flex-row.flex-between')

        for article_list in article_group:
            articles = article_list.select('.item-row.item-row-2.flex-row')
        
        for article in articles:
            _title = article.find(class_='article-title-h4').find('a').text
            _url = article.find(class_='article-title-h4').find('a').get('href')
            _date = article.find(class_='roboto-a').text
            _date = re.sub('-\n', '', _date)

            st.write(_date)
            st.write(_title)
            st.write(_url)

            _dates.append(_date)
            _titles.append(_title)
            _urls.append(_url)

    
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    st.dataframe(df, hide_index=True)



