from playwright.sync_api import sync_playwright
import streamlit as st

def get_page_title(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        browser.close()
        return title

st.write(get_page_title("https://www.technewsphilippines.com/page/2/"))