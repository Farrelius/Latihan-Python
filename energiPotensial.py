# PROGRAM ENERGI POTENSIAL BY FARREL
# 04-11-2024 08:06

# MENGAMBIL DATA DARI INPUT USER

m = float(input("Masukkan massa : "))
g = float(input("Masukkan gravitasi : "))
h = float(input("Masukkan ketinggian : "))

# ALGORITMA

EP = lambda m,g,h : m*g*h

# OUTPUT/HASIL

print(f"Energi potensialnya adalah : {EP(m,g,h)} J")