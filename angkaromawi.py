print(f'''{45*"="}
ALGORITMA KONVERSI BILANGAN KE ANGKA ROMAWI
{45*"="}''')

angka = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romawi = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
hasil = ""

# Baca input bilangan
bilangan = int(input("Masukkan bilangan bulat positif: "))

# Tangani bilangan besar (>= 4000)
ribuan = bilangan // 1000
hasil += "M" * ribuan
bilangan %= 1000

# Konversi bilangan < 4000
i = 0
while bilangan > 0:
    while bilangan >= angka[i]:
        hasil += romawi[i]
        bilangan -= angka[i]
        i += 1

print("Angka Romawi:",hasil)