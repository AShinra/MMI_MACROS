import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def pampangajournal_scraper(my_range):

    # convert string to dateobject
    st_date = datetime.strptime(my_range[0], '%Y-%m-%d').date()
    en_date = datetime.strptime(my_range[1], '%Y-%m-%d').date()
    
    PROJECT_ID = "pampanga-journal"
    COLLECTION = "articles"  # change if needed

    # https://firestore.googleapis.com/v1/projects/pampanga-journal/databases/(default)/documents/articles

    url = f"https://firestore.googleapis.com/v1/projects/{PROJECT_ID}/databases/(default)/documents/{COLLECTION}"

    response = requests.get(url)

    if response.status_code != 200:
        st.error("Could not fetch data. Try different collection name.")
    else:
        data = response.json()

        _dates = []
        _titles = []
        _urls = []

        # st.write(data)
        for doc in data['documents']:
            # create url
            slug = doc['name'].split('/')[-1]
            _url = f"https://thepampangajournal.com/story/{slug}"
            # get the title
            _title = doc['fields']['title']['stringValue']
            # get the date
            _date = doc['fields']['customDate']['stringValue'].split('T')[0]
            # convert string to date object
            _date = datetime.strptime(_date, '%Y-%m-%d').date()

            if _date >= st_date and _date <= en_date:
                _dates.append(_date)
                _titles.append(_title)
                _urls.append(_url)
    
    df = pd.DataFrame({'Date':_dates, 'Title':_titles, 'URL':_urls})
    df = df.sort_values(by='Date', ascending=False)

    return df