# tabung.py

import math

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(r):
    """
    Menghitung luas lingkaran.
    r : jari-jari lingkaran
    return : luas lingkaran
    """
    return math.pi * r**2

# Fungsi untuk menghitung volume tabung
def volume_tabung(r, t):
    """
    Menghitung volume tabung.
    r : jari-jari lingkaran
    t : tinggi tabung
    return : volume tabung
    """
    return luas_lingkaran(r) * t

# Program utama
if __name__ == "__main__":
    try:
        # Input dari pengguna
        r = input("Masukkan jari-jari tabung (bilangan bulat): ")
        t = input("Masukkan tinggi tabung (bilangan bulat): ")

        # Cek apakah input adalah integer
        if not r.isdigit() or not t.isdigit():
            raise ValueError("data yang anda masukan harus bilangan bulat")

        # Konversi ke integer
        r = int(r)
        t = int(t)

        # Hitung luas lingkaran dan volume tabung
        luas = luas_lingkaran(r)
        volume = volume_tabung(r, t)

        # Tampilkan hasil
        print(f"Luas lingkaran dengan jari-jari {r} adalah: {luas:.2f}")
        print(f"Volume tabung dengan jari-jari {r} dan tinggi {t} adalah: {volume:.2f}")

    except ValueError as ve:
        print(ve)

