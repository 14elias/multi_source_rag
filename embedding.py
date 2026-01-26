from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
import os

load_dotenv()


def embed(chunks):
    model = "sentence-transformers/all-mpnet-base-v2"

    embedding=HuggingFaceEndpointEmbeddings(
        model=model,
        task="feature-extraction",
        huggingfacehub_api_token=os.getenv('HUGGING_API_KEY'),
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        collection_name="source-aware-rag"
    )

    return vector_store


def retrieve(query: str, vector_store: Chroma):
    retrieved_docs = vector_store.similarity_search(
        query=query,
        k=3
    )

    return retrieved_docs