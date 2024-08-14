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
            st.write(articles)
            
            for article in articles:
                st.write(_title = article.find('a').text)
                st.write(_url = article.find('a').get('href'))

                


