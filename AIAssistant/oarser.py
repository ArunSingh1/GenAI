# import os
# # import bs4
# from langchain_community.document_loaders import WebBaseLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# import os
# from dotenv import load_dotenv
# # from bs4 import BeautifulSoup



# # Load environment variables from .env file
# load_dotenv()


# from langchain_community.document_loaders import PyPDFLoader
# loader=PyPDFLoader('attention.pdf')
# docs=loader.load()


# # Initialize a RecursiveCharacterTextSplitter for splitting text into chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

# # Split the documents into chunks using the text_splitter
# documents = text_splitter.split_documents(docs)

# # Let's take a look at the first document
# documents[1]

# num_documents = len(documents)
# print(f"loaded {num_documents} documents")


# # --------------
# from langchain_milvus import Milvus
# # from langchain_huggingface import HuggingFaceEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import time, pprint
# from langchain_openai import OpenAIEmbeddings

# # Define the embedding model.
# # model_name = "BAAI/bge-large-en-v1.5"
# # model_kwargs = {'device': 'cpu'}
# # encode_kwargs = {'normalize_embeddings': True}
# # embed_model = HuggingFaceEmbeddings(
# #     model_name=model_name,
# #     model_kwargs=model_kwargs,
# #     encode_kwargs=encode_kwargs
# # )
# # EMBEDDING_DIM = embed_model.dict()['client'].get_sentence_embedding_dimension()
# # print(f"EMBEDDING_DIM: {EMBEDDING_DIM}")

# # Chunking
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=51)

# # Create a Milvus collection from the documents and embeddings.
# start_time = time.time()
# docs = text_splitter.split_documents(docs)
# vectorstore = Milvus.from_documents(
#     documents=docs,
#     embedding=OpenAIEmbeddings(),
#     connection_args={
#         "uri": "./milvus_demo.db"},
#     # Override LangChain default values for Milvus.
#     consistency_level="Eventually",
#     drop_old=True,
#     index_params = {
#         "metric_type": "COSINE",
#         "index_type": "AUTOINDEX",
#         "params": {},}
# )
# end_time = time.time()
# print(f"Created Milvus collection from {len(docs)} docs in {end_time - start_time:.2f} seconds")


import os
import time
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_core.text_splitters import RecursiveCharacterTextSplitter
from langchain_milvus.vectorstores import Milvus
# from langchain_core.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
# Load environment variables from .env file
load_dotenv()

# Set the USER_AGENT environment variable
user_agent = os.getenv("USER_AGENT")
if user_agent:
    os.environ["USER_AGENT"] = user_agent

# Load documents
loader = PyPDFLoader('attention.pdf')
docs = loader.load()

# Initialize a RecursiveCharacterTextSplitter for splitting text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

# Split the documents into chunks using the text_splitter
docs = text_splitter.split_documents(docs)

# Initialize Milvus vectorstore
vectorstore = Milvus.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    connection_args={
        "uri": "./milvus_demo.db"
    },
    consistency_level="Eventually",
    drop_old=True,
    index_params={
        "metric_type": "COSINE",
        "index_type": "AUTOINDEX",
        "params": {},
    }
)

start_time = time.time()
try:
    # Perform any operations with the vectorstore here
    query = "Your query here"
    print(vectorstore.similarity_search(query, k=1))
finally:
    # Ensure Milvus is properly shut down
    vectorstore.release_all()

end_time = time.time()
print(f"Created Milvus collection from {len(docs)} docs in {end_time - start_time:.2f} seconds")