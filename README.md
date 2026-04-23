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
│   └── Arsitektur.png       # 📌 Diagram arsitektur
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
| 1 | Menanam sawit di pegunungan apakah legal? | Berdasarkan konteks dokumen hukum yang disediakan, saya tidak menemukan aturan yang secara spesifik melarang menanam sawit di pegunungan. Namun, perlu diingat bahwa menanam sawit di Kawasan Hutan tanpa Perizinan Berusaha dari Pemerintah Pusat dapat dianggap sebagai kegiatan yang melanggar aturan. <br>Menurut Pasal 5 UU Nomor 6 Tahun 2023, Pemanfaatan Hutan Produksi sebagaimana dimaksud pada ayat (1) dilakukan dengan pemberian Perizinan Berusaha dari Pemerintah Pusat. Namun, tidak ada aturan yang secara spesifik melarang menanam sawit di pegunungan. <br>Oleh karena itu, saya sarankan klien untuk meminta Perizinan Berusaha dari Pemerintah Pusat sebelum melakukan kegiatan menanam sawit di pegunungan. Jika klien tidak memiliki Perizinan Berusaha, maka kegiatan tersebut dapat dianggap sebagai kegiatan yang melanggar aturan. Dasar hukum: UU Nomor 6 Tahun 2023, Pasal 5.  | ... | ... |
| 2 | Sebuah toko sudah memiliki izin usaha dan NPWP, namun beroperasi melebihi jam operasional yang diizinkan oleh peraturan daerah. Apakah hal ini termasuk pelanggaran hukum? Jelaskan. | Berdasarkan konteks hukum yang disediakan, saya dapat menganalisis pertanyaan klien Anda sebagai berikut: Menurut Pasal 4 UU Nomor 6 Tahun 2023, Perusahaan Penanaman Modal yang akan melakukan kegiatan usaha wajib memenuhi Perizinan Berusaha dari Pemerintah Pusat atau Pemerintah Daerah. Namun, tidak ada ketentuan yang spesifik tentang jam operasional yang diizinkan oleh peraturan daerah. <br>Namun, berdasarkan Pasal 405 PP Nomor 5 Tahun 2021, Setiap Pelaku Usaha di sektor perindustrian yang tidak memiliki Perizinan Berusaha akan dianggap melanggar hukum. Meskipun toko Anda sudah memiliki izin usaha, namun beroperasi melebihi jam operasional yang diizinkan oleh peraturan daerah dapat dianggap sebagai pelanggaran hukum. <br>Dalam hal ini, saya sarankan untuk memeriksa peraturan daerah yang berlaku dan memastikan bahwa toko Anda tidak melanggar ketentuan yang berlaku. Jika ditemukan pelanggaran, maka toko Anda harus mengambil tindakan untuk memenuhi ketentuan yang berlaku. <br>Dalam beberapa kasus, pelanggaran hukum dapat diatasi dengan cara mengajukan permohonan perubahan izin usaha atau meminta pengecualian dari pemerintah daerah. Namun, hal ini harus dilakukan dengan hati-hati dan memastikan bahwa toko Anda memenuhi semua ketentuan yang berlaku. <br>Dalam keseluruhan, saya menyarankan untuk memeriksa peraturan daerah yang berlaku dan mengambil tindakan yang tepat untuk memenuhi ketentuan yang berlaku. | ... | ... |
| 3 | saya ingin jual rokok tanpa dikasi beacukai apakah legal? | Berdasarkan konteks dokumen hukum yang disediakan, saya tidak menemukan informasi yang spesifik tentang penjualan rokok. Namun, berdasarkan Perpres 10/2021, saya dapat mencari informasi tentang impor tembakau. <br>Menurut Lampiran III Perpres 10/2021, impor tembakau harus memenuhi standar pelaksanaan kegiatan usaha. Jika usaha Anda melakukan impor tembakau tetapi tidak memenuhi standar tersebut, maka Anda dapat dikenai sanksi administratif berupa pencabutan Perizinan Berusaha sebagaimana dimaksud dalam Pasal 330 huruf c. <br>Namun, saya tidak menemukan informasi tentang penjualan rokok tanpa bea cukai. Oleh karena itu, saya tidak dapat memberikan jawaban yang pasti tentang apakah penjualan rokok tanpa bea cukai legal atau tidak. <br>Saya sarankan Anda untuk memeriksa regulasi terkait impor dan penjualan rokok secara lebih lanjut, serta menghubungi instansi terkait untuk memastikan bahwa usaha Anda memenuhi semua persyaratan hukum yang berlaku. | ... | ... |
| 4 | saya mau bikin usaha toko obat ganja untuk medis apakah legal? | Mohon maaf, namun saya tidak menemukan informasi yang relevan tentang toko obat ganja untuk medis dalam dokumen yang disediakan. Namun, saya dapat memberikan jawaban berdasarkan konteks hukum yang ada. <br>Dalam Pasal 39 ayat (1) UU Nomor 6 Tahun 2023, disebutkan bahwa Narkotika hanya dapat disalurkan oleh Industri Farmasi, Pedagang Besar Farmasi, dan sarana penyimpanan sediaan farmasi pemerintah sesuai dengan ketentuan dalam Undang-Undang ini. <br>Namun, dalam Pasal 36 UU Nomor 6 Tahun 2023, disebutkan bahwa Narkotika dalam bentuk obat jadi hanya dapat diedarkan setelah memenuhi Perizinan Berusaha dari Pemerintah. Tidak ada informasi tentang toko obat ganja untuk medis dalam dokumen tersebut. <br>Dalam konteks hukum yang ada, saya tidak dapat menentukan apakah usaha toko obat ganja untuk medis legal atau tidak. Namun, saya dapat merekomendasikan klien untuk memeriksa peraturan perundang-undangan yang lebih spesifik tentang penjualan obat-obatan, serta meminta saran dari ahli hukum yang berpengalaman dalam bidang ini. <br>Dalam beberapa kasus, penjualan obat-obatan dapat diatur oleh peraturan perundang-undangan yang lebih spesifik, seperti Peraturan Pemerintah atau Peraturan Menteri Kesehatan. Oleh karena itu, saya sarankan klien untuk memeriksa peraturan perundang-undangan yang lebih spesifik dan meminta saran dari ahli hukum yang berpengalaman dalam bidang ini. | ... | ... |
| 5 | Sebuah toko didirikan tanpa izin usaha dan tanpa NPWP. Apakah toko tersebut melanggar hukum? | Berdasarkan konteks dokumen hukum yang disediakan, saya dapat menganalisis pertanyaan klien Anda sebagai berikut: <br>Menurut Pasal 110B Ayat (1) UU Nomor 6 Tahun 2023, yang dimaksud dengan "tanpa memiliki Perizinan Berusaha" adalah setiap orang yang melakukan kegiatan usaha tanpa memiliki izin usaha yang diterbitkan oleh pejabat yang berwenang. Dalam kasus toko yang didirikan tanpa izin usaha, maka toko tersebut dapat dianggap sebagai pelaku usaha yang tidak memiliki Perizinan Berusaha. <br>Selain itu, Pasal 405 Ayat (1) PP Nomor 5 Tahun 2021 juga menyebutkan bahwa setiap Pelaku Usaha di sektor perindustrian yang tidak memiliki Perizinan Berusaha akan dikenakan sanksi. Namun, perlu diingat bahwa PP Nomor 5 Tahun 2021 tidak secara spesifik menyebutkan tentang toko atau kegiatan usaha yang tidak memiliki izin usaha. <br>Dalam hal ini, saya tidak menemukan regulasi yang secara spesifik menyebutkan tentang sanksi bagi toko yang didirikan tanpa izin usaha. Namun, berdasarkan Pasal 110B Ayat (1) UU Nomor 6 Tahun 2023 dan Pasal 405 Ayat (1) PP Nomor 5 Tahun 2021, toko tersebut dapat dianggap sebagai pelaku usaha yang tidak memiliki Perizinan Berusaha dan mungkin akan dikenakan sanksi. <br>Dalam prakteknya, toko tersebut juga tidak memiliki NPWP, yang merupakan syarat wajib bagi pelaku usaha yang melakukan kegiatan usaha di Indonesia. Dalam hal ini, toko tersebut juga melanggar hukum karena tidak memiliki NPWP. <br>Dalam kesimpulan, toko tersebut melanggar hukum karena tidak memiliki izin usaha dan tidak memiliki NPWP. | ... | ... |
| 6 | Menurut peraturan tentang perizinan usaha, apakah wajib memiliki NIB (Nomor Induk Berusaha) untuk membuka toko kecil? | Berdasarkan dokumen yang disediakan, untuk kegiatan usaha Risiko rendah, Pelaku Usaha hanya dipersyaratkan memiliki NIB. Karena toko kecil biasanya dianggap memiliki risiko rendah, maka menurut Peraturan Pemerintah Nomor 5 Tahun 2021, wajib memiliki NIB untuk membuka toko kecil. <br>Dasar hukumnya adalah Peraturan Pemerintah Nomor 5 Tahun 2021, Pasal (6) yang menyebutkan bahwa NIB merupakan Perizinan Berusaha bagi Pelaku Usaha untuk melakukan kegiatan operasional dan/atau komersial kegiatan usaha. | ... | ... |
| 7 | Apa risiko hukum yang dapat terjadi jika sebuah toko beroperasi tanpa izin resmi? | Berdasarkan konteks dokumen hukum yang disediakan, saya dapat menganalisis risiko hukum yang dapat terjadi jika sebuah toko beroperasi tanpa izin resmi. <br>Menurut PP Nomor 5 Tahun 2021, perusahaan perkebunan yang melakukan kegiatan usaha tanpa memiliki Perizinan Berusaha yang ditetapkan berdasarkan hasil analisis Risiko kegiatan usaha dan/atau Perizinan Berusaha Untuk Menunjang Kegiatan Usaha dikenai sanksi administratif berupa: <br>a. penghentian sementara kegiatan; <br>b. pengenaan denda administratif; dan/atau <br>c. paksaan Pem. <br>Namun, dokumen tidak menyebutkan secara spesifik tentang risiko hukum untuk toko yang beroperasi tanpa izin resmi. Oleh karena itu, saya tidak dapat menentukan dengan pasti risiko hukum yang dapat terjadi. <br>Namun, berdasarkan UU Nomor 6 Tahun 2023, Pasal 110B Ayat (1), yang dimaksud dengan "tanpa memiliki Perizinan Berusaha" adalah setiap orang yang melakukan kegiatan usaha tanpa memiliki izin lokasi dan/atau izin usaha di bidang perkebunan yang diterbitkan oleh pejabat yang berwenang. <br>Dengan demikian, saya dapat menyimpulkan bahwa toko yang beroperasi tanpa izin resmi dapat dikenai sanksi administratif, tetapi jenis sanksi yang dapat dikenakan tidak dapat ditentukan dengan pasti berdasarkan dokumen yang disediakan. <br>Regulasi terkait tidak ditemukan dalam dokumen. | ... | ... |
| 8 | Jika sebuah toko belum memiliki izin usaha lengkap, langkah apa yang harus dilakukan agar menjadi legal? | Berdasarkan konteks dokumen hukum yang disediakan, saya dapat memberikan jawaban sebagai berikut: <br> Menurut Pasal 110B UU Nomor 6 Tahun 2023, yang dimaksud dengan "tanpa memiliki Perizinan Berusaha" adalah setiap orang yang melakukan kegiatan usaha tanpa izin usaha yang diterbitkan oleh pejabat yang berwenang. Oleh karena itu, toko yang belum memiliki izin usaha lengkap harus melakukan langkah-langkah berikut untuk menjadi legal: <br> 1.Membuat permohonan izin usaha kepada pejabat yang berwenang. <br>2.Mengumpulkan dokumen-dokumen yang diperlukan untuk mendapatkan izin usaha, seperti dokumen identitas, dokumen keuangan, dan lain-lain. <br>3.Menunggu proses pengajuan izin usaha dan memenuhi syarat-syarat yang ditetapkan oleh pejabat yang berwenang. <br>4.Setelah izin usaha diterbitkan, toko harus memenuhi kewajiban-kewajiban yang terkait dengan izin usaha tersebut. <br>Dasar hukumnya adalah Pasal 110B UU Nomor 6 Tahun 2023. | ... | ... |
| 9 | Sebuah toko memiliki NIB dan NPWP, tetapi tidak memiliki izin lingkungan dan IMB. Apakah toko tersebut sudah dapat dikatakan legal? Jelaskan secara rinci. | Berdasarkan konteks dokumen hukum yang disediakan, saya akan menganalisis keadaan toko tersebut. <br> Dari dokumen PP Nomor 5 Tahun 2021, kita tahu bahwa untuk kegiatan usaha Risiko menengah rendah, Pelaku Usaha hanya dipersyaratkan memiliki NIB dan pernyataan pemenuhan Sertifikat Standar. Namun, tidak ada informasi tentang persyaratan izin lingkungan dan IMB. <br> Namun, dari dokumen PP Nomor 5 Tahun 2021, kita juga tahu bahwa untuk kegiatan usaha Risiko tinggi, Pelaku Usaha wajib memiliki NIB yang diterbitkan melalui Sistem OSS dan Izin yang telah diverifikasi. Meskipun toko tersebut memiliki NIB, namun tidak memiliki Izin yang telah diverifikasi, sehingga toko tersebut tidak memenuhi persyaratan untuk kegiatan usaha Risiko tinggi. <br> Dari dokumen UU Nomor 6 Tahun 2023, kita tahu bahwa setiap orang yang melakukan kegiatan usaha tanpa memiliki Perizinan Berusaha (izin usaha) dianggap tidak legal. Namun, dokumen ini tidak menyebutkan tentang persyaratan izin lingkungan dan IMB. <br> Dari analisis di atas, saya dapat menyimpulkan bahwa toko tersebut belum dapat dikatakan legal karena tidak memiliki Izin yang telah diverifikasi, meskipun memiliki NIB dan NPWP. Selain itu, toko tersebut juga tidak memiliki izin lingkungan dan IMB, yang mungkin merupakan persyaratan lain untuk kegiatan usaha. <br> Dalam konteks hukum, toko tersebut dapat dikategorikan sebagai "tanpa memiliki Perizinan Berusaha" menurut Pasal 110B UU Nomor 6 Tahun 2023. Oleh karena itu, toko tersebut perlu melakukan proses perizinan dan memenuhi persyaratan lainnya untuk menjadi legal. | ... | ... |
| 10 | Apakah saya boleh mendirikan toko di zona industri atau zona tertentu di Indonesia, dan aturan hukum apa yang mengaturnya? | Berdasarkan konteks dokumen hukum yang disediakan, saya tidak menemukan pasal atau ayat yang secara spesifik mengatur tentang mendirikan toko di zona tertentu. Namun, saya dapat memberikan analisis berdasarkan pasal yang terkait. <br>Pasal 72 PP Nomor 5 Tahun 2021 menyebutkan bahwa perizinan berusaha untuk kegiatan usaha kawasan industri hanya diberikan kepada Pelaku Usaha nonperseorangan, badan usaha milik negara, badan usaha milik daerah, koperasi, dan perusahaan terbatas yang berlokasi di dalam kawasan peruntukan industri. <br> Pasal 65 PP Nomor 5 Tahun 2021 menyebutkan bahwa perizinan berusaha untuk kegiatan usaha industri diperuntukan untuk kegiatan usaha industri yang wajib dilakukan di lokasi kawasan industri. Namun, ada beberapa pengecualian, seperti industri yang berdampak luas, industri yang menggunakan bahan baku khusus, dan/atau proses produksinya memerlukan lokasi khusus. <br> Dari analisis di atas, saya tidak dapat menemukan dasar hukum yang secara spesifik mengatur tentang mendirikan toko di zona tertentu. Namun, jika klien ingin mendirikan toko di zona industri, maka perlu memenuhi syarat-syarat yang ditetapkan dalam Pasal 72 dan Pasal 65 PP Nomor 5 Tahun 2021. <br> Jika klien ingin mendirikan toko di zona lain, seperti perumahan atau pendidikan, maka perlu memeriksa regulasi yang terkait dengan zona tersebut. Namun, saya tidak dapat memberikan jawaban yang spesifik karena tidak ada informasi yang cukup tentang zona tersebut. <br>Dalam kasus ini, saya sarankan klien untuk memeriksa regulasi yang terkait dengan zona yang diinginkan dan untuk berkonsultasi dengan ahli hukum yang berpengalaman dalam bidang regulasi bisnis. | ... | ... |
**Rata-rata Skor:** ...  
**Analisis:** ...

---

## 🏗️ Arsitektur Sistem

*![Diagram Arsitektur](./docs/Arsitektur.png)*

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
- Tutorial yang digunakan: *(https://medium.com/@nermeen.abdelaziz/build-your-first-python-rag-using-chromadb-openai-d711db1abf66)*

---

## 👨‍🏫 Informasi UTS

- **Mata Kuliah:** Data Engineering
- **Program Studi:** D4 Teknologi Rekayasa Perangkat Lunak
- **Deadline:** *Kamis, 23 April 2026*
