import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from pathlib import Path




with st.container(border=True):
    st.header('TRIAL')

st.file_uploader('Input Raw File', key='bsp_raw')

if st.session_state['bsp_raw'] != None:
    button_process = st.button('Process File')

    if button_process:

        REPORT_FILE = Path(__file__).parent/f'BSP_Temp/trial.xlsx'
        wb = openpyxl.Workbook(REPORT_FILE)
        wb.save(REPORT_FILE)
        wb.close()

        wb = openpyxl.load_workbook(st.session_state['bsp_raw'])
        ws = wb.active

        df = pd.DataFrame()
        st.write(df)

        # s_row = 8
        # for row in ws.iter_rows(min_row=8, max_col=7):

        

        # result_file = open(REPORT_FILE, 'rb')
        # st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        # st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         

