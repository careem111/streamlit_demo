
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.globals import set_debug

set_debug(True)

st.title("Ask Anything from Me")
with st.sidebar:
    st.title("Provide Your API key")
    OPENAI_API_KEY = st.text_input("OpenAI API key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter Your OPENAI API key to continue")
    st.stop()

llm=ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)



question=st.text_input("Enter the question: ")

if question:
    response = llm.invoke(question) 
    st.write(response.content)



