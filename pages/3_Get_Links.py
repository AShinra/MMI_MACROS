import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapers
from pages.scrapers.scraper_mst import mst

col1, col2 = st.columns(2)

with col1:

    st.header('Link Scraper')
    with col1.container(border=True):

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

with st.container(border=True):

    if pro:
        if pub_sel == 'Manila Standard':
            links_collected = mst()

            with col2:
                
                st.header('')

                with col2.container(border=True):
                
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
                with col2.container(border=True):
                    st.error('Development Phase')
