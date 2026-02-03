import streamlit as st

from langchain_openai import ChatOpenAI
import tempfile

import os
from dotenv import load_dotenv

from helper import document_loader
from splitter import splitter
from embedding import embed, retrieve, load_vector_store
from graph import ingestion, client, indexes
from graph_retriver import graph_search
from qa_service import answer_question
from model import get_llm
from hybrid_retriever import hybrid_retrieve



st.title("Multi Rag App")

source_mode = st.selectbox(
    "Choose input type",
    ["Upload File", "URL"]
)

query = st.text_input("Ask a question")

model = get_llm()


documents = []

def run_streamlit():
    global documents
    if source_mode =='Upload File':
        uploaded_file = st.file_uploader("upload file")

        if uploaded_file is not None:
            st.write('File Name', uploaded_file.name)
            file_type = uploaded_file.type

            with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
                tmp.write(uploaded_file.read())
                file_path = tmp.name

            documents = document_loader.load(source=file_path, source_type=file_type)

    elif source_mode == 'URL':
        url = st.text_input("Enter webpage URL")
        if url:

            documents =document_loader.load(source=url, source_type="web")

    if documents:
        chunks = splitter(documents)
        embed(chunks=chunks)

    if query:
        vectore_store=load_vector_store()
        retrieved_result = hybrid_retrieve(
            query=query,
            vectore_store=vectore_store,
            docs=chunks
        )

        context=''
        for retrieved in retrieved_result:
            context += retrieved.page_content
        

        result = answer_question(context= context, question= query)
    
        st.write(result)


run_streamlit()