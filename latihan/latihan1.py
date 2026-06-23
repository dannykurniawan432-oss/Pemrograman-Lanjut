# PROGRAM PENGELOLA DATA MAHASISWA

# 1. Cek apakah script dijalankan langsung
def main():
    print("Program berjalan...")

main()  # Tidak menggunakan idiom __name__
#==========jawaban==========
if __name__ == "__main__":
    main()


# 2. Truthy dan falsy (masih verbose)
name = "Cahyo"
hobbies = ["Membaca", "Menulis"]
data = {}

if name != "" and len(hobbies) > 0 and data != {}:
    print("Data tersedia")
else:
    print("Data tidak lengkap")
#==========jawaban==========
name = "Cahyo"
hobbies = ["Membaca", "Menulis"]
data = {}

if name and hobbies and data:
    print("Data tersedia")
else:
    print("Data tidak lengkap")


# 3. Mengecek huruf dalam string (tidak pakai in)
nama = "Universitas Jenderal Achmad Yani Yogyakarta"
if nama.find("v") != -1:
    print("Huruf ditemukan")
#==========jawaban==========
nama = "Universitas Jenderal Achmad Yani Yogyakarta"
if "v" in nama:
    print("Huruf ditemukan")

# 4. Iterasi dengan while dan index
mahasiswa = ["Ani", "Budi", "Citra"]
i = 0
while i < len(mahasiswa):
    print("Nama:", mahasiswa[i])
    i = i + 1
#==========jawaban==========
mahasiswa = ["Ani", "Budi", "Citra"]
for nama in mahasiswa:
    print("Nama:", nama)


# 5. Swap variabel pakai temp
a = 10
b = 20
temp = a
a = b
b = temp
print("a:", a, "b:", b)
#==========jawaban==========
a, b = 10, 20
a, b = b, a
print("a:", a, "b:", b)


# 6. Bangun string dengan +
chars = ["P", "y", "t", "h", "o", "n"]
word = ""
for c in chars:
    word = word + c
print(word)
#==========jawaban==========
chars = ["P", "y", "t", "h", "o", "n"]
word = "".join(chars)
print(word)


# 7. LBYL (Look Before You Leap)
d = {"nilai": "90"}
if "nilai" in d and d["nilai"].isdigit():
    nilai = int(d["nilai"])
else:
    nilai = None
print("Nilai:", nilai)
#==========jawaban==========
d = {"nilai": "90"}

try:
    nilai = int(d["nilai"])
except (KeyError, ValueError):
    nilai = None

print("Nilai:", nilai)


# 8. Enumerasi manual
names = ["Dina", "Eka", "Fajar"]
count = 0
for name in names:
    print(count, name)
    count = count + 1
#==========jawaban==========
names = ["Dina", "Eka", "Fajar"]
for i, name in enumerate(names):
    print(i, name)



# 9. List comprehension manual
data_angka = [5, 15, 20, 3]
hasil = []
for x in data_angka:
    if x > 10:
        hasil.append(x * 2)
print("Hasil:", hasil)
#==========jawaban==========
data_angka = [5, 15, 20, 3]
hasil = [x * 2 for x in data_angka if x > 10]
print("Hasil:", hasil)


# 10. Membuat dictionary manual dari dua list
keys = ["A", "B", "C"]
values = [1, 2, 3]

result = {}
i = 0
for key in keys:
    result[key] = values[i]
    i = i + 1

print(result)
#==========jawaban==========
keys = ["A", "B", "C"]
values = [1, 2, 3]

result = dict(zip(keys, values))
print(result)