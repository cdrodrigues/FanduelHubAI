import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def load_and_chunk_docs(docs_path, chunk_size=500):
    """Load markdown files from a folder and split them into chunks of given size."""
    chunks = []
    sources = []
    for fname in os.listdir(docs_path):
        if fname.endswith(".md"):
            with open(os.path.join(docs_path, fname), "r", encoding="utf-8") as f:
                text = f.read()
                for i in range(0, len(text), chunk_size):
                    chunk = text[i:i+chunk_size]
                    chunks.append(chunk)
                    sources.append(fname)
    return chunks, sources

def retrieve_relevant_chunks(query, doc_chunks, doc_embeddings, embedder, k=3):
    """Retrieve the top-k most relevant document chunks for a query."""
    query_emb = embedder.encode([query], convert_to_numpy=True)
    sims = cosine_similarity(query_emb, doc_embeddings)[0]
    top_idx = np.argsort(sims)[-k:][::-1]
    return [doc_chunks[i] for i in top_idx]
