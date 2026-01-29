from langchain_community.graphs import Neo4jGraph
from settings import settings

def get_graph():
    return Neo4jGraph(
        url=settings.NEO4J_URI,
        username=settings.NEO4J_USERNAME,
        password=settings.NEO4J_PASSWORD,
    )
