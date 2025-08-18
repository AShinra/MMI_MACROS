import os
import subprocess
import streamlit as st
from playwright.sync_api import sync_playwright

# Ensure browser is installed
if not os.path.exists("/home/appuser/.cache/ms-playwright"):
    subprocess.run(["playwright", "install", "chromium"], check=True)

def get_page_title(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        title = page.title()
        browser.close()
        return title

st.write(get_page_title("https://www.technewsphilippines.com/page/2/"))