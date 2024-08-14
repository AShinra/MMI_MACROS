import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapers
from pages.scrapers.scraper_mst import mst
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
            'Manila Times',
            ':blue[Manila Standard]',
            'Malaya Business Insight',
            'Daily Tribune'))

    pro = st.button(label='Process', )

with st.container(border=True, height=500):

    if pro:
        if pub_sel == ':blue[Manila Standard]':
            links_collected = mst()

            with col2:
                
                st.header('')

                with col2.container(border=True, height=300):
                
                    try:
                        st.header('Links Collected')
                    except:
                        pass

                    try:
                        st.subheader(links_collected)
                    except:
                        pass
                    
        else:
            with col2:
                st.header('')
                with col2.container(border=True, height=300):
                    st.error('Development Phase')
