Kebun = ["Carrot", "Carrot", "Carrot", "Carrot", "Carrot", "Carrot", "Carrot"]
print(Kebun)
buku_pelajaran = ['Bahasa Indonesia', 'Bahasa Arab', 'Wafa', 'Matematika']

print("Buku Pelajaran *UNKNOWN* : ", buku_pelajaran)


print(f'*UNKOWN* Mengambil Buku {buku_pelajaran[1]}')

buku_pelajaran[0] = "Pendidikan Pancasila"
print("Buku Sudah Di Ganti : ", buku_pelajaran)


buku_pelajaran.pop()
print("Buku Sudah Di Hapus : ", buku_pelajaran)


buku_pelajaran.remove("Wafa")
print("Buku Sudah Di Hapus : ", buku_pelajaran)