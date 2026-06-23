try:
    jumlah = int(input("Berapa jumlah nama yang akan dimasukkann:"))
    daftar_nama = []
    for i in range(jumlah):
        nama = input(f"Nama ke {i}:")
        daftar_nama.append(nama)

    print("\nApabila semua nama sudah dimasukan....")
    idx = int(input("Panggil nama dengan index ke :"))
    print(f"Nama pada index {idx} adalah {daftar_nama[idx]}")
except ValueError:
    print("Masukan nilai angka bilangan bulat, bukan string.")
except IndexError:
    print("Indeks data tersebut tidak tersedia.")