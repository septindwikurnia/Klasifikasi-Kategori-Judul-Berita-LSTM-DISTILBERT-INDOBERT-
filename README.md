

# Klasifikasi Kategori Judul Berita Detik 📰

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Repository ini berisi sistem **klasifikasi kategori judul berita** dari website [detik.com](https://www.detik.com) menggunakan tiga model utama: **LSTM**, **DistilBERT**, dan **IndoBERT**. Dataset diperoleh melalui scrapping website Detik dengan lima kategori utama: Politik, Ekonomi, Olahraga, Selebritas, dan Teknologi.

---

## 🔹 Fitur Utama

* Klasifikasi judul berita menjadi **5 kategori**: Politik, Ekonomi, Olahraga, Selebritas, Teknologi
* Menggunakan tiga model:

  * **LSTM**
  * **DistilBERT** (tanpa file `.bin` karena ukuran model terlalu besar, bisa diunduh via [Google Drive] (https://drive.google.com/drive/folders/16djD5orNWm4Gc_V9fphpyHTJQRVMfv4u?usp=drive_link))
  * **IndoBERT** (tanpa file `.bin` karena ukuran model terlalu besar, bisa diunduh via [Google Drive] (https://drive.google.com/drive/folders/1Q2l9RfFoh0Ek0dgD0Takr-FeKqeYSrzm?usp=drive_link))
* Dataset sudah dibersihkan dan siap untuk training dan evaluasi
* Mendukung prediksi judul berita baru melalui **Jupyter Notebook** atau **Streamlit dashboard**

---

## 📂 Struktur Folder

```
Klasifikasi_Kategori_Berita/
│
├─ data/
│  ├─ raw/
│  │  └─ berita_detik_5_kategori.csv       # Dataset mentah hasil scrapping
│  └─ processed/
│     └─ berita_clean.csv                  # Dataset bersih
│
├─ models/
│  ├─ lstm/
│  │  ├─ model_lstm.h5
│  │  └─ label_encoder_lstm.pkl
│  │  └─ tokenizer_lstm.json
│  ├─ distilbert/
│  │  ├─ config.json
│  │  ├─ label_encoder.pkl
│  │  ├─ tokenizer_config.json
│  │  ├─ tokenizer.json
│  │  ├─ vocab.txt
│  │  └─ special_tokens_map.json
│  └─ indobert/
│     ├─ config.json
│     ├─ label_encoder.pkl
│     ├─ tokenizer_config.json
│     ├─ vocab.txt
│     └─ special_tokens_map.json
│
├─ notebooks/
│  ├─ 01_UAP_KLASIFIKASI_KATEGORI_JUDUL_BERITA.ipynb
│  └─ 02_UAP_DASHBOARD_BERITA.ipynb
│
└─ README.md
│
└─ app.py
```

---

## 🗂 Dataset

* **Sumber:** Scrapping dari detik.com menggunakan URL kategori berikut:

```python
kategori_urls = {
    "Politik": "https://www.detik.com/tag/politik",
    "Ekonomi": "https://www.detik.com/tag/ekonomi",
    "Olahraga": "https://www.detik.com/tag/olahraga",
    "Selebritas": "https://www.detik.com/tag/seleb",
    "Teknologi": "https://www.detik.com/tag/teknologi"
}
```

* **File penting:**

  * `berita_detik_5_kategori.csv` → dataset mentah
  * `berita_clean.csv` → dataset bersih (stopwords, case-folding, tokenisasi)

---

## 🛠 Model

| Model          | Deskripsi                                                           | Akurasi | Link Download                                                         |
| -------------- | ------------------------------------------------------------------- | ------- | --------------------------------------------------------------------- |
| **LSTM**       | Deep learning untuk text sequence menggunakan tokenizer khusus LSTM | 84%     | Termasuk di folder `models/lstm`                                      |
| **DistilBERT** | Pretrained transformer ringan untuk Bahasa Indonesia                | 90%     | [Download via Google Drive]   |
| **IndoBERT**   | Pretrained transformer besar untuk Bahasa Indonesia                 | 91%     | [Download via Google Drive]   |

> **Catatan:** File `.bin` untuk DistilBERT dan IndoBERT tidak diunggah karena ukuran sangat besar. Gunakan link di atas untuk mengunduh model.

---

## ⚡ Instalasi

1. Clone repository:

```bash
git clone https://github.com/septindwikurnia/Klasifikasi-Kategori-Judul-Berita-LSTM-DISTILBERT-INDOBERT-.git
cd Klasifikasi-Kategori-Judul-Berita-LSTM-DISTILBERT-INDOBERT-
```

2. Install dependencies (disarankan menggunakan virtual environment):

```bash
pip install -r requirements.txt
```

**Catatan:**

* TensorFlow ≥ 2.12 untuk LSTM
* Transformers ≥ 4.30 untuk DistilBERT dan IndoBERT

---

## 🧪 Penggunaan

### 1️⃣ Jupyter Notebook

* `01_UAP_KLASIFIKASI_KATEGORI_JUDUL_BERITA.ipynb` → Training, evaluasi, analisis performa model
* `02_UAP_DASHBOARD_BERITA.ipynb` → Demo prediksi kategori judul berita baru

---

### 📈 Hasil Evaluasi & Analisis Perbandingan Model

| Nama Model | Akurasi | Hasil Analisis                                                                                         |
| ---------- | ------- | -------------------------------------------------------------------------------------------------------|
| LSTM       | 84%     | Cepat training, ringan, tapi akurasi lebih rendah; kadang salah klasifikasi judul ambigu.              |
| DistilBERT | 90%     | Training lebih lama, menangkap konteks lebih baik; akurasi tinggi untuk judul dengan kata-kata ambigu. |
| IndoBERT   | 91%     | Training paling lama, akurasi tertinggi; mampu memahami konteks bahasa Indonesia secara menyeluruh.    |

---

Siap 👍
Berikut **tambahan keterangan khusus untuk `app.py`** yang **bisa langsung kamu tempel di README.md** (gaya bahasa konsisten & profesional, tanpa mengubah bagian lain).

---

## 🖥️ Streamlit Dashboard (`app.py`)

Selain melalui Jupyter Notebook, sistem ini juga menyediakan **dashboard interaktif berbasis Streamlit** untuk melakukan prediksi kategori judul berita secara langsung.

### 📌 Deskripsi `app.py`

File `app.py` merupakan aplikasi dashboard yang memungkinkan pengguna untuk:

* Memasukkan judul berita secara manual
* Memilih model klasifikasi:

  * **LSTM**
  * **DistilBERT**
  * **IndoBERT**
* Melihat hasil prediksi kategori berita secara real-time
* Menggunakan model yang sudah dilatih tanpa perlu retraining

---

### ▶️ Menjalankan Dashboard

Pastikan seluruh dependency telah terinstal dan model tersedia, kemudian jalankan perintah berikut dari root project:

```bash
streamlit run app.py
```

Setelah dijalankan, dashboard dapat diakses melalui browser pada alamat:

```
http://localhost:8501
```

## ⚠️ Catatan

* Dataset hasil scrapping harus digunakan sesuai ketentuan penggunaan detik.com
* Pastikan preprocessing yang sama diterapkan saat menambahkan data baru
* Folder `models` berisi model siap pakai (LSTM lengkap, DistilBERT & IndoBERT via Drive)

---
