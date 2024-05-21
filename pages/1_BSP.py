import streamlit as st
import openpyxl
from pathlib import Path

with st.container(border=True):
    st.header('Bangko Sentral ng Pilipinas Macro')

st.file_uploader('Input Raw File', key='bsp_raw')

if st.session_state['bsp_raw'] != None:
    button_process = st.button('Process File')

    if button_process:
        
        REPORT_FILE = Path(__file__).parent/f'BSP_Temp/bsp.xlsx'
        wb = openpyxl.Workbook(REPORT_FILE)
        wb.save(REPORT_FILE)
        wb.close()

        wb = openpyxl.load_workbook(st.session_state['bsp_raw'])
        ws = wb.active

        for row in ws.iter_rows(min_row=9, max_col=6):
            if row[0].value=='DATE':
                row[1].value='SOURCE'
                row[2].value='TITLE'
                row[3].value='AUTHOR'
                row[4].value='PRINT'
                row[5].value='ONLINE'
                
            
            if row[2].hyperlink != None:
                row[4].value=row[2].hyperlink.target
                row[4].hyperlink=row[4].value

    
        wb.save(REPORT_FILE)
        wb.close()

        result_file = open(REPORT_FILE, 'rb')
        st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         

