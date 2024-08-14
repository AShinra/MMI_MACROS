import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# scrapers
# from scraper_mst import mst

col1, col2 = st.columns(2)

with col1:

    st.header('Links Scraper')

    pub_sel = st.radio(
        'Select Online Publication to scrape',
        ('Manila Bulletin',
        'Inquirer.net',
        'Philstar',
        'Business Mirror',
        'Business World',
        'Manila Times',
        'Manila Standard',
        'Malaya Business Insight',
        'Daily Tribune'))

    pro = st.button(label='Process')


with col2:
    st.success('test')

# if pro:
#     if pub_sel == 'Manila Standard':
#         mst()

#     else:
#         st.error('Development Phase')