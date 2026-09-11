"""
Nama  : Suci Ramadhani
NIM   : 2225250177
Kelas : 2B
"""

print("=== KALKULATOR KOORDINAT ===")

x1 = float(input("Masukkan x1: "))
y1 = float(input("Masukkan y1: "))
x2 = float(input("Masukkan x2: "))
y2 = float(input("Masukkan y2: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print("\n=== HASIL PERHITUNGAN ===")
print(f"Titik A : ({x1:.2f}, {y1:.2f})")
print(f"Titik B : ({x2:.2f}, {y2:.2f})")
print(f"dx : {dx:.2f}")
print(f"dy : {dy:.2f}")
print(f"Jarak : {jarak:.2f}")
print(f"Titik Tengah : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")