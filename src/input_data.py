def validasi_nilai(nilai):
    """
    Memeriksa apakah nilai berada pada rentang 0 sampai 100.
    """
    try:
        nilai = float(nilai)
        return 0 <= nilai <= 100
    except (ValueError, TypeError):
        return False


def baca_data(path):
    data_siswa = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for nomor_baris, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                bagian = baris.split(",")

                if len(bagian) != 2:
                    print(f"Format data baris {nomor_baris} tidak valid.")
                    continue

                nama = bagian[0].strip()
                nilai = bagian[1].strip()

                if not nama:
                    print(f"Nama pada baris {nomor_baris} kosong.")
                    continue

                try:
                    nilai = float(nilai)
                except ValueError:
                    print(f"Nilai pada baris {nomor_baris} bukan angka.")
                    continue

                if not validasi_nilai(nilai):
                    print(f"Nilai pada baris {nomor_baris} harus 0-100.")
                    continue

                siswa = {
                    "nama": nama,
                    "nilai": nilai
                }

                data_siswa.append(siswa)

    except FileNotFoundError:
        print("File data siswa tidak ditemukan.")

    return data_siswa