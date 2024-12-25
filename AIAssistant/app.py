from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os

# Set the title of the Streamlit app
st.title("AI Assistant")

# Add some content to the app
st.write("Welcome to the AI Assistant application!")

# You can add more interactive elements here
# Add a sidebar for file uploads
uploaded_files = st.sidebar.file_uploader("Upload Files", accept_multiple_files=True)

# Save uploaded files to the 'data' folder

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join('data', uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.sidebar.success("Files successfully uploaded to the 'data' folder.")


