import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import google.generativeai as genai

from embeddings import get_embedding_model, get_vectorstore_collection

load_dotenv()

TOP_K = int(os.getenv("TOP_K", 10))
GROQ_MODEL = os.getenv("GROQ_MODEL_NAME", "llama-3.1-8b-instant")
GEMINI_MODEL = os.getenv("GEMINI_MODEL_NAME", "gemini-3-flash-preview")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def retrieve_context(question: str, top_k: int = TOP_K) -> list:
    """
    Retrieve top-k relevant document chunks from vectorstore
    Returns: list[dict]
    """
    collection = get_vectorstore_collection()
    embedding_model = get_embedding_model()
    
    query_embedding = embedding_model.encode([question]).tolist()
    
    hasil_pencarian = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k,
        include=["documents", "distances", "metadatas"]
    )
    
    contexts = []
    if hasil_pencarian['documents'] and len(hasil_pencarian['documents']) > 0:
        docs = hasil_pencarian['documents'][0]
        dists = hasil_pencarian['distances'][0]
        metas = hasil_pencarian['metadatas'][0]
        
        for i in range(len(docs)):
            contexts.append({
                "content": docs[i],
                "source": metas[i].get("source", "Unknown PDF"),
                "score": float(dists[i])
            })
            
    return contexts


def build_prompt(question: str, contexts: list) -> str:
    """
    Build LLM prompt using retrieved contexts and user question
    Returns: str
    """
    context_text = "\n\n".join(
        [f"[Dokumen: {c['source']}]\n{c['content']}" for c in contexts]
    )

    prompt = f"""Anda adalah Konsultan Hukum (Legal Tech Assistant) khusus regulasi dan legalitas badan usaha di Indonesia.
Tugas Anda adalah menganalisis ide bisnis atau pertanyaan pengguna dan menentukan apakah ide tersebut legal, terikat oleh Daftar Positif Investasi (Perpres 10/2021), perlu perizinan risiko tinggi (PP 5/2021), atau terkait aturan Perseroan Terbatas/CV.

INSTRUKSI:
1. Jawab HANYA berdasarkan konteks hukum yang disediakan di bawah.
2. Jika dokumen tidak menyebutkan jawaban dari pertanyaan, katakan dengan jelas bahwa regulasi terkait tidak ditemukan dalam dokumen.
3. Selalu sebutkan dasar hukumnya (contoh: "Menurut UU Cipta Kerja No 6 Tahun 2023..." atau "Berdasarkan Lampiran III Perpres 10/2021...").

Konteks Dokumen Hukum:
{context_text}

Pertanyaan Klien: {question}"""
    return prompt


def get_answer_groq(prompt: str) -> str:
    """
    Generate answer using Groq model
    Returns: str
    """
    response = groq_client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=1024
    )
    return response.choices[0].message.content


def get_answer_gemini(prompt: str) -> str:
    """
    Generate answer using Gemini model
    Returns: str
    """
    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(prompt)
    return response.text


def answer_question(question: str, vectorstore, top_k, ai_choice="Groq") -> dict:
    """
    Run full RAG pipeline: retrieve, build prompt, generate answer
    Returns: dict
    """
    contexts = retrieve_context(question, top_k=top_k)
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
    print("legal tech assistant system ready")
    while True:
        q = input("\nask about legality (type 'exit' to quit): ")
        if q.lower() == "exit":
            break
        res = answer_question(q, None, TOP_K, ai_choice="Gemini")        print("\n=== legal analysis ===")
        print(res["answer"])
