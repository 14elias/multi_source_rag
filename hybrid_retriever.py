from keyword_search import bm25_retriever as bm25

def hybrid_retrieve(query: str, docs, vectore_store):

    # build keyword retriever
    bm25_model = bm25(docs)

    # build semantic retriever
    vector_retriever = vectore_store.as_retriever(search_kwargs={"k": 3})

    # actually retrieve documents
    vect_docs = vector_retriever.invoke(query)
    keyword_docs = bm25_model.invoke(query)

    combined = vect_docs + keyword_docs

    # deduplicate
    seen = set()
    unique_docs = []
    for d in combined:
        if d.page_content not in seen:
            unique_docs.append(d)
            seen.add(d.page_content)

    return unique_docs
