# FORMULA PERSEGI PANJANG BY FARREL
# 05/10/2024 15:01

# MENGAMBIL INPUT DATA DARI USER

P = int(input("Masukkan panjang persegi panjang : "))
L = int(input("Masukkan panjang lebar panjang : "))

# ALGORITMA

luasPP = P*L
kelilingPP = 2*(P+L)

# OUTPUT

print(f'''LUAS PERSEGI PANJANG : {luasPP}cm^2
KELILING PERSEGI PANJANG : {kelilingPP}cm^2''')