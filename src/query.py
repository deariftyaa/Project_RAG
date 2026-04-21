import os
from pathlib import Path
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from groq import Groq
import google.generativeai as genai

load_dotenv()

TOP_K = int(os.getenv("TOP_K", 15))
VS_DIR = Path(os.getenv("VECTORSTORE_DIR", "./vectorstore"))

GROQ_MODEL = os.getenv("GROQ_MODEL_NAME", "llama-3.1-8b-instant")
GEMINI_MODEL = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-flash")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def load_vectorstore():
    if not VS_DIR.exists():
        raise FileNotFoundError(f"Vector store tidak ditemukan di {VS_DIR}")
    
    chroma_client = chromadb.PersistentClient(path=str(VS_DIR))
    collection = chroma_client.get_collection(name="koleksi_uts_rag")
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    return (collection, embedding_model)

def retrieve_context(vs_data, question: str, top_k: int = TOP_K) -> list:
    collection, embedding_model = vs_data
    query_embedding = embedding_model.encode([question]).tolist()
    
    hasil_pencarian = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "distances"]
    )
    
    contexts = []
    if hasil_pencarian['documents'] and len(hasil_pencarian['documents']) > 0:
        docs = hasil_pencarian['documents'][0]
        dists = hasil_pencarian['distances'][0]
        ids = hasil_pencarian['ids'][0]
        
        for i in range(len(docs)):
            contexts.append({
                "content": docs[i],
                "source": ids[i],
                "score": float(dists[i])
            })
            
    return contexts

def build_prompt(question: str, contexts: list) -> str:
    context_text = "\n\n".join([c['content'] for c in contexts])

    prompt = f"""Anda adalah analis data. Tugas Anda adalah menganalisis apakah ada hubungan antara rata-rata jam kerja mingguan dengan indeks kebahagiaan berdasarkan data pada konteks berikut.
Sebutkan beberapa contoh negara dari konteks beserta angka jam kerja dan skor kebahagiaannya untuk mendukung kesimpulan Anda.

HWUSUAL = Week Hour Usual
HWACTUAL = Week Hour Actual
HWOVERP = Week Hour Overtime
LV = Latvia

Konteks Dokumen:
{context_text}

Pertanyaan: {question}"""
    return prompt

def get_answer_groq(prompt: str) -> str:
    response = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1024
    )
    return response.choices[0].message.content

def get_answer_gemini(prompt: str) -> str:
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text

def answer_question(question: str, vectorstore=None, ai_choice="Groq") -> dict:
    if vectorstore is None:
        vectorstore = load_vectorstore()
    
    contexts = retrieve_context(vectorstore, question)
    prompt = build_prompt(question, contexts)
    
    if ai_choice == "Gemini":
        answer = get_answer_gemini(prompt)
    else:
        answer = get_answer_groq(prompt)
    
    return {
        "question": question,
        "answer": answer,
        "contexts": contexts,
        "prompt": prompt,
        "ai_used": ai_choice
    }

if __name__ == "__main__":
    vs = load_vectorstore()
    while True:
        q = input("\nTanya (ketik 'exit' untuk keluar): ")
        if q.lower() == "exit":
            break
        res = answer_question(q, vs, "Groq")
        print("\n=== HASIL ===")
        print(res["answer"])
