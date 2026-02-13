import streamlit as st
from streamlit_option_menu import option_menu
from Tools import bg_image
from templates import template_landing
from scrapers import scraper_landing
from parser import parsers_landing
# from test_scraper import main_scraper
from archive import local_fetcher_archive
from test_selenium_scraper import pampangajournal_scraper




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
            options=['Home', 'Templates', 'Fetcher', 'Pampanga Journal', 'Archive', 'URL Fetcher'],
            icons=['house', 'file-ruled', 'link', 'link', 'archive', 'link'],
            orientation='vertical',
            default_index=0
        )
    
    # with st.sidebar:
    #     selected = option_menu(
    #         menu_title='',
    #         options=['Home', 'Templates', 'Fetcher', 'Parser', 'Test'],
    #         icons=['house', 'file-ruled', 'link', 'text-paragraph', 'file-ruled'],
    #         orientation='vertical',
    #         default_index=0
    #     )
    
    if selected == 'Templates':
        template_landing()
    
    if selected == 'Fetcher':
        scraper_landing()
    
    if selected == 'Archive':
        local_fetcher_archive()
    
    if selected == 'Pampanga Journal':
        pampangajournal_scraper()
    
    # elif selected == 'Parser':
    #     parsers_landing()
    
    # elif selected == 'Test':
    #     main_scraper()