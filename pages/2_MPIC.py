import streamlit as st
from Tools import bg_image




bg_image()

with st.container(border=True):
    
    st.header('Metro Pacific Investments Corporation')

st.file_uploader('Input Raw File', key='mpic_raw')