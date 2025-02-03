import streamlit as st
from streamlit_option_menu import option_menu
from Tools import bg_image
from templates import template_landing
from scrapers import scraper_landing
from parser import parsers_landing



if __name__ == '__main__':

    st.set_page_config(
        page_title="MMI Operations Macro",
        page_icon="👋",
        layout='wide'
    )

    bg_image()

    with st.sidebar:
        selected = option_menu(
            menu_title='',
            options=['Home', 'Templates', 'Fetcher', 'Parser'],
            icons=['house', 'file-ruled', 'link', 'text-paragraph'],
            orientation='vertical',
            default_index=0
        )
    
    if selected == 'Templates':
        template_landing()
    
    elif selected == 'Fetcher':
        scraper_landing()
    
    elif selected == 'Parser':
        parsers_landing()


    