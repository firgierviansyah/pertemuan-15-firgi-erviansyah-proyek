from src.input_data import baca_data
from src.proses import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_ketuntasan,
    tentukan_status
)
from src.output import simpan_laporan

BATAS_KETUNTASAN = 75
PATH_DATA = "data/contoh_data.txt"
PATH_LAPORAN = "data/laporan_nilai.txt"


def tampilkan_hasil(data_siswa):
    if not data_siswa:
        print("\nTidak ada data siswa yang valid.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = cari_nilai_tertinggi(data_siswa)
    terendah = cari_nilai_terendah(data_siswa)

    jumlah_tuntas, jumlah_belum_tuntas = hitung_ketuntasan(
        data_siswa, BATAS_KETUNTASAN
    )

    print("\n========== HASIL ANALISIS NILAI ==========")
    print(f"{'Nama':<20} {'Nilai':<10} {'Status'}")
    print("-" * 45)

    for siswa in data_siswa:
        status = tentukan_status(
            siswa["nilai"], BATAS_KETUNTASAN
        )
        print(f"{siswa['nama']:<20} {siswa['nilai']:<10.2f} {status}")

    print("\n========== STATISTIK KELAS ==========")
    print(f"Rata-rata nilai : {rata_rata:.2f}")
    print(f"Nilai tertinggi : {tertinggi:.2f}")
    print(f"Nilai terendah  : {terendah:.2f}")
    print(f"Siswa tuntas    : {jumlah_tuntas}")
    print(f"Belum tuntas    : {jumlah_belum_tuntas}")


def main():
    print("========================================")
    print(" PROGRAM PENGOLAH DAN ANALISIS NILAI")
    print("========================================")

    data_siswa = baca_data(PATH_DATA)
    tampilkan_hasil(data_siswa)
    simpan_laporan(data_siswa, PATH_LAPORAN, BATAS_KETUNTASAN)


if __name__ == "__main__":
    main()