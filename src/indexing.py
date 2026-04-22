import os
from pathlib import Path
import pandas as pd
import chromadb
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = Path(os.getenv("DATA_DIR", "./data"))
VS_DIR = Path(os.getenv("VECTORSTORE_DIR", "./vectorstore"))

def preprocess_tabular_to_text(df, tipe_data):
    text = ""
    for index, row in df.iterrows():
        if tipe_data == "jam_kerja":
            text += f"Berdasarkan data Eurostat 2024, negara dengan kode {row['Country_Code']} memiliki rata-rata jam kerja mingguan aktual sebesar {row['Weekly_Hours']} jam.\n"
        elif tipe_data == "kebahagiaan":
            text += f"Berdasarkan World Happinesspip Report 2024, negara {row['Country_Name']} memiliki skor indeks kebahagiaan sebesar {row['Happiness_Score']}.\n"
    return text

def chunk_text(text, chunk_size=400, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def process_and_chunk_csv(file_path, rows_per_chunk=5):
    try:
        df = pd.read_csv(file_path)
        chunks = []
        current_chunk_text = ""
        for index, row in df.iterrows():
            row_text = ", ".join([f"{col}: {val}" for col, val in row.items()])
            current_chunk_text += f"Baris {index + 1} - {row_text}\n"
            if (index + 1) % rows_per_chunk == 0:
                chunks.append(current_chunk_text)
                current_chunk_text = ""
        if current_chunk_text.strip() != "":
            chunks.append(current_chunk_text)
        return chunks
    except Exception as e:
        print(f"Error membaca {file_path}: {e}")
        return []

def build_index():
    df_hours = pd.read_excel(DATA_DIR / 'DATA-2024-UPDATE-2025-SE-ACTUAL-AND-USUAL-HOURS-OF-WORK.xlsx', sheet_name='Map 1', skiprows=9, nrows=32)
    df_hours = df_hours[['GEO', 'VALUES']]
    df_hours.columns = ['Country_Code', 'Weekly_Hours']

    df_whr = pd.read_excel(DATA_DIR / 'WHR24_Data_Figure_2.1.xls')
    df_whr = df_whr[['Country name', 'Ladder score']]
    df_whr.columns = ['Country_Name', 'Happiness_Score']

    teks_jam_kerja = preprocess_tabular_to_text(df_hours, "jam_kerja")
    teks_kebahagiaan = preprocess_tabular_to_text(df_whr, "kebahagiaan")
    gabungan_text = "--- DOKUMEN 1: DATA JAM KERJA EROPA ---\n" + teks_jam_kerja + "\n\n--- DOKUMEN 2: DATA INDEKS KEBAHAGIAAN (WHR) ---\n" + teks_kebahagiaan

    chunk_size = int(os.getenv("CHUNK_SIZE", 400))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 100))
    dokumen_chunks = chunk_text(gabungan_text, chunk_size=chunk_size, overlap=chunk_overlap)

    file_list = [
        'FI_LFS_2013_y.csv',
        'FI_LFS_2013_q4.csv',
        'FI_LFS_2013_q3.csv',
        'FI_LFS_2013_q2.csv',
        'FI_LFS_2013_q1.csv',
        'FI_LFS_2013_hh.csv'
    ]

    semua_dokumen_chunks = list(dokumen_chunks)
    for file in file_list:
        file_path = DATA_DIR / file
        if file_path.exists():
            hasil_chunk = process_and_chunk_csv(file_path, rows_per_chunk=10)
            semua_dokumen_chunks.extend(hasil_chunk)

    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    chroma_client = chromadb.PersistentClient(path=str(VS_DIR))
    collection = chroma_client.get_or_create_collection(name="koleksi_uts_rag")

    embeddings = embedding_model.encode(semua_dokumen_chunks).tolist()
    chunk_ids = [f"chunk_{i}" for i in range(len(semua_dokumen_chunks))]

    collection.add(
        documents=semua_dokumen_chunks,
        embeddings=embeddings,
        ids=chunk_ids
    )
    
    print(f"Berhasil! {len(semua_dokumen_chunks)} chunks disimpan ke {VS_DIR}")

if __name__ == "__main__":
    build_index()
#
#     # Load dokumen
#     documents = []
#     for file_path in DATA_DIR.glob("**/*.txt"):
#         with open(file_path, "r", encoding="utf-8") as f:
#             content = f.read()
#             documents.append({"source": str(file_path), "content": content})
#     print(f" {len(documents)} dokumen dimuat")
#
#     # Chunking manual
#     chunks = []
#     for doc in documents:
#         text = doc["content"]
#         for i in range(0, len(text), CHUNK_SIZE - CHUNK_OVERLAP):
#             chunk_text = text[i:i + CHUNK_SIZE]
#             if len(chunk_text) > 50:
#                 chunks.append({"source": doc["source"], "text": chunk_text, "id": len(chunks)})
#     print(f" {len(chunks)} chunk dibuat")
#
#     # Embedding
#     model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
#     texts = [c["text"] for c in chunks]
#     embeddings = model.encode(texts, show_progress_bar=True)
#     print(f" Embedding selesai, dimensi: {embeddings.shape}")
#
#     # Simpan ke FAISS
#     VS_DIR.mkdir(parents=True, exist_ok=True)
#     index = faiss.IndexFlatL2(embeddings.shape[1])
#     index.add(embeddings.astype("float32"))
#     faiss.write_index(index, str(VS_DIR / "index.faiss"))
#
#     # Simpan metadata
#     with open(VS_DIR / "chunks.json", "w", encoding="utf-8") as f:
#         json.dump(chunks, f, ensure_ascii=False, indent=2)
#
#     print(f" Index FAISS tersimpan di {VS_DIR}")


# ─── MAIN ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # TODO: Ganti sesuai implementasi yang kalian pilih
    build_index_langchain()
    
    # Atau jika from scratch:
    # build_index_scratch()
