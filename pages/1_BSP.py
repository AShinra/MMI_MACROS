import streamlit as st
import openpyxl
from pathlib import Path

with st.container(border=True):
    st.header('Bangko Sentral ng Pilipinas Macro')

st.file_uploader('Input Raw File', key='bsp_raw')

if st.session_state['bsp_raw'] != None:
    button_process = st.button('Process File')

    if button_process:

        st.write(Path(__file__).parent)

        # REPORT_FILE = Path(__file__).parent/f'BSP_Temp/bsp.xlsx'
        # wb = openpyxl.Workbook(REPORT_FILE)
        # wb.save(REPORT_FILE)
        # wb.close()

        wb = openpyxl.load_workbook(st.session_state['bsp_raw'])
        ws = wb.active

        for row in ws.iter_rows(min_row=9, max_col=6):
            if row[0]=='DATE':
                row[1]='SOURCE'
                row[2]='TITLE'
                row[3]='AUTHOR'
                row[4]='PRINT'
                row[5]='ONLINE'
                
            
            if row[2].hyperlink != None:
                st.write(row[2].hyperlink[1])
                # row[4].value=row[2].hyperlink
                # row[4].hyperlink=row[4].value
    


         

