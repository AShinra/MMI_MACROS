import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime
from Tools import user_agents
# import cloudscraper


def ps_tech(my_range, timer):

    # scraper = cloudscraper.create_scraper()

    # list of user-agents
    userAgents = user_agents()

    _dates = []
    _titles = []
    _urls = []

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # create list of dates
    D = 'D'
    date_list = pd.date_range(st_date, en_date, freq=D)

    for _date in date_list:
        _Y = _date.year
        _M = _date.month
        _D = _date.day

        with st.spinner('Processing Website'):
            for i in range(1, 2):
                url = f'https://philstartech.com/all-posts/page/{i}/'
                response = requests.get(url, headers={
                    'User-Agent':random.choice(userAgents),
                    'Referer': 'https://www.google.com/',  # Mimic a search engine referral
                    'Accept-Language': 'en-US,en;q=0.9'})
                time.sleep(timer)
                
                # response = scraper.get(url, headers={
                #     'User-Agent':random.choice(userAgents),
                #     'Referer': 'https://www.google.com/',  # Mimic a search engine referral
                #     'Accept-Language': 'en-US,en;q=0.9'})

                "https://philstartech.com/news/2025/08/18/14124/dost-expands-ai-projects-in-ph/"

                            
                if response.status_code == 200:
                    html_content = response.content

                    soup = BeautifulSoup(html_content, 'html.parser')
                    container = soup.select('.loop-grid-base')
                    for _container in container:
                        elements = _container.find_all(class_='grid-base-post')
                        for element in elements:
                            link = element.find('a').get('href')
                            _title = element.find('a').text
                            if link not in [None, '']:
                                if re.search('/\d{4}/\d{2}/\d{2}/\w+', link):
                                    if 'twitter.com/share?' not in link:
                                        if 'facebook.com/share' not in link:
                                            if 'viber://forward?text' not in link:
                                                if link not in _urls:
                                                    _urls.append(link)

                                                    _day = int(link.split('/')[-4])
                                                    _month = int(link.split('/')[-5])
                                                    _year = int(link.split('/')[-6])
                                                    _date = datetime(_year, _month, _day)
                                                    _dates.append(_date)

                                                    _titles.append(_title)

                else:
                    st.write(response)
                    break
                                            
        df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})  

    return df