from langchain_text_splitters import RecursiveCharacterTextSplitter


def splitter(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    result = splitter.split_documents(documents=docs)

    return result