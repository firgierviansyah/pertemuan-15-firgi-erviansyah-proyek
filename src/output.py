from src.proses import (
    hitung_rata_rata,
    cari_nilai_tertinggi,
    cari_nilai_terendah,
    hitung_ketuntasan,
    tentukan_status
)


def simpan_laporan(data_siswa, path, batas=75):
    if not data_siswa:
        print("\nLaporan tidak dapat dibuat karena tidak ada data siswa.")
        return

    rata_rata = hitung_rata_rata(data_siswa)
    tertinggi = cari_nilai_tertinggi(data_siswa)
    terendah = cari_nilai_terendah(data_siswa)

    jumlah_tuntas, jumlah_belum_tuntas = hitung_ketuntasan(
        data_siswa, batas
    )

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write("========== LAPORAN NILAI SISWA ==========\n")
            file.write(f"{'Nama':<20} {'Nilai':<10} {'Status'}\n")
            file.write("-" * 45 + "\n")

            for siswa in data_siswa:
                status = tentukan_status(siswa["nilai"], batas)
                file.write(
                    f"{siswa['nama']:<20} "
                    f"{siswa['nilai']:<10.2f} "
                    f"{status}\n"
                )

            file.write("\n========== STATISTIK KELAS ==========\n")
            file.write(f"Rata-rata nilai : {rata_rata:.2f}\n")
            file.write(f"Nilai tertinggi : {tertinggi:.2f}\n")
            file.write(f"Nilai terendah  : {terendah:.2f}\n")
            file.write(f"Siswa tuntas    : {jumlah_tuntas}\n")
            file.write(f"Belum tuntas    : {jumlah_belum_tuntas}\n")

        print(f"\nLaporan berhasil disimpan di: {path}")

    except OSError as error:
        print(f"\nGagal menyimpan laporan: {error}")
