import streamlit as st
from streamlit_option_menu import option_menu

from BSP_Alert import bsp_main


def template_landing():

    with st.sidebar:
        selected = option_menu(
            menu_title='',
            options=['BSP', 'MPIC'],
            icons = ['file-spreadsheet', 'file-richtext-fill'],
            orientation='vertical',
            default_index=0
        )
    
    if selected == 'BSP':
        bsp_main()

    return