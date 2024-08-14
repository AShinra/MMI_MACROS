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

            for articles in article_group:
                article = articles.select('.item-row.item-row-2.flex-row')

                st.write(article)


