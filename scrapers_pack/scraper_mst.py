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
    section_links = []

    url = 'https://www.manilastandard.net'
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        
        footer_container = soup.find(class_='td-footer-wrap')
        
        _links = footer_container.find_all('a')
        for _link in _links:
            x = _link.get('href')
            if 'category' in x:
                if 'https' not in x:
                    section_links.append(f'https://manilastandard.net{x}')
                # else:
                #     section_links.append(x)

        st.write(section_links)

        for section_link in section_links:
            with st.spinner(f'Processing {section_link}'):
                for i in range(1, 11):
                    response = requests.get(f'{section_link}/page/{i}')

                    if response.status_code == 200:
                        html_content = response.content

                        soup = BeautifulSoup(html_content, 'html.parser')

                        articles = soup.find_all(class_='td-module-meta-info')
                        for article in articles:
                            _datestr = article.find('time').text
                            _date = datetime.strptime(_datestr, '%B %d, %Y, %I:%M %p').date()
                            _title = article.find(class_='entry-title').text
                            _url = _title.find('a').get('href')
                            _url = re.sub('www.', '', _url)
                            
                            if _date >= st_date and _date <= en_date:
                                if _url not in _urls:
                                    _dates.append(_datestr)
                                    _titles.append(_title)
                                    _urls.append(_url)
                                    st.write(_urls)

        return pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    

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