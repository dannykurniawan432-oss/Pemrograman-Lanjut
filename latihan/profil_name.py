# profile_name.py

def main():
    daftar_nama = []  # List untuk menyimpan nama-nama

    while True:
        pilihan = input("Masukan Nama ?\nya/tidak: ").strip().lower()
        
        if pilihan == "ya":
            nama = input("Nama: ").strip()
            daftar_nama.append(nama)
        elif pilihan == "tidak":
            break
        else:
            print("Pilihan tidak valid, ketik 'ya' atau 'tidak'.")
    
    # Tampilkan semua nama yang telah dimasukkan
    if daftar_nama:
        print("\nBeberapa nama yang telah dimasukan")
        for i, nama in enumerate(daftar_nama, start=1):
            print(f"Nama {i} adalah {nama}")
    else:
        print("\nTidak ada nama yang dimasukkan.")

if __name__ == "__main__":
    main()
