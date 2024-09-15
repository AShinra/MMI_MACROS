import streamlit as st
from Tools import bg_image
from pages.parsers.parser_bm import bm_parser
from pages.parsers.parser_inq import inq_parser

st.set_page_config(layout="wide")
bg_image()

with st.container(border=True):
    url = st.text_input("Link to Parse", key='_url')
    button_process = st.button('Parse')
    

if button_process:
    if '/businessmirror.com.ph/' in url:
        bm_parser(url)
    elif 'inquirer.net/' in url:
        inq_parser(url)
    else:
        st.error('Wrong link or Website not yet supported')

