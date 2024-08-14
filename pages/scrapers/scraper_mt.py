import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def mt():

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

                st.write(type(_date))
                st.write(_title)
                st.write(_url)





