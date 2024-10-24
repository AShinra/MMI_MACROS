import streamlit as st
import json
from datetime import datetime, timedelta

def user_agents():

    # list of user-agents
    userAgents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36	'
    ]

    return userAgents


def convert_to_date(_datestr):

    _datestrnum = int(_datestr.split(' ')[0])
    _datestrdes = _datestr.split(' ')[1]

    if _datestrdes.lower() in ['days', 'day']:
        _date = datetime.now() - timedelta(days=_datestrnum)
    elif _datestrdes.lower() in ['hours', 'hour', 'hrs', 'hr']:
        _date = datetime.now() - timedelta(hours=_datestrnum)
    elif _datestrdes.lower() in ['minutes', 'minute', 'mins', 'min']:
        _date = datetime.now() - timedelta(minutes=_datestrnum)
    elif _datestrdes.lower() in ['seconds', 'second', 'secs', 'sec']:
        _date = datetime.now() - timedelta(seconds=_datestrnum)    
    else:
        _date = 0

    return _date.date()


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
     button[data-testid="stBaseButton-headerNoPadding"] {
        display: none;
    }    
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)
    
    return