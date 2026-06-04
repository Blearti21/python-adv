import streamlit as st

with st.from("my_from",clear_on_submit=True):
    name = st.text_input("Name")

    age =  st.slider("Age",min_value=0,max_value=100)

    email = st.text_input("Email")

    biography = st.text_area("Short biio")

    terms = st.checkbox("I agree to the terms and conditions")

    submit_button = st.from_submit_button(label="submit")

if sumbit_button:
    st.write(f"Name :{name}")

    st.write(f"Age: {age}")

    st.write(f"Email: {email}")
    st.write(f"Short Bio: {biography}")

    if terms:
        st.write("you agreed to the terms and conditions.")
    else:
        st.write("you did not agree to the terms and conditions")