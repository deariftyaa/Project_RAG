import os
from pathlib import Path
from pypdf import PdfReader
from dotenv import load_dotenv
from embeddings import get_embedding_model, get_vectorstore_collection

load_dotenv()

# Data directory (default: ./data)
DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))

# Chunking configuration
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))


def chunk_text(text, chunk_size, overlap):
    """
    Split text into overlapping chunks
    Returns: list[str]
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def process_pdfs():
    """
    Extract text from PDFs and convert into chunks with metadata
    Returns: list[dict]
    """
    all_chunks = []
    
    for pdf_path in DATA_DIR.glob("*.pdf"):
        print(f"extracting text from {pdf_path.name}...")
        try:
            reader = PdfReader(pdf_path)
            full_text = ""

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

            teks_dengan_sumber = f"--- SUMBER: {pdf_path.name} ---\n{full_text}"
            chunks = chunk_text(teks_dengan_sumber, CHUNK_SIZE, CHUNK_OVERLAP)

            for i, chunk in enumerate(chunks):
                all_chunks.append({
                    "id": f"{pdf_path.stem}_chunk_{i}",
                    "text": chunk,
                    "metadata": {"source": pdf_path.name}
                })

        except Exception as e:
            print(f"failed to process {pdf_path.name}: {e}")
            
    return all_chunks


def build_index():
    """
    Process PDFs, generate embeddings, and store in ChromaDB
    Returns: None
    """
    print("starting legal doc processing...")
    
    chunks_data = process_pdfs()
    
    if not chunks_data:
        print("no text extracted. make sure pdfs are in the data folder.")
        return

    print(f"created {len(chunks_data)} chunks total.")
    print("loading embedding model...")
    
    embedding_model = get_embedding_model()
    collection = get_vectorstore_collection()
    
    texts = [c["text"] for c in chunks_data]
    ids = [c["id"] for c in chunks_data]
    metadatas = [c["metadata"] for c in chunks_data]
    
    print("calculating vectors and saving to chromadb. this might take a while depending on pdf size...")
    embeddings = embedding_model.encode(texts, show_progress_bar=True).tolist()
    
    batch_size = 5000
    for i in range(0, len(texts), batch_size):
        print(f"saving batch {i} to {i + batch_size}...")
        collection.add(
            documents=texts[i:i + batch_size],
            embeddings=embeddings[i:i + batch_size],
            metadatas=metadatas[i:i + batch_size],
            ids=ids[i:i + batch_size]
        )
    
    print("done. legal docs are ready for querying.")


if __name__ == "__main__":
    build_index()
