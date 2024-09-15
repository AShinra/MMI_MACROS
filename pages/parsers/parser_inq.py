import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import streamlit_shadcn_ui as ui
from Tools import bg_image
import random


def inq_parser(url):

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

        header = soup.find('div', id='art-head-group')
        
        # get section
        element = header.find('div', id='bc-share')
        for ele in element.findAll('div'):
            if 'Array' in ele.text:
                ele.decompose()
        
        try:
            _section = element.text.split(',')[0].strip()
        except:
            _section = element.text

        # get title
        _title = header.find('h1', class_='entry-title').text

        # get author
        _author_date = header.find('div', id='byline_share')
        try:
            _author = _author_date.find('div', id='art_author').find('span').find('a').text
        except:
            _author = 'No Author'
        
        # get date
        _date = _author_date.find('div', id='art_plat').find('a').next_sibling
        _date = _date.split('/')[1].strip()

        container = soup.find('div', id='article_content')
        element = container.find('div')

        # decompose unwanted elements from content
        for ele in element.findAll('div', id='billboard_article'):
            ele.decompose()
        
        for ele in element.findAll('p'):
            for x in ele.findAll('strong'):
                if 'READ:' in x.text:
                    x.decompose()
        
        for ele in element.findAll('div', id='article-new-featured'):
            ele.decompose()

        for ele in element.findAll('i', id='art_cont'):
            ele.decompose()
        
        for ele in element.findAll('div', class_='sib-form'):
            ele.decompose()

        for ele in element.findAll('div', id='rn-2023'):
            ele.decompose()
        
        for ele in element.findAll('div', id='lsmr-latest'):
            ele.decompose()
        
        for ele in element.findAll('div', id='lsmr-mostread'):
            ele.decompose()
        
        for ele in element.findAll('a'):
            for x in ele.findAll('span'):
                if x.text == 'View comments':
                    ele.decompose()

        _content = element.text

        for ele in element.findAll('picture'):
            for x in ele.findAll('source'):
                try:
                    _img.append(x.get('data-lazy-srcset').split('.avif')[0])
                except:
                    pass
        
        for ele in element.findAll('img'):
            x = ele.get('src')
            if 'data:image' not in x:
                _img.append(x)
                
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
