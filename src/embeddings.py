import os
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

VS_DIR = Path(os.getenv("VECTORSTORE_DIR", "./vectorstore"))

def get_embedding_model():
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def get_vectorstore_collection():
    VS_DIR.mkdir(parents=True, exist_ok=True)
    
    chroma_client = chromadb.PersistentClient(path=str(VS_DIR))
    collection = chroma_client.get_or_create_collection(name="legalitas_usaha_rag")
    return collection
