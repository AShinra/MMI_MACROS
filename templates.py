import streamlit as st
from streamlit_option_menu import option_menu

from BSP_Alert import bsp_main


def template_landing():

    cols = st.columns([2,5,3])

    with cols[0]:
        client = st.radio('Select Client', ['Bangko Sentral ng Pilipinas','JG Summit'])
    with cols[1]:
        raw_file = st.file_uploader('Input Raw File', key='client_raw',label_visibility='collapsed')

    if raw_file == None:
        _disabled = True
    else:
        _disabled = False
    
    if st.button(label='Process File', disabled=_disabled):
        if client == 'Bangko Sentral ng Pilipinas':
            bsp_main(client)
        if client == 'JG Summit':
            bsp_main(client)



    