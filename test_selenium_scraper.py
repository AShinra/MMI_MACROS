import streamlit as st
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def pampangajournal_scraper():
    st.title("The Pampanga Journal Scraper")

    if st.button("Scrape Site"):

        homepage = "https://thepampangajournal.com"

        # Chrome options
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(homepage)

        # Wait until articles appear
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3.headline"))
        )

        links = []

        # Count articles first
        articles_count = len(driver.find_elements(By.CSS_SELECTOR, "h3.headline"))

        for i in range(articles_count):

            # Re-fetch elements every loop (VERY IMPORTANT for React)
            articles = driver.find_elements(By.CSS_SELECTOR, "h3.headline")

            # Scroll to element
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", articles[i])
            time.sleep(1)

            # Click article
            driver.execute_script("arguments[0].click();", articles[i])

            # Wait until URL changes
            WebDriverWait(driver, 10).until(
                lambda d: d.current_url != homepage
            )

            # Store URL
            links.append(driver.current_url)

            # Go back to homepage
            driver.get(homepage)

            # Wait again for articles to reload
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h3.headline"))
            )

        driver.quit()

        st.success("Scraping completed!")
        st.write("Found article links:")
        st.write(links)
