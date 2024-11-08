# PROGRAM WAKTU BY FARREL
# 08-11-2024 07:41

# MENGAMBIL DATA DARI INPUT USER

s = float(input("Masukkan jarak : "))
v = float(input("Masukkan kecepatan : "))

# ALGORITMA

t = lambda s,v : s/v

# OUTPUT/HASIL

print(f"Waktunya adalah : {t(s,v)}")