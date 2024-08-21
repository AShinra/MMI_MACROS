import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime, timedelta


def bm():
    
    urls = [
        'https://www.philstar.com/the-philippine-star/headlines',
        'https://www.philstar.com/the-philippine-star/opinion',
        'https://www.philstar.com/the-philippine-star/business',
        'https://www.philstar.com/the-philippine-star/nation',
        'https://www.philstar.com/the-philippine-star/news-commentary',
        'https://www.philstar.com/the-philippine-star/sports',
        'https://www.philstar.com/the-philippine-star/entertainment',
        'https://www.philstar.com/campus',
        'https://www.philstar.com/movies',
        'https://www.philstar.com/music',
        'https://www.philstar.com/lifestyle/arts-and-culture',
        'https://www.philstar.com/lifestyle/business-life',
        'https://www.philstar.com/lifestyle/health-and-family',        
    ] 
    
    # list of user-agents
    userAgents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36	'
    ]

    # convert string to dateobject
    # st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    # en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # get sections
    urls = []
    url = 'https://www.philstar.com/other-sections'
    response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})
    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    segments = soup.find_all(class_='segment')
    for segment in segments:
        _urls = segment.find_all('a')
        for _url in _urls:
            urls.append(_url.get('href'))
    
    _dates = []
    _titles = []
    _urls = []
    
    for url in urls:
        # response = requests.get(url)
        st.write(url)
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content

            soup = BeautifulSoup(html_content, 'html.parser')

            # check carousel container
            carousel = soup.find(class_='carousel__items')
            st.write(carousel)
            carousel_items = carousel.find_all('div', attrs={
                'class':'carousel__item',
                'id':'parent_top-article-list'})
            for carousel_item in carousel_items:
                _title = carousel_item.find(class_='carousel__item__title').text
                st.write(_title)

                _url = carousel_item.find(class_='carousel__item__title')
                _url = _url.find('a').get('href')
                _datestr = carousel_item.find(class_='carousel__item__time').text
                _time = int(_datestr.split(' ')[0])
                _desc = _datestr.split(' ')[1]

                if _desc in ['minutes', 'minutes']:
                    _date = datetime.now() - timedelta(minutes=_time)
                elif _desc in ['hours', 'hour']:
                    _date = datetime.now() - timedelta(hours=_time)

                # if _date >= st_date and _date <= en_date:
                if _url not in _urls:
                    _dates.append(_date)
                    _titles.append(_title)
                    _urls.append(_url)
            
            # check latest articles container
            # st.write('scraping latest items')
            # news_columns = soup.select('.news_column.latest')
            # for news_column in news_columns:
            #     tiles = news_column.find_all(class_='tiles')
            # for tile in tiles:
            #     _title = tile.find(class_='TilesText').text
            #     st.write(_title)

            #     _url = tile.find(class_='TilesText')
            #     _url = _url.find('a').get('href')
            #     st.write(_url)

            #     _datestr = tile.find(class_='dateOfFeature').text
            #     _datestr = _datestr.split('|')[-1].strip()

            #     _time = int(_datestr.split(' ')[0])
            #     _desc = _datestr.split(' ')[1]

            #     if _desc in ['minutes', 'minutes']:
            #         _date = datetime.now() - timedelta(minutes=_time)
            #     elif _desc in ['hours', 'hour']:
            #         _date = datetime.now() - timedelta(hours=_time)

            #     if _url not in _urls:
            #         _dates.append(_date)
            #         _titles.append(_title)
            #         _urls.append(_url)
            
            # # check trending articles container
            # st.write('scraping trending items')
            # news_columns = soup.select('.news_column.trending')
            # for news_column in news_columns:
            #     tiles = news_column.find_all(class_='tiles')
            # for tile in tiles:
            #     _title = tile.find(class_='TilesText').text
            #     st.write(_title)
                
            #     _url = tile.find(class_='TilesText')
            #     _url = _url.find('a').get('href')
                
            #     _datestr = tile.find(class_='dateOfFeature').text
            #     _datestr = _datestr.split('|')[-1].strip()

            #     _time = int(_datestr.split(' ')[0])
            #     _desc = _datestr.split(' ')[1]

            #     if _desc in ['minutes', 'minutes']:
            #         _date = datetime.now() - timedelta(minutes=_time)
            #     elif _desc in ['hours', 'hour']:
            #         _date = datetime.now() - timedelta(hours=_time)

            #     if _url not in _urls:
            #         _dates.append(_date)
            #         _titles.append(_title)
            #         _urls.append(_url)


    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    st.dataframe(df, hide_index=True)


        #     article_group = soup.find(class_='elementor-posts-container')
        #     articles = article_group.find_all('article', class_='elementor-post')
        #     for article in articles:
        #         _title = article.find('h3').text
        #         _url = article.find('a').get('href')
        #         _datestr = article.find(class_='elementor-post-date').text.strip()
        #         _date = datetime.strptime(_datestr, '%B %d, %Y').date()


        #         st.write(_datestr)
        #         st.write(_date)
        #         st.write(_title)
        #         st.write(_url)
        # elif response.status_code == 404:
        #     continue
        # else:
        #     st.write(response.status_code)
            


    #         article_archive = soup.find(class_='archive-main')
    #         post_grids = article_archive.find_all(class_='post-grid')
    #         for post_grid in post_grids:
    #             _title = post_grid.find(class_='entry-title').text
    #             _url = post_grid.find(class_='entry-title').find('a').get('href')
    #             _datestr = post_grid.find(class_='meta-date').text
    #             _date = datetime.strptime(_datestr, '%B %d, %Y').date()

    #             if _date >= st_date and _date <= en_date:
    #                 if _url not in _urls:
    #                     _dates.append(_datestr)
    #                     _titles.append(_title)
    #                     _urls.append(_url)

    # df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})

    # st.dataframe(df, hide_index=True)

    # return df.shape[0]


bm()