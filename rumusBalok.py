# PROGRAM FORMULA BALOK BY FARREL
# 08/10/2024 06:38

# MENGAMBIL DATA DARI INPUT USER

P = int(input("Masukkan panjang balok : "))
L = int(input("Masukkan lebar balok : "))
T = int(input("Masukkan tinggi balok : "))

# ALGORITMA

V = P*L*T
K = 2*(P+L+T)
lP = 2*(P*L)+(P*T)+(L*T)

# OUTPUT/HASIL

print(f'''VOLUME BALOK : {V}
KELILING BALOK : {K}
LUAS PERMUKAAN BALOK : {lP}''')