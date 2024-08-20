import streamlit as st
from Tools import bg_image
from Templates import templates


if __name__ == '__main__':

    st.set_page_config(
        page_title="MMI Operations Macro",
        page_icon="👋",
    )

    bg_image()
    templates()
    