import streamlit as st
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border
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

        for row in ws.iter_rows(min_row=9, max_col=7):
            s_row = 9

            if row[0].value in [
                'TODAY\'S HEADLINE NEWS',
                'TODAY\'S BUSINESS HEADLINE NEWS',
                'BSP ONLINE NEWS',
                'BSP PRINT NEWS'
                ]:
                ws.merge_cells(start_row=s_row, start_column=1, end_row=s_row, end_column=6)
                color_fill = PatternFill(start_color='0b80f8', end_color='0b80f8', fill_type='solid')
                row[0].style = color_fill

            if row[0].value=='DATE':
                row[1].value='SOURCE'
                row[2].value='TITLE'
                row[3].value='AUTHOR'
                row[4].value='PRINT'
                row[5].value='ONLINE'
            
            if row[2].hyperlink != None:
                if row[6].value=='Online News':
                    row[5].value=row[2].hyperlink.target
                    row[5].hyperlink=row[5].value
                    row[5].value='Online Link'
                    row[5].style = 'Hyperlink'
                else:
                    row[4].value=row[2].hyperlink.target
                    row[4].hyperlink=row[4].value
                    row[4].value='Print Link'
                    row[4].style = 'Hyperlink'

            s_row = s_row + 1

        ws.delete_cols(7,1)
        wb.save(REPORT_FILE)
        wb.close()

        result_file = open(REPORT_FILE, 'rb')
        st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         

