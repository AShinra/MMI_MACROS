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
from pages.scrapers.scraper_ps import ps
from pages.scrapers.scraper_inq import inq
from pages.scrapers.scraper_mal import mal
from pages.scrapers.scraper_bw import bw
from pages.scrapers.scraper_mb import mb

st.set_page_config(layout="wide")
bg_image()

my_range = ui.date_picker(label='Select Date Range', mode='range', key='my_range', default_value=None)

col1, col2 = st.columns(2)

with col1:

    with col1.container(border=True, height=450):
        st.header('Link Scraper')

        pub_sel = st.radio(
            'Select Online Publication to scrape',
            ('Manila Bulletin',
            ':blue[Inquirer.net]',
            'Philstar',
            ':blue[Business Mirror]',
            ':blue[Business World]',
            ':blue[Manila Times]',
            ':blue[Manila Standard]',
            ':blue[Malaya Business Insight]',
            'Daily Tribune'), key='pub_sel_radio')

        pro = st.button(label='Process', use_container_width=True)

if pro:
    if my_range in ['', None, []]:
        st.error('Please indicate date range')
    else:
        if st.session_state['pub_sel_radio'] == ':blue[Manila Standard]':
            links_collected = mst(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
                        
        elif st.session_state['pub_sel_radio'] == ':blue[Manila Times]':
            links_collected = mt(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ':blue[Business Mirror]':
            links_collected = bm(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ':blue[Philstar]':
            links_collected = ps(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ':blue[Inquirer.net]':
            links_collected = inq(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ':blue[Malaya Business Insight]':
            links_collected = mal(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ':blue[Business World]':
            links_collected = bw(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
        
        elif st.session_state['pub_sel_radio'] == ' Manila Bulletin':
            links_collected = mb(my_range)

            with col2:

                with col2.container(border=True, height=450):
                    st.header('Links Collected', )
                    st.subheader(links_collected)
                    
        else:
            with col2:
                with col2.container(border=True, height=450):
                    st.error('Development Phase')


