from langchain_experimental.graph_transformers import LLMGraphTransformer
from model import get_llm
from graph.client import get_graph

def ingest_graph(documents):
    graph = get_graph()
    transformer = LLMGraphTransformer(llm=get_llm())
    graph_docs = transformer.convert_to_graph_documents(documents)

    graph.add_graph_documents(
        graph_docs,
        baseEntityLabel=True,
        include_source=True
    )