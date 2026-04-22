# 🤖 RAG Starter Pack — UTS Data Engineering

> **Retrieval-Augmented Generation** — Sistem Tanya-Jawab Cerdas Berbasis Dokumen

Starter pack ini adalah **kerangka awal** proyek RAG untuk UTS Data Engineering D4.

Tujuan dari project ini adalah untuk membantu seseorang dalam mengecek usaha yang ingin di jalankan, apakah usaha tersebut legal atau tidak.

---

## 👥 Identitas Kelompok

| Nama | NIM | Tugas Utama |
|------|-----|-------------|
| Dzakwan Daris Fakhruddin  | 244311011 |   Data Engineer    |
| Takeru Putra Nojima  | 244311029 |       Data Analysis  |
| Dea Riftya Ananda | 244311008|  Project Manager        |

**Topik Domain:** *Pengecekan Legalitas Pada Badan Usaha Berdasarkan Undang-Undang*  
**Stack yang Dipilih:** *From Scratch*  
**LLM yang Digunakan:** *Gemini, Llama*  
**Vector DB yang Digunakan:** *ChromaDB*

---

## 🗂️ Struktur Proyek

```
rag-uts-[kelompok 9]/
├── data/                    
   └── Salinan Perpres Nomor 10 Tahun 2021.pdf
   └── Lampiran I Salinan Perpres Nomor 10 Tahun 2021.pdf
   └── Lampiran II Salinan Perpres Nomor 10 Tahun 2021.pdf
   └── Lampiran III Salinan Perpres Nomor 10 Tahun 2021.pdf
   └── laporan-lkpm-non-umk-triwulan-i-2023.xlsx
   └── Permenkumham Nomor 17 Tahun 2018.pdf
   └── Perpres Nomor 10 Tahun 2021.pdf
   └── PP Nomor 5 Tahun 2021_penjelasan.pdf
   └── PP Nomor 5 Tahun 2021.pdf
   └── UU Nomor 6 Tahun 2023.pdf
   └── UU Nomor 40 Tahun 2007.pdf                
├── src/
│   ├── indexing.py         
│   ├── query.py            
│   ├── embeddings.py
├── ui/
│   └── app.py               # 🔧 WAJIB DIISI: Antarmuka Streamlit
├── docs/
│   └── arsitektur.png       # 📌 Diagram arsitektur
├── evaluation/
│   └── hasil_evaluasi.xlsx  # 📌 Tabel evaluasi 10 pertanyaan
├── notebooks/
│   └── 01_demo_rag.ipynb    # Notebook demo dari hands-on session
├── .env.example             # Template environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚡ Cara Memulai (Quickstart)

### 1. Clone & Setup

```bash
# Clone repository ini
git clone https://github.com/deariftyaa/Project_RAG.git
cd Project_RAG

# Buat virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau: venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Konfigurasi API Key

```bash
# Salin template env
cp .env.example .env

# Edit .env dan isi API key Anda
# JANGAN commit file .env ke GitHub!
```

### 3. Siapkan Dokumen

Letakkan dokumen sumber Anda di folder `data/`:
```bash
# Contoh: salin PDF atau TXT ke folder data
cp dokumen-saya.pdf data/
```

### 4. Jalankan Indexing (sekali saja)

```bash
python src/indexing.py
```

### 5. Jalankan Sistem RAG

```bash
# Dengan Streamlit UI
streamlit run ui/app.py

# Atau via CLI
python src/query.py
```

---

## 🔧 Konfigurasi

Semua konfigurasi utama ada di `src/config.py` (atau langsung di setiap file):

| Parameter | Default | Keterangan |
|-----------|---------|------------|
| `CHUNK_SIZE` | 500 | Ukuran setiap chunk teks (karakter) |
| `CHUNK_OVERLAP` | 50 | Overlap antar chunk |
| `TOP_K` | 3 | Jumlah dokumen relevan yang diambil |
| `MODEL_NAME` | *(isi)* | Nama model LLM yang digunakan |

---

## 📊 Hasil Evaluasi

*(Isi setelah pengujian selesai)*

| # | Pertanyaan | Jawaban Sistem | Jawaban Ideal | Skor (1-5) |
|---|-----------|----------------|---------------|-----------|
| 1 | Menanam sawit di pegunungan apakah legal? | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
**Rata-rata Skor:** ...  
**Analisis:** ...

---

## 🏗️ Arsitektur Sistem

*(Masukkan gambar diagram arsitektur di sini)*

```
[Dokumen] → [Loader] → [Splitter] → [Embedding] → [Vector DB]
                                                         ↕
[User Query] → [Query Embed] → [Retriever] → [Prompt] → [LLM] → [Jawaban]
```

---

## 📚 Referensi & Sumber

- Framework: *(LangChain docs / LlamaIndex docs)*
- LLM: *(Groq / Gemini / Ollama)*
- Vector DB: *(ChromaDB / FAISS docs)*
- Tutorial yang digunakan: *(cantumkan URL)*

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** *Kamis, 23 April 2026*
