import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

def get_page_source(url):
    # Set up Chrome options
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set path to Chrome binary if running in cloud environment
    chrome_path = "/usr/bin/chromium-browser"
    if os.path.exists(chrome_path):
        options.binary_location = chrome_path

    # Install and start ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    page_source = driver.page_source
    driver.quit()
    return page_source


def main_scraper():
    # Streamlit UI
    st.title("Web Scraper with Selenium & Streamlit")
    url = st.text_input("Enter a URL to scrape:")

    if st.button("Scrape"):
        if url:
            with st.spinner("Scraping..."):
                try:
                    page_content = get_page_source(url)
                    st.success("Scraping completed!")
                    st.text_area("Page Source:", page_content[:2000])  # Show first 2000 chars
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Please enter a valid URL.")