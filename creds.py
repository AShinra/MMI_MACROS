import streamlit as st
from streamlit_option_menu import option_menu
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def get_gsheet_client():
    # Load credentials from Streamlit secrets
    credentials_dict = {
        "type": st.secrets["gcp_service_account"]["type"],
        "project_id": st.secrets["gcp_service_account"]["project_id"],
        "private_key_id": st.secrets["gcp_service_account"]["private_key_id"],
        "private_key": st.secrets["gcp_service_account"]["private_key"],
        "client_email": st.secrets["gcp_service_account"]["client_email"],
        "client_id": st.secrets["gcp_service_account"]["client_id"],
        "auth_uri": st.secrets["gcp_service_account"]["auth_uri"],
        "token_uri": st.secrets["gcp_service_account"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["gcp_service_account"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["gcp_service_account"]["client_x509_cert_url"]
    }
    
    credentials = Credentials.from_service_account_info(credentials_dict, scopes=["https://www.googleapis.com/auth/spreadsheets"])
    client = gspread.authorize(credentials)
    return client