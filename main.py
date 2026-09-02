import math

# Input
r = float(input("Masukkan jari-jari lingkaran (cm): "))

# Proses
luas = math.pi * r * r
keliling = 2 * math.pi * r

# Output
print("\n=== HASIL PERHITUNGAN ===")
print(f"Luas lingkaran = {luas:.2f} cm²")
print(f"Keliling lingkaran = {keliling:.2f} cm")