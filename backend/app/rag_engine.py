# backend/app/rag_engine.py

from app.database import get_vector_connection


def fetch_relevant_chunks(query: str, top_k: int = 3):
    conn = get_vector_connection()
    cursor = conn.execute("SELECT content, source FROM documents ORDER BY content MATCH ? LIMIT ?", (query, top_k))
    chunks = []
    sources = []
    for row in cursor.fetchall():
        chunks.append(row[0])
        sources.append(row[1])
    return "\n---\n".join(chunks), "\n".join(sources)