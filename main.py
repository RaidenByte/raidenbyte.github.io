
import streamlit as st
st.set_page_config(
    page_title="Your App", 
    page_icon="🎯",
    initial_sidebar_state="collapsed",  # 初始折叠侧边栏
    menu_items={
        'Get Help': None,              # 隐藏右上角 "Get Help"
        'Report a bug': None,          # 隐藏 "Report a bug"
        'About': None                   # 隐藏 "About"
    }
)
st.title("AI Web Scrapper88888")
url = st.text_input("Enter a website Url: ")
if st.button("Scrape Website"):
    st.write("yes Scraping the website")