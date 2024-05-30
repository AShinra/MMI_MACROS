import streamlit as st

@st.cache_resource
def bg_image():

    # old bg
    # https://www.kantar.com/-/media/project/kantar/global/campaigns/analytics/kantar-analytics-live.jpg
    # https://wallpapers.com/images/high/graphic-design-background-45n565dokok0gqpv.webp

    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://www.kantar.com/-/media/project/kantar/global/campaigns/analytics/kantar-analytics-live.jpg");
        background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
        background-position: center;  
        background-repeat: no-repeat;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

    return


if __name__ == '__main__':

    st.set_page_config(
        page_title="MMI Operations Macro",
        page_icon="👋",
    )

    bg_image()