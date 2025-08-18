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


# -----------------MST

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime


def mst():

    # convert string to dateobject
    # st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    # en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # _dates = []
    # _titles = []
    # _urls = []
    

    for i in range(1, 2):
        print(i)
        url = f'https://www.technewsphilippines.com/page/{i}/'
        response = requests.get(url)
        print(response.status_code)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            print(soup)
            
            container = soup.select_one('.cat-box-content')
            elements = container.select('article')
            for element in elements:
                _link = element.find('a').get('href')
                print(_link)


                
            # articles = soup.select('.grid-base-post')
            # print(len(articles))
            # for article in articles:
            #     # _datestr = article.find('time').text
            #     # _date = datetime.strptime(_datestr, '%B %d, %Y, %I:%M %p').date()
            #     # _title = article.find('a').text
            #     _url = article.find('a').get('href')
            #     # _url = re.sub('www.', '', _url)
            #     print(_url)
                
    #             if _date >= st_date and _date <= en_date:
    #                 if _url not in _urls:
    #                     _dates.append(_datestr)
    #                     _titles.append(_title)
    #                     _urls.append(_url)

    # df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    
    # return df

mst()