import streamlit as st
from creds import get_gsheet_client


def local_fetcher_archive():

    pub_selection = st.radio(
        'Publication',
        options=['Manila Bulletin', 'Philippine Star'],
        horizontal=True)
    
    if pub_selection == 'Manila Bulletin':
        sheet_name = "Manila Bulletin"
    elif pub_selection == 'Philippine Star':
        sheet_name = "Philippine Star"

    client = get_gsheet_client()

    try:
        # sheet = client.open("Your Google Sheet Name").sheet1  # Update with your sheet name
        sheet_id = "1yU-_jdBAF4qYfdM9-dON0neMc77NF4VeDdeNpKlx79A"
        sheet = client.open_by_key(sheet_id)
        value_list = sheet.worksheet(sheet_name)
        # values_list = sheet.sheet1.row_values(1)
        st.write(value_list)

    except Exception as e:
        st.error(f"Error accessing Google Sheet: {e}")



    return