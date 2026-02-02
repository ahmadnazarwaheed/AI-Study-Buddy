import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

st.set_page_config(page_title="AI Study Buddy", page_icon="🧠", layout="centered")
st.title("🧠 AI Study Buddy")
st.write("Ask a question and get step-by-step explanations!")

user_question = st.text_input("Type your question here:")

@st.cache_resource(show_spinner=True)
def load_model():
    model_name = "TheBloke/Mistral-7B-Instruct-GGML"  # Free open-source instruct model
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return generator

generator = load_model()

if user_question:
    try:
        with st.spinner("Thinking..."):
            response = generator(user_question, max_length=300, do_sample=True, temperature=0.7)
            answer = response[0]['generated_text']

        st.write("**Your question:**", user_question)
        st.write("**AI answer:**", answer)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
