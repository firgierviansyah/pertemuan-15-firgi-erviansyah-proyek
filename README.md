# Program Pengolah dan Analisis Nilai Siswa

## 1. Deskripsi Proyek

Program Pengolah dan Analisis Nilai Siswa adalah program berbasis Python yang digunakan untuk membaca, mengolah, dan menganalisis nilai siswa. Program ini membantu pengguna mengetahui statistik nilai kelas dan status ketuntasan setiap siswa.

## 2. Fitur Program

- Membaca data siswa dari file teks.
- Memvalidasi nama dan nilai siswa.
- Memastikan nilai berada dalam rentang 0–100.
- Menghitung nilai rata-rata kelas.
- Menentukan nilai tertinggi dan terendah.
- Menghitung jumlah siswa tuntas dan belum tuntas.
- Menentukan status ketuntasan siswa.
- Menyimpan hasil analisis ke dalam file laporan.

## 3. Teknologi dan Kebutuhan

- Python 3
- Visual Studio Code
- Terminal

## 4. Cara Menjalankan Program

1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah berikut:
   ```bash
   python main.py
4. Hasil analisis akan ditampilkan di terminal.
5. Laporan hasil analisis disimpan di data/laporan_nilai.txt.

## 5. Struktur Folder
```text
nama-proyek/
├── README.md
├── .gitignore
├── main.py
├── src/
│   ├── __init__.py
│   ├── input_data.py
│   ├── proses.py
│   └── output.py
├── data/
│   └── contoh_data.txt
├── tests/
│   └── test_case.md
└── docs/
    └── screenshot/
```

## 6. Pengujian Program

Pengujian dilakukan menggunakan lima skenario:

- TC01: Pembacaan dan analisis data normal.
- TC02: Pengujian batas ketuntasan nilai 75.
- TC03: Validasi nilai di atas 100.
- TC04: Validasi nilai negatif.
- TC05: Validasi input bukan angka.

Hasil pengujian dicatat dalam file `tests/test_case.md`.

## 7. Hasil Pengujian

Berdasarkan lima skenario pengujian yang telah dilakukan, program berhasil menjalankan pengujian sesuai hasil yang diharapkan.

## 8. Dokumentasi

Bukti pelaksanaan program dan pengujian disimpan dalam folder `docs/screenshot/`.

## 9. Anggota dan Kontribusi

- Nama: Firgi Erviansyah, dkk.
- Kontribusi: Perancangan, implementasi program, pengujian, debugging, dan dokumentasi proyek.

## 10. Referensi

- Modul Bahan Ajar Pertemuan 15: Implementasi, Pengujian, dan Dokumentasi Proyek.
- Python Documentation: https://docs.python.org/3/