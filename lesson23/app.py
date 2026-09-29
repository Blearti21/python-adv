from http.client import responses

import streamlit as st
import requests
import pandas as pd

st.title("Project managemet App")

st.header("Add a Developer")
dev_name= st.text_input("Developer Name")
dev_experience = st.number_input("Experience(Years)",min_value=0,max_value=50,value=0)

if st.button("Create Developer"):
    dev_date={"name":dev_name,"experience":dev_experience}
    response = requests.post("http://localhost:8000/developers",json=dev_date)
    st.json(response.json())


st.header("Add a proejct")
proj_title = st.text_input("Project title")
proj_desc = st.text_input("Project description")
proj_langs = st.text_input("Languages Used (Coma-separeted)")
lead_dev_name = st.text_input("Developer Name")
lead_dev_exp=st.number_input("Experience(Years)",min_value=0,max_value=50,value=0)

if st.button("Create Developer"):
    lead_dev_date={"name":dev_name,"experience":dev_experience}
    proj_date={
        "title":proj_title
        "description":proj_desc,
        "languages":proj_langs.split(",")
        "lead_developer":lead_dev_date
    }
    response = requests.post("http://localhost:8000/developers",json=dev_date)
    st.json(response.json())