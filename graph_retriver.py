from graph.client import get_graph
from entity_extraction import extract_entities
from langchain_community.vectorstores.neo4j_vector import remove_lucene_chars

def _lucene_query(text: str) -> str:
    words = remove_lucene_chars(text).split()
    return " AND ".join(f"{w}~2" for w in words)

def graph_search(question: str) -> str:
    graph = get_graph()
    entities = extract_entities(question)
    output = []

    for entity in entities:
        result = graph.query(
            """
            CALL db.index.fulltext.queryNodes('entity', $query, {limit:2})
            YIELD node
            MATCH (node)-[r]->(n)
            RETURN node.id + ' - ' + type(r) + ' -> ' + n.id AS text
            """,
            {"query": _lucene_query(entity)}
        )
        output.extend([r["text"] for r in result])

    return "\n".join(output)
