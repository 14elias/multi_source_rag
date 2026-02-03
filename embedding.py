from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from settings import settings
import os

load_dotenv()


def embed(chunks):
    model = "sentence-transformers/all-mpnet-base-v2"

    embedding=HuggingFaceEndpointEmbeddings(
        model=model,
        task="feature-extraction",
        huggingfacehub_api_token=settings.HUGGING_API_KEY,
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        collection_name="source-aware-rag",
        persist_directory="./chroma_db"
    )

    
    return vector_store


def load_vector_store():
    embedding = HuggingFaceEndpointEmbeddings(
        model="sentence-transformers/all-mpnet-base-v2",
        task="feature-extraction",
        huggingfacehub_api_token=settings.HUGGING_API_KEY,
    )

    return Chroma(
        persist_directory="./chroma_db",
        collection_name="source-aware-rag",
        embedding_function=embedding
    )



def retrieve(query: str, vector_store: Chroma):
    return vector_store.as_retriever(search_kwargs={"k": 3})