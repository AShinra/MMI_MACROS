# import webdriver 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pathlib import Path
import streamlit as st



def mb_scraper():

    # path to gecko file
    gecko_path = Path(__file__).parent/f'Utility_Files/geckodriver.exe'

    # run firefox as headless
    options_firefox = webdriver.FirefoxOptions
    options_firefox.add_argument("--headless")
    driver = webdriver.Firefox(gecko_path, options=options_firefox)

    # create webdriver object 
    # driver = webdriver.Firefox()

    # get google.co.in 
    driver.get("https://mb.com.ph/sitemap")

    link_objects = driver.find_elements(By.CLASS_NAME, 'title-label')

    all_category_links = {}
    for i in link_objects:
        link = i.get_attribute('href')
        cat = i.text
        if link not in [
            'https://mb.com.ph/contact-us',
            'https://mb.com.ph/corporate-governance',
            'https://mb.com.ph/privacy-policy',
            'https://mb.com.ph/our-company',
            'https://mb.com.ph/terms-and-conditions',
            None]:
            if cat != '':
                all_category_links[cat] = link
                
    for cat_name, cat_link in all_category_links.items():
        driver.get(cat_link)

        try:
            element1 = driver.find_element(By.XPATH, '//*[@class="col-sm-6 col-md-8 col-lg-8 col-12"]')
            cat_links = element1.find_elements(By.XPATH, '//*[@class="mb-font-article-title mt-0 mb-1"]/a')
            
        except:
            pass
        
        else:
            st.success(cat_name)
            for i in cat_links:
                art_link = i.get_attribute('href')
                st.write(art_link)

        
    driver.quit()


# main process

process_button = st.button('Process', key='Prcoess')

if process_button:
    mb_scraper()