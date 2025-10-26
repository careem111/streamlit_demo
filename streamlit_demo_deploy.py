
from langchain_openai import ChatOpenAI
import streamlit as st




# app.py
from langchain_openai import ChatOpenAI
import streamlit as st

st.set_page_config(page_title="AI Chat", page_icon="🤖")

st.title("🤖 Ask Anything from Me")

# Sidebar API key input
with st.sidebar:
    st.header("🔑 Provide Your API key")
    OPENAI_API_KEY = st.text_input("OpenAI API key", type="password")
    st.markdown(
        "Don't have one? [Get it here](https://platform.openai.com/account/api-keys)"
    )

# Validate key
if not OPENAI_API_KEY:
    st.info("👉 Enter your OpenAI API key in the sidebar to continue.")
    st.stop()

# Cache the model so it loads only once
@st.cache_resource(show_spinner=False)
def load_llm(api_key):
    return ChatOpenAI(model="gpt-4o", api_key=api_key, temperature=0.7)

llm = load_llm(OPENAI_API_KEY)

# User input
question = st.text_input("💬 Enter your question:")

if question:
    with st.spinner("Thinking..."):
        response = llm.invoke(question)
    st.success("Answer:")
    st.write(response.content)



