import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import streamlit_shadcn_ui as ui
from Tools import bg_image

# scrapers
from pages.scrapers.scraper_mst import mst
from pages.scrapers.scraper_mt import mt
from pages.scrapers.scraper_bm import bm
from pages.scrapers.scraper_inq import inq
from pages.scrapers.scraper_mal import mal
from pages.scrapers.scraper_bw import bw
from pages.scrapers.scraper_bil import bil

st.set_page_config(layout="wide")
bg_image()

st.markdown("<h1 style='text-align: center;'>URL Fetcher</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1,3])
with col1:

    my_range = ui.date_picker(label='Select Date Range', mode='range', key='my_range', default_value=None)
    
    option = st.selectbox('Select Publication',
                            ('Inquirer.net',
                            'Business Mirror',
                            'Business World',
                            'Manila Times',
                            'Manila Standard',
                            'Malaya Business Insight',
                            'Bilyonaryo'),key='pub_sel_radio')
        
    pro = st.button(label='Process', use_container_width=True)

if pro:
    if my_range in ['', None, []]:
        st.error('Please indicate date range')
    else:
        if st.session_state['pub_sel_radio'] == 'Manila Standard':
            links_collected = mst(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
                        
        elif st.session_state['pub_sel_radio'] == 'Manila Times':
            links_collected = mt(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
        
        elif st.session_state['pub_sel_radio'] == 'Business Mirror':
            links_collected = bm(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
        
        elif st.session_state['pub_sel_radio'] == 'Inquirer.net':
            links_collected = inq(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
        
        elif st.session_state['pub_sel_radio'] == 'Malaya Business Insight':
            links_collected = mal(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
        
        elif st.session_state['pub_sel_radio'] == 'Business World':
            links_collected = bw(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
         
        elif st.session_state['pub_sel_radio'] == 'Bilyonaryo':
            links_collected = bil(my_range)

            with col2:
                st.header(f'Links Collected - {links_collected.shape[0]}')
                st.dataframe(links_collected, hide_index=True)
        
                        
        else:
            with col2:
                st.error('Development Phase')


