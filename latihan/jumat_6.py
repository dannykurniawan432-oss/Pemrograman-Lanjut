data = ["dani","fajar","nada"]
for i, nama in enumerate(data):
    print("nama mahasiswa {}: {}".format(i+1, nama))
for i, nama in enumerate(data):
    if i % 2 == 0:
        print("nama mahasiswa {}: {}".format(i+1, nama))
