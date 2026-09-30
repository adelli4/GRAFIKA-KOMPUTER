# nomor 3
# fungsi: menentukan posisi titik berdasarkan nilai koordinat x
# menggunakan if-else untuk menentukan apakah titik berada di kanan,
# kiri, atau tengah layar
# perulangan for digunakan untuk menampilkan angka 1 sampai 5

x = int(input("Masukkan nilai x: "))	# memasukkan nilai koordinat x

if x > 0:
    print("Titik di kanan layar.")
elif x < 0:
    print("Titik di kiri layar.")
else:
    print("Titik di tengah.")

# menampilkan angka 1 sampai 5 sebagai simulasi iterasi titik
    print("Menampilkan 5 titik:")
for i in range(1, 6):
    print(f"Titik ke-{i}")