# Draft Presentasi: Naive Bayes vs Decision Tree

**Instruksi Desain untuk Pembuat PPT:** Gunakan *template* yang minimalis (latar putih atau abu-abu terang) agar gambar visualisasi nanti terlihat jelas. Jangan gunakan terlalu banyak teks, gunakan format poin-poin (*bullet points*) persis seperti di bawah ini.

---

## SLIDE 1: JUDUL UTAMA
* **Judul:** Perbandingan Algoritma Machine Learning: Naive Bayes vs Decision Tree
* **Sub-judul:** Studi Kasus Klasifikasi Bunga menggunakan Iris Dataset
* **Disusun Oleh:**
  * [Nama anggota kelompok] - [NIM anggota kelompok]
  * [Nama anggota kelompok] - [NIM anggota kelompok]

---

## SLIDE 2: PEMBAGIAN TUGAS
* **[Nama anggota kelompok]:** 
* **[Nama anggota kelompok]:** 

---

## SLIDE 3: TEORI SINGKAT (FIRST PRINCIPLES)
* **Naive Bayes:**
  * Berbasis Probabilitas (Teorema Bayes).
  * Cara kerja: Menghitung peluang matematis dari setiap kelas berdasarkan data masa lalu.
  * Sifat: Cepat, efisien, dengan asumsi semua fitur independen (tidak saling bergantung).
* **Decision Tree:**
  * Berbasis Aturan Logika (*Rule-Based*).
  * Cara kerja: Memecah data menggunakan aturan kondisi (If-Else) secara hierarkis dari atas ke bawah.
  * Sifat: Sangat mudah diinterpretasikan visualnya oleh manusia.

---

## SLIDE 4: DATASET & TUJUAN PROGRAM
* **Tujuan:** Membuat program yang mampu memprediksi 3 spesies bunga (Setosa, Versicolor, Virginica).
* **Dataset yang Digunakan:** Iris Fisher Dataset (Terdiri dari 150 sampel bunga).
* **Parameter yang Diukur:** Panjang & Lebar Kelopak Luar (*Sepal*) dan Kelopak Dalam (*Petal*).
* **Sumber Data Resmi:** `https://archive.ics.uci.edu/ml/datasets/iris`

---

## SLIDE 5: HASIL EKSEKUSI PROGRAM
> **Instruksi Visual (Penting):** *Paste screenshot dari terminal (yang warna hitam berisi angka akurasi) di tengah slide ini.*

* Pembagian Data: 80% Data Latih (*Training*), 20% Data Uji (*Testing*).
* Berdasarkan eksekusi, kedua model mampu mengklasifikasikan spesies bunga dengan tingkat akurasi yang optimal (mendekati/mencapai 100% pada data uji).

---

## SLIDE 6: VISUALISASI MESIN
> **Instruksi Visual (Penting):** *Masukkan gambar `visualisasi_tree.png` secara penuh (Full-screen) di slide ini.*

* *Gambar di atas menunjukkan bagaimana mesin mengambil keputusan. Variabel "Petal Length" (Panjang Kelopak) menjadi parameter paling krusial untuk memisahkan spesies bunga pada tahap awal.*

---

## SLIDE 7: KESIMPULAN
* Naive Bayes dan Decision Tree sama-sama efektif untuk dataset berukuran kecil yang terstruktur rapi (seperti Iris).
* **Keunggulan Decision Tree pada tugas ini:** Mampu menghasilkan visualisasi berbentuk struktur pohon, sehingga proses mesin mengambil keputusan ("Black Box") dapat dipahami dengan sangat mudah oleh manusia.