def log_transaksi(func):
    def wrapper(total_belanja, uang_bayar, nama_pembeli):
        print(f"total belanja: {total_belanja}")
        print(f"uang bayar: {uang_bayar}")
        try:
            hasil = func(total_belanja, uang_bayar, nama_pembeli)
            print(f"{nama_pembeli} status transaksi berhasil")
            return hasil
        except Exception as e:
            print(f"error: {e}")
            print(f"{nama_pembeli} status transaksi gagal")
    return wrapper

@log_transaksi
def transaksi_pembelian(total_belanja, uang_bayar, nama_pembeli):
    try:
        total_belanja = float(total_belanja)
        uang_bayar = float(uang_bayar)
    except Exception:
        raise ValueError("input harus berupa angka")

    if uang_bayar < total_belanja:
        raise ValueError("uang bayar tidak cukup")

    kembalian = uang_bayar - total_belanja
    print(f"kembalian yang diterima adalah: {kembalian}")
    return kembalian



jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))

for i in range(jumlah_transaksi):
    print(f"\nTransaksi ke-{i+1}")
    nama = input("Masukkan nama pembeli: ")
    total = input("Masukkan total belanja: ")
    bayar = input("Masukkan uang bayar: ")

    transaksi_pembelian(total, bayar, nama)
    print("-----")


