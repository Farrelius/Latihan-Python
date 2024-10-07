# PROGRAM FORMULA KERUCUT
# 07/10/2024 19:37

# MENGAMBIL DATA DARI INPUT USER

r = int(input("Masukkan jari jari kerucut : "))
s = int(input("Masukkan sisi kerucut : "))
t = int(input("Masukkan tinggi kerucut : "))

# ALGORITMA

luasK = 3.14*r(r+s)
volumeK = 1/3*3.14*r**2*t

# HASIL/OUTPUT

print(f'''LUAS KERUCUT : {luasK}
VOLUME KERUCUT : {volumeK}''')