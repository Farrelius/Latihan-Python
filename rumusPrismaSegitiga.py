# PROGRAM RUMUS PRISMA SEGITIGA BY FARREL
# 20/10/2024 14:21

def prisma_segitiga():

# AMBIL DATA DARI INPUT USER 

    LA = int(input("Masukkan Luas Alas Prisma Segitiga : "))
    T = int(input("Masukkan Tinggi Prisma Segitiga : "))
    LS = int(input("Masukkan Luas Selimut Prisma Segitiga : "))

# ALGORITMA

    L = lambda LA,LS:  2*LA+LS
    V = lambda LA,T : LA*T

    print(f'''LUAS PRISMA SEGITIGA ADALAH = {L(LA,LS)}
VOLUME PRISMA SEGITIGA ADALAH = {V(LA,T)}''')
    
prisma_segitiga()