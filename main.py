
import streamlit as st

# 页面配置
st.set_page_config(
    initial_sidebar_state="collapsed",
    menu_items=None
)

# 注入 CSS
st.markdown("""
    <style>
        /* 隐藏所有干扰元素 */
        #MainMenu, header, footer, [data-testid="collapsedControl"] {display: none !important;}
        /* 调整主内容区域为全宽 */
        .block-container {padding: 0; max-width: 100% !important;}
        .stApp > div {padding: 0;}
    </style>
""", unsafe_allow_html=True)

st.title("AI Web Scrapper88888")
url = st.text_input("Enter a website Url: ")
if st.button("Scrape Website"):
    st.write("yes Scraping the website")