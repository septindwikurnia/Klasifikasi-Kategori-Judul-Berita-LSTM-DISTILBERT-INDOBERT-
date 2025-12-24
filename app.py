import streamlit as st
import numpy as np
import joblib
import torch
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# ===================== BASE PATH =====================
BASE_PATH = "/content/drive/MyDrive/Klasifikasi_Kategori_Judul_Berita/models"

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Dashboard Klasifikasi Judul Berita",
    layout="wide"
)

st.title("📰 Dashboard Klasifikasi Kategori Judul Berita")
st.caption("Prediksi kategori judul berita menggunakan model Deep Learning & Transformer")

# ===================== LOAD MODELS =====================
@st.cache_resource
def load_lstm():
    tf.keras.backend.clear_session()
    model = load_model(f"{BASE_PATH}/lstm/model_lstm.h5", compile=False)
    model.compile(optimizer="adam", loss="categorical_crossentropy")
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(
        open(f"{BASE_PATH}/lstm/tokenizer_lstm.json").read()
    )
    label_encoder = joblib.load(f"{BASE_PATH}/lstm/label_encoder_lstm.pkl")
    return model, tokenizer, label_encoder

@st.cache_resource
def load_transformer(name):
    path = f"{BASE_PATH}/{name}"
    tokenizer = AutoTokenizer.from_pretrained(path)
    model = AutoModelForSequenceClassification.from_pretrained(path)
    label_encoder = joblib.load(f"{path}/label_encoder.pkl")
    return tokenizer, model, label_encoder

lstm_model, lstm_tokenizer, lstm_le = load_lstm()
distil_tok, distil_model, distil_le = load_transformer("distilbert")
indo_tok, indo_model, indo_le = load_transformer("indobert")

# ===================== SIDEBAR (KANAN) =====================
with st.sidebar:
    st.header("⚙️ Model Klasifikasi")

    model_choice = st.radio(
        "Pilih Model",
        ["LSTM", "DistilBERT", "IndoBERT"]
    )

    st.markdown("---")
    st.subheader("📊 Ringkasan Model")

    model_info = {
        "LSTM": ("84%", "Cepat & ringan"),
        "DistilBERT": ("90%", "Konteks lebih baik"),
        "IndoBERT": ("91%", "Akurasi tertinggi")
    }

    acc, desc = model_info[model_choice]
    st.metric("Akurasi Model", acc)
    st.caption(desc)

# ===================== MAIN AREA =====================
st.subheader("✍️ Masukkan Judul Berita")
text_input = st.text_area("Judul Berita", height=120)

if st.button("🔍 Prediksi Kategori"):
    if text_input.strip() == "":
        st.warning("Teks tidak boleh kosong")
    else:
        # ===== LSTM =====
        if model_choice == "LSTM":
            seq = lstm_tokenizer.texts_to_sequences([text_input])
            pad_seq = pad_sequences(seq, maxlen=100, padding="post")
            pred = lstm_model.predict(pad_seq)
            idx = np.argmax(pred)
            label = lstm_le.inverse_transform([idx])[0]
            conf = np.max(pred) * 100

        # ===== DistilBERT =====
        elif model_choice == "DistilBERT":
            inputs = distil_tok(text_input, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                outputs = distil_model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1)
            idx = torch.argmax(probs, dim=1).item()
            label = distil_le.inverse_transform([idx])[0]
            conf = probs[0][idx].item() * 100

        # ===== IndoBERT =====
        else:
            inputs = indo_tok(text_input, return_tensors="pt", truncation=True, padding=True)
            with torch.no_grad():
                outputs = indo_model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1)
            idx = torch.argmax(probs, dim=1).item()
            label = indo_le.inverse_transform([idx])[0]
            conf = probs[0][idx].item() * 100

        st.success(f"📰 **Kategori: {label}**")
        st.info(f"📈 Confidence: **{conf:.2f}%**")
