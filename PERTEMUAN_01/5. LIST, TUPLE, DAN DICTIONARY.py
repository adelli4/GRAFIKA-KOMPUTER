# nomor 5
# fungsi: menggunakan struktur data list, tuple, dan dictionary
# list digunakan untuk menyimpan beberapa pasangan titik
# tuple digunakan untuk menyimpan satu titik pusat
# dictionary digunakan untuk menyimpan atribut sebuah titik seperti koordinat dan warna.

# membuat list yang berisi tiga pasangan titik
titik = [(0, 0), (50, 50), (100, 0)]

# menampilkan semua titik menggunakan perulangan for
for t in titik: print(f"titik: {t}")

# membuat tuple untuk menyimpan titik pusat
pusat = (0, 0)

# menampilkan nilai titik pusat
print(f"titik pusat: {pusat}")

# membuat dictionary yang berisi atribut titik
titik_objek = { "x": 10, "y": 20, "warna": "biru" }

# menampilkan isi dictionary dalam format teks
print(f"titik ({titik_objek['x']},{titik_objek['y']}) berwarna {titik_objek['warna']}.")