# Pengujian Program Pengolah dan Analisis Nilai Siswa

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat:

- Membaca data siswa dari file.
- Memvalidasi nilai yang dimasukkan.
- Menghitung statistik kelas.
- Menentukan status ketuntasan siswa.
- Menyimpan laporan hasil analisis.

---

## 2. Ketentuan Pengujian

- Rentang nilai yang valid: **0–100**
- Batas ketuntasan: **75**
- Format data siswa: **Nama,Nilai**
- Pengujian dilakukan melalui terminal **VS Code**

---

## 3. Skenario Pengujian

| ID | Fitur | Input atau Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|--------|-------------------|----------------------|-------------|--------|
| TC01 | Pembacaan dan analisis data | Andi,85; Budi,70; Citra,90; Dewi,80; Eko,65 | Rata-rata 78, nilai tertinggi 90, nilai terendah 65, 3 siswa tuntas dan 2 belum tuntas | Rata-rata 78.00, nilai tertinggi 90.00, nilai terendah 65.00, 3 siswa tuntas, dan 2 siswa belum tuntas. | Berhasil |
| TC02 | Batas ketuntasan | Siswa dengan nilai 75 | Status **Tuntas** | Nilai 75 mendapatkan status Tuntas | Berhasil |
| TC03 | Validasi nilai di atas batas | Siswa dengan nilai 105 | Data ditolak dan muncul pesan *"Nilai harus berada pada rentang 0–100"* | Nilai pada baris 1 harus 0-100 | Berhasil |
| TC04 | Validasi nilai negatif | Siswa dengan nilai -5 | Data ditolak dan muncul pesan *"Nilai harus berada pada rentang 0–100"* | Nilai pada baris 1 harus 0-100 | Berhasil |
| TC05 | Validasi input bukan angka | Siswa dengan nilai abc | Data ditolak dan muncul pesan *"Nilai yang dimasukkan bukan angka"* | Belum diuji | Belum diuji |

---

## 4. Kesimpulan Pengujian

Kesimpulan pengujian akan dibuat setelah seluruh skenario pengujian dijalankan dan hasil aktual pada setiap test case dicatat.