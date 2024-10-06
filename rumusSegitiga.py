# FORMULA SEGITIGA BY FARREL
# 05/10/2024 15:46

# MENGAMBIL INPUT DATA DARI USER

S = int(input("Masukkan Sisi Segitiga : "))
A = int(input("Masukkan Alas Segitiga : "))
T = int(input("Masukkan Tinggi Segitiga : "))

#ALGORITMA

luasS = 0.5*A*T 
kelilingS = S*3 

# OUTPUT/HASIL

print(f'''LUAS SEGITIGA : {luasS}cm
KELILING SEGITIGA : {kelilingS}cm''')