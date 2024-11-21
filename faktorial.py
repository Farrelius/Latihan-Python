# PROGRAM FAKTORIAL BY FARREL
# 21-11-2024 20:16

# MENGAMBIL DATA DARI INPUT USER

n = int(input("Masukkan nilai yang akan di faktorialkan : "))

# ALGORITMA

a = n
while a != 1:
    n = (a-1)*n
    a = a-1

#OUTPUT 

print(n)