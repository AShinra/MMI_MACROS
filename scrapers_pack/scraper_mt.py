import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime

def mt(my_range):

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    _dates = []
    _titles = []
    _urls = []

    for i in range(1, 101):
        url = f'https://www.manilatimes.net/search?query=&pgno={i}'
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
                if 'tmt-newswire' not in _url:
                    _date = article.find(class_='roboto-a').text
                    _date = re.sub('-\n', '', _date)
                    _date = re.sub('\n', '', _date)
                    _date = _date.strip()
                    _date = datetime.strptime(_date, '%B %d, %Y').date()

                    if _date >= st_date and _date <= en_date:
                        if _url not in _urls:
                            _dates.append(_date)
                            _titles.append(_title)
                            _urls.append(_url)
        
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    return df



