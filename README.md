# KELAS-3E-ALGORITMA-PEMROGRAMAN
🧮 Menghitung Luas dan Keliling Lingkaran

📝 Deskripsi Masalah

Dalam matematika, lingkaran merupakan salah satu bangun datar yang memiliki bentuk khusus. Untuk mengetahui ukuran sebuah lingkaran, kita dapat menghitung luas dan keliling berdasarkan jari-jari lingkaran.

Masalah yang akan dibuat adalah sebuah program sederhana untuk menghitung luas dan keliling lingkaran. Program akan menerima nilai jari-jari (r) sebagai input. Selanjutnya, program akan menghitung luas dan keliling menggunakan rumus yang telah ditentukan.

Rumus yang digunakan adalah:

- Luas lingkaran = π × r²
- Keliling lingkaran = 2 × π × r

Program kemudian menampilkan hasil luas dan keliling lingkaran.

📥 Input-Proses-Output (IPO)

Bagian| Keterangan
Input| Jari-jari lingkaran (r)
Proses| Menghitung luas dengan rumus π × r² dan keliling dengan rumus 2 × π × r
Output| Hasil luas dan keliling lingkaran

💻 Pseudocode

START

INPUT r

Luas = π × r × r
Keliling = 2 × π × r

OUTPUT "Luas lingkaran = ", Luas
OUTPUT "Keliling lingkaran = ", Keliling

END

📊 Flowchart
%%{init: {
  "themeVariables": {
    "fontSize": "12px"
  },
  "flowchart": {
    "nodeSpacing": 15,
    "rankSpacing": 20,
    "padding": 8
  }
}}%%

flowchart TD
    A([START]) --> B[/INPUT jari-jari r/]
    B --> C[/PROSES<br/>Luas = π × r × r<br/>Keliling = 2 × π × r/]
    C --> D[/OUTPUT<br/>"Luas lingkaran = ", Luas<br/>"Keliling lingkaran = ", Keliling/]
    D --> E([END])

    style A fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    style B fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    style C fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    style D fill:#e0e7ff,stroke:#4f46e5,stroke-width:2px,color:#312e81
    style E fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a

🧪 Test Case

Test Case| Input Jari-jari| Luas| Keliling
1| 7 cm| 154 cm²| 44 cm
2| 14 cm| 616 cm²| 88 cm

Keterangan:
Pada perhitungan di atas digunakan π = 22/7 karena jari-jari yang digunakan merupakan kelipatan 7.

🐍 Implementasi Python

import math

r = float(input("Masukkan jari-jari lingkaran: "))

luas = math.pi * r * r
keliling = 2 * math.pi * r

print("Luas lingkaran =", luas)
print("Keliling lingkaran =", keliling)

📸 Hasil Pengujian

Program diuji menggunakan dua nilai jari-jari, yaitu 7 cm dan 14 cm. Hasil yang diperoleh sesuai dengan perhitungan matematika yang diharapkan, yaitu:

- Untuk jari-jari 7 cm, luas = 154 cm² dan keliling = 44 cm.
- Untuk jari-jari 14 cm, luas = 616 cm² dan keliling = 88 cm.
