import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime, timedelta


userAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36	'
]

def convert_to_date(datestr):

    datestr = datestr.strip()
    _time = int(datestr.split(' ')[0])
    _desc = datestr.split(' ')[1]

    if _desc in ['hour', 'hours']:
        _date = datetime.now() - timedelta(hours=_time)
    elif _desc in ['minute', 'minutes']:
        _date = datetime.now() - timedelta(minutes=_time)
    elif _desc in ['day', 'days']:
        _date = datetime.now() - timedelta(days=_time)

    return _date.date()


def get_sections():

    pub_sections = {}
    url = 'https://www.philstar.com/other-sections'
    response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})
    html_content = response.content
    
    soup = BeautifulSoup(html_content, 'html.parser')
    segments = soup.find_all(class_='segment')
    for segment in segments:
        _urls = segment.find_all('a')
        for _url in _urls:
            _section_name = _url.text
            pub_sections[_section_name] = _url.get('href')

    return pub_sections


def bm():
    
    # convert string to dateobject
    # st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    # en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # get sections
    pub_sections = get_sections()
        
    _dates = []
    _titles = []
    _urls = []
    _section = []
    
    for section_name, url in pub_sections.items():
        # response = requests.get(url)
        st.write(f':red[Scraping - {section_name}]')
        response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')

            # check carousel container
            if soup.find('div', {'class':'carousel__items'}) != None:
                carousel = soup.find('div',{'class':'carousel__items'})
                carousel_items = carousel.find_all('div', {'class':'carousel__item'})

                for carousel_item in carousel_items:

                    _title = ''
                    _date = ''
                    _url = ''

                    # get title
                    _title = carousel_item.find('div', {'class':'carousel__item__title'})
                    _title = _title.find('h2')
                    _title = _title.find('a').text
                    # get date string
                    _datestr = carousel_item.find('div', {'class':'carousel__item__time'}).text
                    # convert dates tring to date
                    try:
                        _date = convert_to_date(_datestr)
                    except:
                        _date = datetime.strptime(_datestr, '%B %d, %Y').date()
                    # get url
                    _url = carousel_item.find('div', {'class':'carousel__item__title'})
                    _url = _url.find('h2')
                    _url = _url.find('a').get('href')

                    st.write(f'{_date} {_title}')
                    st.write(_url)

                    if _url not in _urls:
                        _dates.append(_date)
                        _titles.append(_title)
                        _urls.append(_url)
                        _section.append(section_name)

            # check micro top container
            elif soup.find('div', {'id':'micro_top'}) != None:
                carousel = soup.find('div', {'id':'micro_top'})
                articles = carousel.find_all('div', {'class':'microsite_article'})

                for article in articles:

                    _title = ''
                    _date = ''
                    _url = ''

                    # get title
                    _title = article.find('div', {'class':'microsite_article_title'})
                    _title = _title.find('h2')
                    _title = _title.find('a').text
                    # get url
                    _url = article.find('div', {'class':'microsite_article_title'})
                    _url = _url.find('h2')
                    _url = _url.find('a').get('href')
                    # get date
                    _datestr = _url.split('/')
                    _month = _datestr[-4]
                    _day = _datestr[-3]
                    _year = _datestr[-5]
                    _datestr = f'{_month}-{_day}-{_year}'
                    _date = datetime.strptime(_datestr, '%m-%d-%Y')
                    _date = _date.date()

                    st.write(f'{_date} {_title}')
                    st.write(_url)

                    if _url not in _urls:
                        _dates.append(_date)
                        _titles.append(_title)
                        _urls.append(_url)
                        _section.append(section_name)
            
            # check latest news
            if soup.select('.news_column.latest') != None:
                latest_column = soup.select('.news_column.latest')[1]
                articles = latest_column.select('.tiles.late')

                for article in articles:

                    _title = ''
                    _date = ''
                    _url = ''

                    if article.find('div', {'class':'news_title'}) != None:
                        # get title
                        _title = article.find('div', {'class':'news_title'})
                        # _title = _title.find('h2')
                        _title = _title.find('a').text

                        # get url
                        _url = article.find('div', {'class':'news_title'})
                        # _url = _url.find('h2')
                        _url = _url.find('a').get('href')

                        # get date
                        _datestr = article.find('div', {'class':'dateOfFeature'}).text
                        _datestr = _datestr.split('|')[-1].strip()
                        _date = convert_to_date(_datestr)

                    elif article.find('div', {'class':'titleForFeature'}) != None:
                        # get title
                        _title = article.find('div', {'class':'titleForFeature'})
                        # _title = _title.find('h2')
                        _title = _title.find('a').text

                        # get url
                        _url = article.find('div', {'class':'titleForFeature'})
                        # _url = _url.find('h2')
                        _url = _url.find('a').get('href')

                        # get date
                        _datestr = article.find('div', {'class':'dateOfFeature'}).text
                        _datestr = _datestr.split('|')[-1].strip()
                        _date = convert_to_date(_datestr)

                    st.write(f'{_date} {_title}')
                    st.write(_url)
            
            # check micro top
            if soup.select('div', {'id':'micro_bottom'}) != None:
                # latest_column = soup.select('.news_column.latest')[1]
                # articles = latest_column.select('.tiles.late')
                st.write('Yey')
                    


    df = pd.DataFrame({'Section':_section, 'Date':_dates, 'Title':_titles, 'URL':_urls})
    st.dataframe(df, hide_index=True)
                
            

            #     _url = carousel_item.find(class_='carousel__item__title')
            #     _url = _url.find('a').get('href')
            #     _datestr = carousel_item.find(class_='carousel__item__time').text
            #     _time = int(_datestr.split(' ')[0])
            #     _desc = _datestr.split(' ')[1]

            #     if _desc in ['minutes', 'minutes']:
            #         _date = datetime.now() - timedelta(minutes=_time)
            #     elif _desc in ['hours', 'hour']:
            #         _date = datetime.now() - timedelta(hours=_time)

            #     # if _date >= st_date and _date <= en_date:
            #     if _url not in _urls:
            #         _dates.append(_date)
            #         _titles.append(_title)
            #         _urls.append(_url)

            #         st.write(_date)
            #         st.write(_title)
            #         st.write(_url)
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


    # df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    # st.dataframe(df, hide_index=True)


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