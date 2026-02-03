from langchain_community.retrievers import BM25Retriever


def bm25_retriever(docs):
    bm25_retriever = BM25Retriever.from_documents(docs)
    bm25_retriever.k = 3

    return bm25_retriever