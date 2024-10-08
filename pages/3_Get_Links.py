import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import streamlit_shadcn_ui as ui
from Tools import bg_image
import openpyxl

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

    my_range = ui.date_picker('DATE RANGE', mode='range', key='my_range', default_value=None)
    
    option = st.selectbox('**_:blue[SELECT PUBLICATION]_**',
                            ('Inquirer.net',
                            'Business Mirror',
                            'Business World',
                            'Manila Times',
                            'Manila Standard',
                            'Malaya Business Insight',
                            'Bilyonaryo'),key='pub_sel_radio')
        
    pro = st.button(label='**_:blue[PROCESS]_**', use_container_width=True)

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


    links_collected.to_excel('pages/fetcher_temp/temp.xlsx', index=None)

    wb = openpyxl.load_workbook('pages/fetcher_temp/temp.xlsx')
    ws = wb.active

    for row in ws.iter_rows(min_col=3, max_col=3, min_row=2):
        for cl in row:
            cl.hyperlink = cl.value

    wb.save('pages/fetcher_temp/temp.xlsx')
    wb.close()
    _file = 'pages/fetcher_temp/temp.xlsx'

    result_file = open(_file, 'rb')
    col1, col2, col3 = st.columns(3)

    with col2:
        st.download_button(label='📥 Download Current Result', data=result_file ,file_name= f'Fetched_URL.xlsx',use_container_width=True)

