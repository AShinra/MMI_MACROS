import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import streamlit_shadcn_ui as ui
from Tools import bg_image
import random


def bm_parser(url):

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

    _section = ''
    _title = ''
    _author = ''
    _date = ''
    _img = []
    _content = ''


    response = requests.get(url, headers={'User-Agent':random.choice(userAgents)})

    if response.status_code == 200:
        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        container = soup.find(id='content')

        _section = container.find('header').find('a').text
        _title = container.find(class_='entry-title').text
        _author = container.find('span', class_='author').text
        _date = container.find('li', class_='meta-date').text

        # get image from header
        _img.append(container.find('section', class_='post-media').find('a').get('href'))

        element = container.find('section', class_='entry-content')

        # get images from content
        image_elements = element.find_all('figure')
        for image_element in image_elements:
            _img.append(image_element.find('img').get('src'))

        for x in element.find_all('div'):
            x.decompose()
        
        for x in element.find_all(style="font-family: 'Open Sans', arial, sans-serif; font-size: 12px"):
            x.decompose()
        
        for ele in element.find_all('p'):
            _content += ' '
            _content += ele.text
            
                
    with st.container(border=True):

        st.subheader('TITLE')
        with st.container(border=True):
            st.code(_title)



        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader('DATE')
            st.code(_date)

        with col2:
            st.subheader('AUTHOR')
            st.code(_author)
        
        with col3:
            st.subheader('SECTION')
            st.code(_section)

        if len(_img) > 1:
            st.subheader('IMAGE LINKS')
        else:
            st.subheader('IMAGE LINK')

        for i in _img:
            st.code(i)

        st.subheader('CONTENT')
        with st.container(border=True, height=500):
            st.write(_content)
