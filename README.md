# 🏥 MedikaCare – Sistem Diagnosa Penyakit Berbasis AI

**MedikaCare** merupakan aplikasi berbasis Artificial Intelligence (AI) yang dirancang untuk membantu proses diagnosis penyakit melalui analisis data vital dan gejala yang dialami pasien.

Sistem ini memanfaatkan teknologi Machine Learning untuk menganalisis kondisi kesehatan pasien dan menghasilkan informasi berupa diagnosis penyakit, tingkat keparahan kondisi, serta rekomendasi tindakan berdasarkan data yang dimasukkan.

MedikaCare juga dilengkapi dengan fitur pengelolaan riwayat pasien sehingga informasi pemeriksaan dapat disimpan, ditampilkan, diperbarui, dan dihapus melalui aplikasi.

## ✨ Fitur Utama

- **Input Data Pasien** – Memasukkan identitas dan informasi dasar pasien.
- **Analisis Data Vital** – Menganalisis detak jantung, saturasi oksigen (SpO2), tekanan darah, dan suhu tubuh.
- **Identifikasi Gejala** – Memasukkan gejala yang dialami pasien sebagai bagian dari proses diagnosis.
- **Diagnosa Berbasis AI** – Membantu menganalisis kondisi pasien menggunakan model Machine Learning.
- **Analisis Tingkat Keparahan** – Mengidentifikasi tingkat keparahan kondisi berdasarkan hasil analisis sistem.
- **Rekomendasi Tindakan** – Menampilkan rekomendasi penanganan berdasarkan hasil analisis.
- **Riwayat Pasien** – Menyimpan dan menampilkan data pemeriksaan pasien.
- **Detail Rekam Medis** – Menampilkan informasi klinis, gejala, dan hasil diagnosis.
- **Edit Data Pasien** – Memperbarui informasi pasien dan melakukan analisis ulang.
- **Hapus Riwayat** – Menghapus data rekam medis pasien.

## 🩺 Parameter Pemeriksaan

### 1. Data Pasien dan Tanda Vital

| Parameter | Keterangan |
|---|---|
| Patient Name | Nama pasien |
| Age | Usia pasien |
| Gender | Jenis kelamin |
| Heart Rate | Detak jantung (bpm) |
| Oxygen Saturation | Saturasi oksigen (SpO2) |
| Systolic | Tekanan darah sistolik |
| Diastolic | Tekanan darah diastolik |
| Body Temperature | Suhu tubuh (°C) |

### 2. Identifikasi Gejala

MedikaCare menyediakan delapan pilihan gejala yang dapat diidentifikasi:

- Body Ache (Badan pegal)
- Shortness of Breath (Sesak napas)
- Cough (Batuk)
- Fatigue (Kelelahan)
- Sore Throat (Sakit tenggorokan)
- Fever (Demam)
- Headache (Sakit kepala)
- Runny Nose (Hidung meler)

### 3. Hasil Analisis Sistem

Setelah data pasien dimasukkan, sistem menghasilkan tiga informasi utama:

1. **Diagnosis Penyakit** – Hasil analisis kondisi kesehatan pasien berdasarkan data yang diberikan.
2. **Tingkat Keparahan (Severity)** – Informasi mengenai tingkat keparahan kondisi pasien.
3. **Rekomendasi Tindakan (Treatment Plan)** – Rekomendasi tindakan berdasarkan hasil analisis sistem.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|---|---|
| Python | Bahasa pemrograman backend |
| FastAPI | Pengembangan REST API |
| Pandas | Pengolahan data pasien |
| Joblib | Memuat model Machine Learning |
| Scikit-learn | Ekosistem model Machine Learning |
| SQLAlchemy | Pengelolaan database menggunakan ORM |
| PostgreSQL | Penyimpanan data rekam medis |
| Neon.tech | Layanan database PostgreSQL cloud |
| HTML | Struktur halaman aplikasi |
| JavaScript | Interaksi dan komunikasi frontend dengan backend |
| Tailwind CSS | Desain dan styling antarmuka |
