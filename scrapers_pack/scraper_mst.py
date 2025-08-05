import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime


def mst(my_range):

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    _dates = []
    _titles = []
    _urls = []

    url = 'https://www.manilastandard.net'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')

        section_containers = soup.findAll('.menu')

        st.write(len(section_containers))
    

'''
    

    for i in range(1, 31):
        url = f'https://www.manilastandard.net/page/{i}?s='
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            articles = soup.select('.td-module-meta-info')
            for article in articles:
                _datestr = article.find('time').text
                _date = datetime.strptime(_datestr, '%B %d, %Y, %I:%M %p').date()
                _title = article.find('a').text
                _url = article.find('a').get('href')
                _url = re.sub('www.', '', _url)
                
                if _date >= st_date and _date <= en_date:
                    if _url not in _urls:
                        _dates.append(_datestr)
                        _titles.append(_title)
                        _urls.append(_url)

    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    return df

    '''