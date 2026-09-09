from enum import unique

import pandas as pd
import streamlit as st
import ploty.express as px

#kjo i merr te dhenat nga file
books_df= pd.read_csv("data")

st.title("Bestselling Books Analysis")

st.write("This app analyze the Amazon top selling books from 2009 to 2022")

st.subheader("summary statistics")

total_books =data.shape[0]

unique_title = date['Name'].unique()
avg_rating = date['User Rating'].mean()
avg_price = date['Price'].mean()

col1,col2,col3,col4=st.colums(4)
col1.metric("Total books",total_books)
col2.metric("Unique Titles",unique_title)
col3.metric("Average rating",avg_racting)
col4.metric("Average price",avg_price)

st.subheader("Date set Preview")
st.write(date.head())

col1,col2=st.columns(2)

with col1:
    st.subheader("top 10 book titles")
    top_title = date["Name"].value_counts.head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("top 10 authors")
    top_title = date["Author"].value_counts().head(10)
    st.bar_chart(top_author)
