def create_entity_index(graph):
    graph.query("""
    CREATE FULLTEXT INDEX entity IF NOT EXISTS
    FOR (e:__Entity__) ON EACH [e.id]
    """)