# Career Evaluator AI 🚀
### Sistem Pendukung Keputusan Berbasis Logika Fuzzy (Mamdani)

Aplikasi web premium yang dirancang untuk membantu profesional mengevaluasi kelayakan tawaran pekerjaan atau magang menggunakan **Logika Fuzzy Mamdani**. Sistem ini menganalisis empat parameter utama untuk memberikan skor kelayakan yang akurat dan objektif.

![Vercel Status](https://img.shields.io/badge/Vercel-Deployed-success?style=for-the-badge&logo=vercel)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-white?style=for-the-badge&logo=flask)

---

## 👤 Informasi Mahasiswa
- **Nama:** Nadine Ariesta
- **NIM:** H1D024028
- **Tugas:** Responsi Praktikum Kecerdasan Buatan (KB)
- **Live Demo:** [sistemfuzzy-nadin.vercel.app](https://sistemfuzzy-nadin.vercel.app)

---

## ✨ Fitur Utama
- **Premium UI/UX:** Desain modern menggunakan Glassmorphism, animasi bokeh, dan tipografi "Mix-Match" (Montserrat & Instrument Serif).
- **Fuzzy Logic Engine:** Menggunakan library `scikit-fuzzy` untuk memproses inferensi Mamdani secara presisi.
- **Analisis 4 Parameter:**
  - **Kompensasi (Gaji):** Penilaian finansial (0 - 10 Juta+).
  - **Relevansi:** Kesesuaian tugas dengan passion dan keahlian (Skala 1-10).
  - **Fleksibilitas:** Work-life balance dan kebijakan kerja (Skala 1-10).
  - **Kredibilitas:** Reputasi perusahaan dan jenjang karir (Skala 1-10).
- **Smart Insights:** Memberikan saran karir manusiawi berdasarkan hasil evaluasi.
- **Responsive Design:** Optimal diakses melalui perangkat desktop maupun mobile.

---

## 🛠️ Tech Stack
- **Backend:** Python (Flask)
- **Fuzzy Library:** `scikit-fuzzy`, `numpy`, `networkx`
- **Frontend:** HTML5, Vanilla CSS, JavaScript (ES6+)
- **Icons:** Phosphor Icons
- **Deployment:** Vercel

---

## 📐 Logika Fuzzy (Mamdani)
Sistem ini mengimplementasikan logika fuzzy dengan struktur berikut:
1. **Fuzzifikasi:** Mengubah nilai input tegas menjadi nilai linguistik (Rendah, Sedang, Tinggi).
2. **Mesin Inferensi:** Menggunakan aturan IF-THEN untuk menentukan hubungan antar parameter.
3. **Defuzzifikasi:** Menggunakan metode **Centroid** untuk menghasilkan skor kelayakan akhir (0-100%).

### Kategori Hasil:
- **0 - 20%:** Sangat Tolak
- **21 - 40%:** Tolak
- **41 - 60%:** Pertimbangkan
- **61 - 80%:** Terima
- **81 - 100%:** Sangat Layak

---

## 🚀 Cara Menjalankan Secara Lokal

1. **Clone Repositori**
   ```bash
   git clone https://github.com/NadineAriesta/H1D024028-PraktikumKB-ResponsiSistemFuzzy.git
   cd H1D024028-PraktikumKB-ResponsiSistemFuzzy
   ```

2. **Install Dependensi**
   ```bash
   pip install -r sistem_fuzzy/requirements.txt
   ```

3. **Jalankan Aplikasi**
   ```bash
   python sistem_fuzzy/app.py
   ```
   Buka `http://127.0.0.1:5000` di browser Anda.

---

## 📁 Struktur Folder
```text
.
├── sistem_fuzzy/
│   ├── app.py              # Flask Backend & Routes
│   ├── fuzzy_logic.py      # Implementasi Logika Fuzzy Mamdani
│   ├── requirements.txt    # Daftar Library Python
│   ├── vercel.json         # Konfigurasi Cloud Deployment
│   └── templates/
│       └── index.html      # Frontend (HTML, CSS, JS)
└── README.md               # Dokumentasi Proyek
```

---

© 2026 Nadine Ariesta | Praktikum Kecerdasan Buatan
