# Klasifikasi Kategori Judul Berita Detik

Repository ini berisi implementasi sistem **klasifikasi kategori judul berita** dari website [detik.com](https://www.detik.com) menggunakan tiga model utama: **LSTM**, **DistilBERT**, dan **IndoBERT**. Dataset diperoleh melalui scrapping website Detik dengan lima kategori utama: Politik, Ekonomi, Olahraga, Selebritas, dan Teknologi.

---

## 🔹 Fitur Utama

* Klasifikasi judul berita menjadi **5 kategori**:

  * Politik
  * Ekonomi
  * Olahraga
  * Selebritas
  * Teknologi
* Menggunakan tiga model:

  * **LSTM**
  * **DistilBERT** (tanpa file `.bin` karena ukuran model terlalu besar)
  * **IndoBERT** (tanpa file `.bin` karena ukuran model terlalu besar)
* Dataset sudah dibersihkan dan siap untuk training dan evaluasi
* Mendukung prediksi judul berita baru melalui Jupyter Notebook atau Streamlit

---

## 📂 Struktur Folder

```
Klasifikasi_Kategori_Berita/
│
├─ data/
│  ├─ raw/
│  │  └─ berita_detik_5_kategori.csv       # Dataset mentah hasil scrapping
│  └─ processed/
│     └─ berita_clean.csv                  # Dataset sudah dibersihkan
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
  * `berita_clean.csv` → dataset sudah dibersihkan (stopwords, case-folding, tokenisasi)

---

## 🛠 Model

| Model          | Deskripsi                                                                | Akurasi |
| -------------- | ------------------------------------------------------------------------ | ------- |
| **LSTM**       | Deep learning untuk text sequence menggunakan tokenizer khusus LSTM      | 84%     |
| **DistilBERT** | Pretrained transformer ringan untuk Bahasa Indonesia (tanpa file `.bin`) | 90%     |
| **IndoBERT**   | Pretrained transformer besar untuk Bahasa Indonesia (tanpa file `.bin`)  | 91%     |

> **Catatan:** File `.bin` untuk DistilBERT dan IndoBERT tidak diunggah karena ukuran model sangat besar. Model dapat diunduh langsung dari Hugging Face jika diperlukan.

---

## ⚡ Instalasi

1. Clone repository:

```bash
git clone https://github.com/username/Klasifikasi_Kategori_Berita.git
cd Klasifikasi_Kategori_Berita
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

### Prediksi dan Training di Jupyter Notebook

* `01_UAP_KLASIFIKASI_KATEGORI_JUDUL_BERITA.ipynb` → Training, evaluasi, dan analisis performa model
* `02_UAP_DASHBOARD_BERITA.ipynb` → Demo prediksi kategori judul berita baru

### Prediksi melalui Streamlit

```bash
streamlit run app.py
```

* Upload file `.txt` berisi judul berita
* Pilih model: LSTM, DistilBERT, atau IndoBERT
* Lihat prediksi kategori secara real-time

---

## 📈 Evaluasi Model

* **LSTM:** 84%
* **DistilBERT:** 90%
* **IndoBERT:** 91%

> Akurasi dapat bervariasi tergantung preprocessing, tokenisasi, dan jumlah data.

---

## 📝 Referensi

1. Hugging Face Transformers: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
2. TensorFlow Documentation: [https://www.tensorflow.org/](https://www.tensorflow.org/)
3. Scikit-learn Documentation: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)

---

## ⚠️ Catatan

* Dataset hasil scrapping harus digunakan sesuai ketentuan penggunaan detik.com
* Pastikan preprocessing yang sama diterapkan saat menambahkan data baru
* Folder `models` berisi model siap pakai (LSTM lengkap, DistilBERT & IndoBERT tanpa `.bin`)



Apakah mau aku buat versi itu juga?
