import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime
from Tools import user_agents, parse_date
# import cloudscraper


def yugatech(my_range, timer):

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

    status = ''

    for _date in date_list:
        _Y = _date.year
        _M = _date.month
        _D = _date.day

        with st.spinner('Processing Website'):
            for i in range(1, 3):
                if status=='break':
                    break
                else:
                    url = f'https://www.yugatech.com/page/{i}/'
                    response = requests.get(url, headers={
                        'User-Agent':random.choice(userAgents),
                        'Referer': 'https://www.google.com/',  # Mimic a search engine referral
                        'Accept-Language': 'en-US,en;q=0.9'})
                    time.sleep(timer)
                                                                        
                    if response.status_code == 200:
                        html_content = response.content

                        soup = BeautifulSoup(html_content, 'html.parser')
                        container = soup.select_one('.bde-loop-list')
                        elements = container.select('.bde-loop-item')
                        for element in elements:
                            link = element.find('a').get('href')
                            _title = element.find('h3').text
                            # _element = element.select('li')[-1]
                            # _ele = _element.find('span').text
                            # st.write(_ele)

                            _date = element.select_one('.ee-postmeta-date').text
                            _date = parse_date(_date)
                            st.write(f'{_date} - {_title}')

                            # if link not in [None, '']:
                            #     if re.search('/\d{4}/\d{2}/\d{2}/\w+', link):
                            #         if 'twitter.com/share?' not in link:
                            #             if 'facebook.com/share' not in link:
                            #                 if 'viber://forward?text' not in link:
                            #                     if link not in _urls:

                            #                         _day = int(link.split('/')[-4])
                            #                         _month = int(link.split('/')[-5])
                            #                         _year = int(link.split('/')[-6])
                            #                         _date = datetime(_year, _month, _day)

                            #                         if _date in date_list:
                            #                             _urls.append(link)
                            #                             _dates.append(_date)
                            #                             _titles.append(_title)
                            #                         else:
                            #                             status='break'

    #                 else:
    #                     st.write(response)
    #                     break
                                                
    #         df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})  

    # return df