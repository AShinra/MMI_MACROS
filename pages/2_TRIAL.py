import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from pathlib import Path


def dataframe_create(uploaded_file):

    REPORT_FILE = Path(__file__).parent/f'BSP_Temp/trial.xlsx'
    wb = openpyxl.Workbook(REPORT_FILE)
    wb.save(REPORT_FILE)
    wb.close()

    wb = openpyxl.load_workbook(uploaded_file)
    ws = wb.active

    ws.delete_rows(1,7)

    for row in ws.iter_rows(max_col=7):

        if row[0].value == 'TODAYS HEADLINENEWS':
            cat = 'TODAYS HEADLINENEWS'
        elif row[0].value == 'TODAYS BUSINESS HEADLINENEWS':
            cat = 'TODAYS BUSINESS HEADLINENEWS'
        elif row[0].value == 'BSPNEWS':
            cat = 'BSP NEWS'

        if row[0].value == 'DATE':
            row[1].value = 'SOURCE'
            row[2].value = 'TITLE'
            row[3].value = 'AUTHOR'
            row[4].value = 'TYPE'
            row[5].value = 'CATEGORY'
            row[6].value = 'LINK'
        
        if row[2].hyperlink != None:
            row[4].value = row[6].value
            row[5].value = cat
            row[6].value = row[2].hyperlink.target
            row[2].hyperlink = None
    

    for row in ws.iter_rows(max_col=7):

        if row[0].value in ['TODAYS HEADLINENEWS',
                            'TODAYS BUSINESS HEADLINENEWS',
                            'BSPNEWS']:
            row[0].value = ''
    
    for row in ws.iter_rows(min_row=3, max_col=7):
        if row[0].value == 'DATE':
            row[0].value = ''
            row[1].value = ''
            row[2].value = ''
            row[3].value = ''
            row[4].value = ''
            row[5].value = ''
            row[6].value = ''
    
    wb.save(REPORT_FILE)
    wb.close()

    df = pd.read_excel(REPORT_FILE)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.dropna()
    

    return df




with st.container(border=True):
    st.header('TRIAL')

st.file_uploader('Input Raw File', key='bsp_raw')

if st.session_state['bsp_raw'] != None:
    button_process = st.button('Process File')

    if button_process:

        df = dataframe_create(st.session_state['bsp_raw'])

        df['PRINT LINK'] = 'N/A'
        df['ONLINE LINK'] = 'N/A'
        
        st.dataframe(df)

        for row in df.rows:
            st.write(row['TITLE'])
            

        

        # result_file = open(REPORT_FILE, 'rb')
        # st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        # st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         

