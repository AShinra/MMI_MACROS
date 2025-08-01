import streamlit as st
from creds import get_gsheet_client
import pandas as pd


def local_fetcher_archive():   

    col1, col2 = st.columns([0.25, 0.75])

    with col1:
        pub_selection = st.selectbox(
            'Select Publication',
            options=['Manila Bulletin',
                     'Philippine Star',
                     'Daily Tribune',
                     'ABS CBN',
                     'GMA',
                     'PNA']
        )
            
    if pub_selection == 'Manila Bulletin':
        sheet_name = "Manila Bulletin"
    elif pub_selection == 'Philippine Star':
        sheet_name = "Philippine Star"
    elif pub_selection == 'Daily Tribune':
        sheet_name = "Daily Tribune"
    elif pub_selection == 'ABS CBN':
        sheet_name = "ABS CBN"
    elif pub_selection == 'GMA':
        sheet_name = "GMA"
    elif pub_selection == 'PNA':
        sheet_name = "PNA"

    with col2:

        cola, colb = st.columns([0.25, 0.75])
        
        with cola:
            date_selected = st.date_input('Select Date', format="YYYY-MM-DD").isoformat()
            btn_submit = st.button('Check Date', use_container_width=True)
        
        if btn_submit:
            with st.spinner('Checking Archives.....'):
                client = get_gsheet_client()

                try:
                    # sheet = client.open("Your Google Sheet Name").sheet1  # Update with your sheet name
                    sheet_id = "1yU-_jdBAF4qYfdM9-dON0neMc77NF4VeDdeNpKlx79A"
                    sheet = client.open_by_key(sheet_id)
                    value_list = sheet.worksheet(sheet_name).get_all_values()
                    # values_list = sheet.sheet1.row_values(1)
                    df = pd.DataFrame(value_list)
                    df.columns = df.iloc[0]
                    df = df[1:]
                    df['ARTICLE_DATE'] = pd.to_datetime(df['ARTICLE_DATE'])
                    df = df[df['ARTICLE_DATE'] == date_selected]

                    
                    st.header(f'{pub_selection} Article Count - {df.shape[0]}')
                    st.dataframe(df, use_container_width=True, hide_index=True)

                except Exception as e:
                    st.error(f"Error accessing Google Sheet: {e}")

    return