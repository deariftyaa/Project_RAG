import os
from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

# Vector store directory (default: ./vectorstore)
VS_DIR = Path(os.getenv("VECTORSTORE_DIR", "./vectorstore"))


def get_embedding_model():
    """
    Load multilingual sentence embedding model
    Returns: SentenceTransformer
    """
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')


def get_vectorstore_collection():
    """
    Initialize or load persistent ChromaDB collection
    Returns: chromadb.Collection
    """
    VS_DIR.mkdir(parents=True, exist_ok=True)
    chroma_client = chromadb.PersistentClient(path=str(VS_DIR))
    return chroma_client.get_or_create_collection(name="legalitas_usaha_rag")
