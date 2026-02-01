import streamlit as st

# Title of the app
st.title("AI Study Buddy")

# Short description
st.write("Hello! This is a test of the workspace. Your AI Study Buddy will go here.")

# User input example
user_question = st.text_input("Ask a question:")

if user_question:
    st.write(f"You asked: {user_question}")
    st.write("AI answer will appear here.")
