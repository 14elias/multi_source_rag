import streamlit as st

from langchain_openai import ChatOpenAI
import tempfile

import os
from dotenv import load_dotenv

from helper import document_loader
from splitter import splitter
from embedding import embed, retrieve
from query_constructor import build_llm_prompt



st.title("Multi Rag App")

source_mode = st.selectbox(
    "Choose input type",
    ["Upload File", "URL"]
)

query = st.text_input("Ask a question")

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv('API_KEY'),
    base_url="https://openrouter.ai/api/v1"
)


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
        vectore_store = embed(chunks=chunks)

    if query:
        retrieved_result = retrieve(
            query= query,
            vector_store= vectore_store
        )

        context=''
        for retrieved in retrieved_result:
            context += retrieved.page_content

        prompt = build_llm_prompt(context=context, query=query)

        result = model.invoke(prompt)
        st.write(result.content)


run_streamlit()