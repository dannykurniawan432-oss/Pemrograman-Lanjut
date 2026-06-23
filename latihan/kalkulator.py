# kalkulator.py

# Fungsi untuk perkalian
def perkalian(a, b):
    return a * b

# Fungsi untuk pembagian
def pembagian(a, b):
    if b == 0:
        return "Error: Tidak bisa membagi dengan nol"
    return a / b

# Fungsi untuk penambahan
def penambahan(a, b):
    return a + b

# Fungsi untuk pengurangan
def pengurangan(a, b):
    return a - b

# Fungsi untuk menghentikan program
def stop():
    print("Terimakasih telah menggunakan program ini")

# Program utama
def main():
    while True:
        operasi = input("Operasi yang diminta (perkalian, pembagian, penambahan, pengurangan, stop): ").strip().lower()

        if operasi == "stop":
            stop()
            break
        elif operasi in ["perkalian", "pembagian", "penambahan", "pengurangan"]:
            try:
                angka1 = float(input("Masukan angka 1: "))
                angka2 = float(input("Masukan angka 2: "))

                if operasi == "perkalian":
                    hasil = perkalian(angka1, angka2)
                elif operasi == "pembagian":
                    hasil = pembagian(angka1, angka2)
                elif operasi == "penambahan":
                    hasil = penambahan(angka1, angka2)
                elif operasi == "pengurangan":
                    hasil = pengurangan(angka1, angka2)

                print(f"Hasilnya adalah {hasil}")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        else:
            print("Operasi tidak valid. Pilih antara perkalian, pembagian, penambahan, pengurangan, atau stop.")

if __name__ == "__main__":
    main()
