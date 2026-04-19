# Iris Morphology Analytics System: Probabilistic vs Structural Analysis

Sistem ini merupakan implementasi komparatif antara dua paradigma utama dalam *Supervised Learning*: pendekatan probabilistik (**Naive Bayes**) dan pendekatan berbasis aturan hierarkis (**Decision Tree**). Sistem ini dirancang untuk menganalisis morfologi spesies bunga berdasarkan parameter numerik.

## 📊 Dataset: Iris Fisher
Sistem menggunakan **Iris Dataset** sebagai basis data latih dan uji.
- **Data Source:** [UCI Machine Learning Repository - Iris](https://archive.ics.uci.edu/ml/datasets/iris)
- **Metadata:** Terdiri dari 150 sampel dengan 4 fitur utama (Petal/Sepal Length & Width).
- **Spesies Target:** Iris Setosa, Iris Versicolor, Iris Virginica.

## 🚀 Panduan Instalasi & Eksekusi

Pilih panduan yang sesuai dengan sistem operasi yang Anda gunakan.

### A. Untuk Pengguna Windows (Rekomendasi untuk Teman)
Jika Anda ingin cara cepat, buka **Command Prompt (CMD)** di folder proyek ini dan jalankan perintah gabungan ini:
```cmd
pip install -r requirements.txt && python main.py