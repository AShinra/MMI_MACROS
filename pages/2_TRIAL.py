import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from pathlib import Path
import spacy
import json


def json_publications():

    f = open('json_files/bsp_publications.json')
    bsp_pub = json.load(f)

    return bsp_pub


def similar_title(a, b):

    # a_tokens = a.split(' ')
    # b_tokens = b.split(' ')

    nlp = spacy.load('en_core_web_md')
    # a1 = nlp(' '.join(a_tokens))
    # b1 = nlp(' '.join(b_tokens))
    a1 = nlp(a)
    b1 = nlp(b)
    return a1.similarity(b1)




def dataframe_create(uploaded_file):

    REPORT_FILE = Path(__file__).parent/f'BSP_Temp/trial.xlsx'
    wb = openpyxl.Workbook(REPORT_FILE)
    wb.save(REPORT_FILE)
    wb.close()

    wb = openpyxl.load_workbook(uploaded_file)
    ws = wb.active


    s_row = 1
    for row in ws.iter_rows():
        try:
            ws.unmerge_cells(start_row=s_row, start_column=1, end_row=s_row, end_column=7)
        except:
            pass
        s_row += 1

    

    for row in ws.iter_rows(max_col=7):

        if row[0].value == 'TODAYS HEADLINENEWS':
            cat = 'TODAYS HEADLINENEWS'
        elif row[0].value == 'TODAYS BUSINESS HEADLINENEWS':
            cat = 'TODAYS BUSINESS HEADLINENEWS'
        elif row[0].value == 'BSPNEWS':
            cat = 'BSP NEWS'
        
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

    ws.delete_rows(1,7)
    wb.save(REPORT_FILE)
    wb.close()

    df = pd.read_excel(REPORT_FILE)
    # df.columns = df.iloc[0]
    # df = df.drop(df.index[0])    

    return df, REPORT_FILE




with st.container(border=True):
    st.header('TRIAL')

st.file_uploader('Input Raw File', key='bsp_raw')

if st.session_state['bsp_raw'] != None:
    button_process = st.button('Process File')

    if button_process:

        df, REPORT_FILE = dataframe_create(st.session_state['bsp_raw'])

        df.columns = ['DATE', 'SOURCE', 'TITLE', 'AUTHOR', 'TYPE', 'CATEGORY', 'LINK']

        df['PRINT LINK'] = 'N/A'
        df['ONLINE LINK'] = 'N/A'
        df['DELETE'] = ''

        grouped = df.groupby(df.CATEGORY)
        df1 = grouped.get_group('TODAYS HEADLINENEWS')
        df2 = grouped.get_group('TODAYS BUSINESS HEADLINENEWS')
        df3 = grouped.get_group('BSP NEWS')

        st.dataframe(df1)
        # st.dataframe(df2)
        # st.dataframe(df3)

        # for i in df.index:
        #     st.write(df['SOURCE'][i], df['TITLE'][i])

        l, w = df1.shape
        st.write(l)
        st.write(w)
        st.write(df1['TITLE'][1])

        bsp = json_publications()
        


        main_title = df1['TITLE'][1]
        main_source = df1['SOURCE'][1]
        main_link = df1['LINK'][1]
        
        for i in df1.index:
            _title = df1['TITLE'][i]
            _source = df1['SOURCE'][i]
            _link = df1['LINK'][i]
            _type = df1['TYPE'][i]

            st.write(_title)

            if i == 1:
                continue
            elif _type == 'Online News':
                if _source not in bsp[main_source]:
                    pass
                elif _source in bsp[main_source]:
                    similarity_ratio = similar_title(main_title, _title)
                    if similarity_ratio >= 0.9:
                        df1.at[1, 'ONLINE LINK'] = _link
                        df1.at[1, 'PRINT LINK'] = main_link
                        df1.at[1, 'DELETE'] = 'NO'
                        df1.at[i, 'DELETE'] = 'YES'
                    else:
                        st.write('THey are not similar')
            else:
                continue


        st.dataframe(df1)    
        

        # result_file = open(REPORT_FILE, 'rb')
        # st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        # st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         
