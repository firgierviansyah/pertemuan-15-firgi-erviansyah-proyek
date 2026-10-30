def hitung_rata_rata(data_siswa):
    if not data_siswa:
        return 0

    total = sum(siswa["nilai"] for siswa in data_siswa)
    return total / len(data_siswa)


def cari_nilai_tertinggi(data_siswa):
    if not data_siswa:
        return 0

    return max(siswa["nilai"] for siswa in data_siswa)


def cari_nilai_terendah(data_siswa):
    if not data_siswa:
        return 0

    return min(siswa["nilai"] for siswa in data_siswa)


def hitung_ketuntasan(data_siswa, batas=75):
    jumlah_tuntas = 0
    jumlah_belum_tuntas = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= batas:
            jumlah_tuntas += 1
        else:
            jumlah_belum_tuntas += 1

    return jumlah_tuntas, jumlah_belum_tuntas


def tentukan_status(nilai, batas=75):
    """
    Menentukan status ketuntasan siswa.
    """
    if nilai >= batas:
        return "Tuntas"
    else:
        return "Belum Tuntas"