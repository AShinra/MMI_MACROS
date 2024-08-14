import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapers
from pages.scrapers.scraper_mst import mst
from pages.scrapers.scraper_mt import mt
from pages.scrapers.scraper_bm import bm
from pages.scrapers.scraper_ps import ps


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:

    with col1.container(border=True, height=420):
        st.header('Link Scraper')

        pub_sel = st.radio(
            'Select Online Publication to scrape',
            ('Manila Bulletin',
            'Inquirer.net',
            ':blue[Philstar]',
            ':blue[Business Mirror]',
            'Business World',
            ':blue[Manila Times]',
            ':blue[Manila Standard]',
            'Malaya Business Insight',
            'Daily Tribune'), key='pub_sel_radio')

        pro = st.button(label='Process', use_container_width=True)

if pro:
    if st.session_state['pub_sel_radio'] == ':blue[Manila Standard]':
        links_collected = mst()

        with col2:

            with col2.container(border=True, height=420):
                st.header('Links Collected', )
                st.subheader(links_collected)
                    
    elif st.session_state['pub_sel_radio'] == ':blue[Manila Times]':
        links_collected = mt()

        with col2:

            with col2.container(border=True, height=420):
                st.header('Links Collected', )
                st.subheader(links_collected)
    
    elif st.session_state['pub_sel_radio'] == ':blue[Business Mirror]':
        links_collected = bm()

        with col2:

            with col2.container(border=True, height=420):
                st.header('Links Collected', )
                st.subheader(links_collected)
    
    elif st.session_state['pub_sel_radio'] == ':blue[Philstar]':
        links_collected = ps()

        with col2:

            with col2.container(border=True, height=420):
                st.header('Links Collected', )
                st.subheader(links_collected)
                
    else:
        with col2:
            with col2.container(border=True, height=420):
                st.error('Development Phase')


