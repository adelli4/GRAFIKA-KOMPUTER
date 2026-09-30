# nomor 4
# fungsi: menghitung jarak antara dua titik
# rumus yang digunakan adalah akar dari
# ((x2 - x1)^2 + (y2 - y1)^2)

import math

def hitung_jarak(x1, y1, x2, y2):
    
    # menghitung jarak antara titik pertama dan titik kedua
    jarak = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return jarak

# memanggil fungsi dengan koordinat (0,0) dan (3,4)
hasil = hitung_jarak(0, 0, 3, 4)
# menampilkan hasil perhitungan jarak
print(f"Jarak antara dua titik: {hasil}")