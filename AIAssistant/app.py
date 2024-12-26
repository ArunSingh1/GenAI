from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_core.output_parsers import StrOutputParser


from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders import PyPDFLoader

from langchain_milvus import Milvus

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


# Set the title of the Streamlit app
st.title("AI Assistant")

# Add some content to the app
st.write("Welcome to the AI Assistant application!")

# Initialization
if 'uploadedfiles' not in st.session_state:
    st.session_state['uploadedfiles'] = 'None'

# if 'vectors' not in st.session_state:
#     st.session_state['vectors'] =  Milvus()

# You can add more interactive elements here
# Add a sidebar for file uploads
uploaded_files = st.sidebar.file_uploader("Upload Files", accept_multiple_files=True)

# Save uploaded files to the 'data' folder

if uploaded_files:
    for uploaded_file in uploaded_files:
        with open(os.path.join('data', uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
    st.sidebar.success("Files successfully uploaded to the 'data' folder.")
    st.session_state['uploadedfiles'] = True
    

llm= ChatOpenAI(model="gpt-4o-mini")

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}

    """

)


URI = "./milvus.db"

## Vector Enbedding and Objectbox Vectorstore db

def vector_embedding():

    print('vector db running...')

    if "vectors" not in st.session_state:
        st.session_state.embeddings=OpenAIEmbeddings()
        st.session_state.loader=PyPDFLoader("3839_07122024201606_unlocked.pdf") ## Data Ingestion
        st.session_state.docs=st.session_state.loader.load() ## Documents Loading
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs[:20])
        st.session_state.vectors = Milvus.from_documents(  # or Zilliz.from_documents
                documents=st.session_state.final_documents,
                embedding=st.session_state.embeddings,
                connection_args={
                    "uri": "./milvus.db",
                },
                # drop_old=True,  # Drop the old Milvus collection if it exists
            )

    # return st.session_state.vectors

import time

input_prompt=st.text_input("Enter Your Question From Documents")

if st.button("Documents Embedding"):
    vector_embedding()
    st.write("ObjectBox Database is ready")


if input_prompt:
    document_chain=create_stuff_documents_chain(llm,prompt)
    retriever=st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    start=time.process_time()

    response=retrieval_chain.invoke({'input':input_prompt})

    print("Response time :",time.process_time()-start)
    st.write(response['answer'])