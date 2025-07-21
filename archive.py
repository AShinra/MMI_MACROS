import streamlit as st
from creds import get_gsheet_client


def local_fetcher_archive():

    client = get_gsheet_client()

    try:
        # sheet = client.open("Your Google Sheet Name").sheet1  # Update with your sheet name
        sheet_id = "1yU-_jdBAF4qYfdM9-dON0neMc77NF4VeDdeNpKlx79A"
        sheet = client.open_by_key("Manila Bulletin")
        values_list = sheet.sheet1.row_values(1)
        st.write(values_list)

    except Exception as e:
        st.error(f"Error accessing Google Sheet: {e}")



    return