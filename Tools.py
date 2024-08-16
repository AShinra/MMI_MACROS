import streamlit as st
import json


def title_clean(title, pub):

    f = open('json_files/title_cleaner.json')
    title_json = json.load(f)

    pub_check = title_json[pub]

    for i in pub_check:
        try:
            title = title.replace(i, '')
        except:
            pass
        
    return title


def bg_image():

    # background_image = """
    # <style>
    # [data-testid="stAppViewContainer"] > .main {
    #     background-image: url("https://www.kantar.com/-/media/project/kantar/global/campaigns/analytics/kantar-analytics-live.jpg");
    #     background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    #     background-position: center;  
    #     background-repeat: no-repeat;
    # }
    # </style>
    # """

    # st.markdown(background_image, unsafe_allow_html=True)

    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    [data-testid="baseButton-header"] {
        display: none;
    }
    [data-testid="baseButton-headerNoPadding"] {
        display: none;
    }
    div[data-testid="stToolbarActions"] {
        display: none;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)
    
    return