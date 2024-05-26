import streamlit as st
import pandas as pd
import openpyxl
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from pathlib import Path
import json
import spacy
import subprocess

# try:
#     nlp = spacy.load('en_core_web_md')
# except OSError:
#     from spacy.cli import download
#     download('en_core_web_md')
#     nlp = spacy.load('en_core_web_md')

# nlp = spacy.load('en_core_web_md')

@st.cache_resource
def download_en_core_web_md():
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_md"])




def json_publications():

    f = open('json_files/bsp_publications.json')
    bsp_pub = json.load(f)

    return bsp_pub


def similar_title(a, b):
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

        # download_en_core_web_md()
        nlp = spacy.load('en_core_web_sm')

        df, REPORT_FILE = dataframe_create(st.session_state['bsp_raw'])

        df.columns = ['DATE', 'SOURCE', 'TITLE', 'AUTHOR', 'TYPE', 'CATEGORY', 'LINK']

        df['PRINT LINK'] = 'N/A'
        df['ONLINE LINK'] = 'N/A'
        df['DELETE'] = ''

        df_cat1 = df.groupby('CATEGORY').get_group('TODAYS HEADLINENEWS')
        df_cat2 = df.groupby('CATEGORY').get_group('TODAYS BUSINESS HEADLINENEWS')
        df_cat3 = df.groupby('CATEGORY').get_group('BSP NEWS')

        dfs = []
        dfs.append(df_cat1)
        dfs.append(df_cat2)
        dfs.append(df_cat3)
        
        # load print/online counterparts
        bsp = json_publications()

        broadsheet_list = []
        for k, v in bsp.items():
            broadsheet_list.append(k)

        for _df in dfs:
            for j in _df.index:
                main_title = _df.at[j, 'TITLE']
                main_source = _df.at[j, 'SOURCE']
                main_link = _df.at[j, 'LINK']
                main_type = _df.at[j, 'TYPE']
                
                if main_type in ['Online News', 'Blogs']:
                    _df.at[j, 'ONLINE LINK'] = main_link
                    continue
                elif main_type in ['Tabloid', 'Magazine', 'Provincial']:
                    _df.at[j, 'PRINT LINK'] = main_link
                    _df.at[j, 'DELETE'] = 'DONE'
                    continue
                elif main_source not in broadsheet_list:
                    _df.at[j, 'PRINT LINK'] = main_link
                    _df.at[j, 'DELETE'] = 'DONE'
                    continue
                else:
                    _df.at[j, 'PRINT LINK'] = main_link

                    for k in _df.index:
                        sub_title = _df.at[k, 'TITLE']
                        sub_source = _df.at[k, 'SOURCE']
                        sub_link = _df.at[k, 'LINK']
                        sub_type = _df.at[k, 'TYPE']
                        sub_delete = _df.at[k, 'DELETE']

                        if sub_type != 'Online News':
                            continue
                        else:
                            if sub_source not in bsp[main_source]:
                                continue
                            else:
                                if sub_delete == 'FPR DELETION':
                                    continue
                                else:
                                    similarity_ratio = similar_title(main_title.lower(), sub_title.lower())
                                    if similarity_ratio < 0.75:
                                        continue
                                    else:
                                        _df.at[j, 'ONLINE LINK'] = sub_link
                                        _df.at[k, 'DELETE'] = 'FOR DELETION'

                    _df.at[j, 'DELETE'] = 'DONE'                    

            # drop rows for deletion
            _del = _df[(_df.DELETE == 'FOR DELETION')]
            _df.drop(_del)

            st.dataframe(_df)



        
        

        # result_file = open(REPORT_FILE, 'rb')
        # st.success(f':red[NOTE:] Downloaded file will go to the :red[Downloads Folder]')
        # st.download_button(label='📥 Download Excel File', data= result_file, file_name= f'bsp.xlsx')


         
