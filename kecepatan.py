# PROGRAM KECEPATAN BY FARREL 
# 08-11-2024 07:30

# MENGAMBIL DATA DARI INPUT USER

s = float(input("Masukkan jarak : "))
t = float(input("Masukkan Waktu : "))

# ALGORITMA

V = lambda s,t : s/t

# HASIL

print(f"Kecepatannya adalah : {V(s,t)}")