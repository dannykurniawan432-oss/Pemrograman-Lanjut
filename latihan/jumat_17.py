try:
    a = [1, 2, 3]
    b = int(input("Masukkan nilai: "))
    c = int(input("Masukkan indeks list: "))
    d = a[c] + b
except ValueError:
    print("Masukan bukan string.")
except IndexError:
    print("Indeks di luar jangkauan.")