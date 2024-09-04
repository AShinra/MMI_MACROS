import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import random
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


userAgents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36	'
]



def fb_scraper():
    
    fb_url = input('Input facebook url ===>>> ')

    # convert string to dateobject
    # st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    # en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()

    # get sections
    # pub_sections = get_sections()
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome()
    # driver.get('https://www.facebook.com/ANCalerts/')
    # driver.get('https://www.facebook.com/gmanews?mibextid=ZbWKwL')
    # driver.get('https://www.facebook.com/DZXLNews')
    driver.get(fb_url)

    # data-visualcompletion="css-img"

    my_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Close']")))
    # my_close = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-visualcompletion='ignore']")))
    # x = my_close.find_element(By.ID, 'facebook')
    # st.write(x)
    
    my_close.click()

    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(1, 10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        last_height = driver.execute_script("return document.body.scrollHeight")
    

    news_links = []

    links = driver.find_elements(By.CSS_SELECTOR, "a[role='link']")
    for link in links:
        _url = link.get_attribute('href')
        if '/posts/' in _url:
            news_links.append(_url)
    
    print(f'Collected {len(news_links)} news links')
    print(news_links)

    driver.close()

    
fb_scraper()