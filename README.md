# Multi-Source RAG (Retrieval-Augmented Generation)

A small multi-source Retrieval-Augmented Generation (RAG) project that ingests documents, builds embeddings, stores vectors, and uses a Neo4j graph for entity-aware retrieval. The code demonstrates loaders, splitting, embedding, vector storage, graph ingestion, and querying helpers.

## Features

- Document loaders for PDF, CSV, text, and web sources
- Chunking via a recursive text splitter
- Embeddings via Hugging Face endpoint and Chroma vector store
- Neo4j graph ingestion for entity relationships
- Utilities for entity extraction and strict prompt construction

## Prerequisites

- Python 3.10+ recommended
- Neo4j instance accessible to the app
- Hugging Face API token (for Hugging Face embeddings)
- OpenAI (or other LLM) credentials if using the included LLM components

## Environment

Create a `.env` file at the project root (or set environment variables). The project expects the following variables:

- `OPENAI_API_KEY`
- `OPENAI_API_BASE_URL`
- `NEO4J_URI`
- `NEO4J_USERNAME`
- `NEO4J_PASSWORD`
- `HUGGING_API_KEY` (used by `embedding.py`)

Example `.env`:

```
OPENAI_API_KEY=sk-...
OPENAI_API_BASE_URL=https://api.openai.com/v1
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=yourpassword
HUGGING_API_KEY=hf_...
```

The `settings.py` module uses `pydantic` and will load `.env` automatically.

## Install

Create and activate a virtual environment, then install dependencies. If you have a `requirements.txt`, use:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

If you manage dependencies with `pyproject.toml` and Poetry, use your preferred tool.

## Quick Start

- Start the Streamlit UI (if present):

```bash
streamlit run streamlit.py
```

- Or use components programmatically. Example: load documents, split, embed, and query.

```python
from helper import document_loader
from splitter import splitter
from embedding import embed, retrieve

# 1) Load
docs = list(document_loader.load('path/to/file.pdf', 'application/pdf'))

# 2) Split
chunks = splitter(docs)

# 3) Embed and store
vector_store = embed(chunks)

# 4) Query
results = retrieve('your question', vector_store)
print(results)
```

To perform graph-based retrieval, see `graph_retriver.graph_search(question)` which extracts entities and queries Neo4j fulltext indexes.

## Important Files

- `helper.py` — Document loaders for PDF, CSV, text, and web sources.
- `splitter.py` — Uses a RecursiveCharacterTextSplitter to chunk documents.
- `embedding.py` — Creates Hugging Face embeddings and stores them in Chroma.
- `graph/client.py` — Neo4j `get_graph()` helper that reads credentials from `settings.py`.
- `graph/ingestion.py` — Converts documents into graph documents using LLMGraphTransformer and ingests into Neo4j.
- `graph_retriver.py` — Performs entity-based graph searches (uses entity extractor).
- `query_constructor.py` — Builds strict LLM prompts and supplies an `ENTITY_PROMPT` for entity extraction.
- `model.py` — Returns an LLM instance (reads keys from `settings.py`).

## Notes & Next Steps

- Ensure Neo4j fulltext indexes exist for the graph entity searches.
- The project uses multiple community LangChain components; verify package names and compatibility with your environment.
- Add a `requirements.txt` or pin dependencies in `pyproject.toml` for reproducible installs.

---

If you'd like, I can:

- Add a `requirements.txt` based on imports found in the codebase.
- Add example ingestion and query scripts (`scripts/ingest.py`, `scripts/query.py`).
- Commit README to git and create a branch.

Created by a code assistant from project files.
