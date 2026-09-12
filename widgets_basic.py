import streamlit as st
st.title("INPUT WIDGETS")
name = st.text_input("Your name: ")
age = st.slider("Your ages: ", min_value = 1, max_value = 100, value=18)
if st.button("Select"):
    st.write(f"Hello {name}, you are {age} years old!") 