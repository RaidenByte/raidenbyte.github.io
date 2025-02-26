
import streamlit as st

# 设置页面配置
st.set_page_config(
    initial_sidebar_state="collapsed",
    menu_items=None
)

# 注入自定义 CSS
st.markdown("""
    <style>
        /* 隐藏右下角用户头像 */
        [data-testid="appCreatorAvatar"] {
            display: none !important;
        }

        /* 隐藏右下角 Streamlit 品牌图标（SVG） */
        svg[width="303"][height="165"] { 
            display: none !important;
        }

        /* 隐藏整个页脚容器（可选） */
        [data-testid="stFooter"] {
            display: none !important;
        }

        /* 补充隐藏其他可能残留的元素 */
        .stApp footer:first-child,
        [data-testid="scrollToBottomButton"] {
            visibility: hidden !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Web Scrapper88888")
url = st.text_input("Enter a website Url: ")
if st.button("Scrape Website"):
    st.write("yes Scraping the website")
