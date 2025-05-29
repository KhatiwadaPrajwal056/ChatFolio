# engine/rag_engine.py
import os
import numpy as np
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sys # Import sys for printing to stderr, often visible in logs

load_dotenv()

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
# Add print statement here
print(f"DEBUG: EMBEDDING_MODEL environment variable is set to: {EMBEDDING_MODEL}", file=sys.stderr)


os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

# Load Nomic model locally
# Consider adding a try-except block around model loading for better error handling
try:
    nomic_model = SentenceTransformer(EMBEDDING_MODEL, trust_remote_code=True)
    print("DEBUG: SentenceTransformer model loaded successfully.", file=sys.stderr)
except Exception as e:
    print(f"ERROR: Failed to load SentenceTransformer model: {e}", file=sys.stderr)
    # Depending on how you want to handle this, you might re-raise the exception
    # or set nomic_model to None and handle it downstream.
    raise # Re-raise the exception to see the full traceback in logs


def load_pdf_text(file_path):\n    # ... existing code ...

def chunk_text(text, max_chunk_size=500):\n    # ... existing code ...

def embed_chunks_nomic(chunks):
    # Add print statement here
    print(f"DEBUG: Starting embedding for {len(chunks)} chunks.", file=sys.stderr)
    if nomic_model is None:
            print("ERROR: nomic_model is None, cannot encode.", file=sys.stderr)
            raise ValueError("Embedding model not loaded.")

    embeddings = nomic_model.encode(chunks)
    print("DEBUG: Embedding completed successfully.", file=sys.stderr)
    return np.array(embeddings)


def retrieve_similar_chunks(query, chunks, chunk_embeddings, top_k=3):
    query_embedding = nomic_model.encode([query])
    # Compute cosine similarities between query and all chunk embeddings
    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
    # Get indices of top_k most similar chunks
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]
