import streamlit as st
from scrape import scrape_website,extract_body_content,clean_body_content,split_dom_content

st.title('Scrape your data')
url = st.text_input("enter url of website: ")

if st.button("Scrape site"):
    st.write("scraping the website")
    result = scrape_website(url)
    
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    st.session_state.chunks = clean_content                         # can be accessed later

    with st.expander("view DOM content"):                                 # this is basically a button and upon clicking it will expand the dom content that is written in text area
        st.text_area("DOM content",clean_content,height=300)              # this is a text area and will expand upon expanding and will have intial height as 300
    

