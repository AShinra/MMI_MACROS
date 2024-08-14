import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapers
from pages.scrapers.scraper_mst import mst
from pages.scrapers.scraper_mt import mt


def link_count(links_collected):

    with col2:
        st.header('')

        with col2.container(border=True, height=300):
            st.subheader('Links Collected', )
            st.subheader(links_collected)

    return


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:

    st.header('Link Scraper')
    with col1.container(border=True, height=300):

        pub_sel = st.radio(
            'Select Online Publication to scrape',
            ('Manila Bulletin',
            'Inquirer.net',
            'Philstar',
            'Business Mirror',
            'Business World',
            ':blue[Manila Times]',
            ':blue[Manila Standard]',
            'Malaya Business Insight',
            'Daily Tribune'), key='pub_sel_radio')

    pro = st.button(label='Process', use_container_width=True)

if pro:
    if st.session_state['pub_sel_radio'] == ':blue[Manila Standard]':
        links_collected = mst()
        link_count(links_collected)
            
            
    elif st.session_state['pub_sel_radio'] == ':blue[Manila Times]':
        links_collected = mt()
        link_count(links_collected)
                
    else:
        with col2:
            st.header('')
            with col2.container(border=True, height=300):
                st.error('Development Phase')


