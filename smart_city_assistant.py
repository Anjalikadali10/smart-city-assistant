import streamlit as st

st.title("Smart City Assistant")

user_input = st.text_input("Ask me something about the city")

if user_input:
    response = f"You asked: '{user_input}'. Here's a smart city insight..."
    st.write(response)