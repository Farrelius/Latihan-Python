# PROGRAM FORMULA TRAPESIUM BY FARREL
# 07/10/2024 17:20

# MENGAMBIL DATA DARI INPUT USER

a = int(input("Masukkan sisi atas : "))
b = int(input("Masukkan sisi bawah : "))
t = int(input("Masukkan tingginya : "))
s = int(input("Masukkan sisi: "))

# ALGORITMA

luasT = 0.5*(a+b)*t
kelilingt = s*4

# HASIL/OUTPUT

print(f'''LUAS TRAPESIUM = {luasT}
KELILING TRAPESIUM = {kelilingt}''')