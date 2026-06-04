import streamlit as st

tab1,tab2,tab3 = st.tabs(["Tab 1","Tab 2","Tab 3"])

with tab1:
    st.header("content for Tab 1")
    st.writr("this is the content of the first tab")
with tab2:
    st.header("content for Tab 2")
    st.writr("this is the content of the first tab")
with tab3:
    st.header("content for Tab 3")
    st.writr("this is the content of the first tab")