
import streamlit as st
st.set_page_config(
    page_title="我的应用",  # 设置页面标题
    layout="wide",          # 可选：宽布局
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)
st.title("AI Web Scrapper88888")
url = st.text_input("Enter a website Url: ")
if st.button("Scrape Website"):
    st.write("yes Scraping the website")