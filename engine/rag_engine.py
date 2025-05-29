import os
import numpy as np
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


load_dotenv()

EMBEDDING = os.getenv("EMBEDDING_MODEL") 

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"

nomic_model = SentenceTransformer(EMBEDDING, trust_remote_code=True)

def load_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    return text

def chunk_text(text, max_chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i + max_chunk_size]) for i in range(0, len(words), max_chunk_size)]

def embed_chunks_nomic(chunks):
    embeddings = nomic_model.encode(chunks)
    return np.array(embeddings)

def retrieve_similar_chunks(query, chunks, chunk_embeddings, top_k=3):
    query_embedding = nomic_model.encode([query])
    similarities = cosine_similarity(query_embedding, chunk_embeddings)[0]
    top_indices = similarities.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]
