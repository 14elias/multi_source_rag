import streamlit as st

st.title("Multi Rag App")

uploaded_file = st.file_uploader("upload file")
query = st.text_input("Ask a question")

if uploaded_file is not None:
    st.write('File Name', uploaded_file.name)
    st.write('File type', uploaded_file.type)
    st.write('File size(bytes)', uploaded_file.size)

if query:
    st.write("user query", query)