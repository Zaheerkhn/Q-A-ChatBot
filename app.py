import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API key and project settings
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] =  os.getenv("LANGCHAIN_PROJECT")
# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #f0f9ff, #cbebff);
            font-family: 'Arial', sans-serif;
        }
        .header {
            background-color: #34C759;
            color: white;
            padding: 30px;
            text-align: center;
            border-radius: 12px;
            margin-bottom: 20px;
        }
        .response-box {
            background-color: #f9f9f9;
            border: 1px solid #34C759;
            border-radius: 10px;
            padding: 15px;
            margin: 15px 0;
            font-size: 16px;
            color: #333333;
        }
        .footer {
            text-align: center;
            color: #888;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app with a header
st.markdown('<div class="header"><h1>Q&A ChatBot</h1><h3>Your AI-powered assistant!</h3></div>', unsafe_allow_html=True)

# Define the prompt template
prompt = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "{question}")
    ]
)

# Function to generate response from Groq model
def generate_response(question, api_key, llm, temperature, max_tokens):
    llm_instance = ChatGroq(model=llm, api_key=api_key, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm_instance | output_parser
    response = chain.invoke({"question": question})
    return response

# Sidebar for settings
st.sidebar.title("🔧 Settings")

api_key = st.sidebar.text_input("🔑 Enter your API key:", type="password")
llm = st.sidebar.selectbox(
    "🤖 Select a Model:",
    ["Deepseek-R1-Distill-Llama-70b", "Gemma2-9b-It", "Llama-3.3-70b-Specdec", "Mixtral-8x7b-32768"]
)
temperature = st.sidebar.slider("🌡️ Temperature", min_value=0.0, max_value=1.0, value=0.5)
max_tokens = st.sidebar.slider("📝 Max Tokens", min_value=50, max_value=2048, value=1000)

# Main interface
st.write("💬 Go ahead and ask any question.")
user_input = st.text_input("🔍 Enter your question:")

if user_input:
    if not api_key:
        st.error("🚫 Please enter a valid Groq API key.")
    else:
        with st.spinner("Connecting to AI... 🔄"):
            response = generate_response(user_input, api_key, llm, temperature, max_tokens)
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)
else:
    st.info("Please provide a query to get a response.")

# Footer
st.markdown('<div class="footer">Powered by LangChain and Streamlit for smarter conversations 💡</div>', unsafe_allow_html=True)

