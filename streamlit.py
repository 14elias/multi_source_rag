import streamlit as st
import tempfile

from helper import document_loader

st.title("Multi Rag App")

uploaded_file = st.file_uploader("upload file")
query = st.text_input("Ask a question")

if uploaded_file is not None:
    st.write('File Name', uploaded_file.name)
    file_type = uploaded_file.type

    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    documents = document_loader.load(source=file_path, source_type=file_type)
    
    for i, doc in enumerate(documents):
        st.markdown(f"### Page {i + 1}")
        st.text(doc.page_content[:3000])