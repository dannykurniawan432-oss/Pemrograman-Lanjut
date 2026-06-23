
def nilai_akhir(nilai_tugas_list, nilai_proyek_list):
    for tugas, proyek in zip(nilai_tugas_list, nilai_proyek_list):
        nilai_akhir = (tugas + proyek) / 2
        yield nilai_akhir


nilai_tugas = [80, 90, 70, 60]
nilai_proyek = [80, 70, 60, 50] 
nilai_akhir_generator = nilai_akhir(nilai_tugas, nilai_proyek)
print(list(nilai_akhir_generator))
for nilai in nilai_akhir_generator:
    print(nilai)
