import streamlit as st
import tempfile

from helper import document_loader


st.title("Multi Rag App")

source_mode = st.selectbox(
    "Choose input type",
    ["Upload File", "URL"]
)

def run_streamlit():
    # query = st.text_input("Ask a question")
    if source_mode =='Upload File':
        uploaded_file = st.file_uploader("upload file")

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

    elif source_mode == 'URL':
        url = st.text_input("Enter webpage URL")
        if url:
            documents =document_loader.load(source=url, source_type="web")

            for i, doc in enumerate(documents):
                st.markdown(f"### Page {i + 1}")
                st.text(doc.page_content[:3000])



run_streamlit()