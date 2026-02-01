import os
import streamlit as st
import openai

# Load your OpenAI API key from Streamlit Secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

# App title and description
st.title("AI Study Buddy")
st.write("Ask a question and get step-by-step explanations and practice exercises!")

# User input
user_question = st.text_input("Type your question here:")

if user_question:
    try:
        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to gpt-4 if available
            messages=[{"role": "user", "content": user_question}]
        )
        
        answer = response.choices[0].message.content
        
        # Display results
        st.write("**Your question:**", user_question)
        st.write("**AI answer:**", answer)
        
    except Exception as e:
        st.error(f"Something went wrong: {e}")
