import streamlit as st
st.title("AI Web Scrapper")
url = st.text_input("Enter a website Url: ")
if st.button("Scrape Website"):
    st.write("Scraping the website")