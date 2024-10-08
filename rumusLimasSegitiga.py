# PROGRAM FORMULA LIMAS SEGITIGA BY FARREL
# 08/10/2024 07:02

# MENGAMBIL DATA DARI INPUT USER

LA = int(input("Masukkan Luas alasnya : "))
LST = int(input("Masukkan Luas Sisi Tegaknya : "))
T = int(input("Masukkan Tingginya : "))

# ALGORITMA

LP= LA + (3*LST)
V = 1/3 * LA * T

# OUTPUT/HASIL

print(f'''LUAS PERMUKAAN LIMAS SEGITIGA : {LP}
VOLUME LIMAS SEGITIGA : {V}''')