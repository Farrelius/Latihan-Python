# PRORGRAM JARAK BY FARREL
# 08-11-2024 07:36

# MENGAMBIL DATA DARI INPUT USER

v = float(input("Masukkan kecepatan : "))
t = float(input("Masukkan waktu : "))

# ALGORITMA

s = lambda v,t : v*t

# OUTPUT/HASIL

print(f"Jaraknya adalah : {s(v,t)}")