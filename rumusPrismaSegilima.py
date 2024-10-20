# PROGRAM RUMUS PRISMA SEGITIGA BY FARREL
# 20/10/2024 14:37

def prisma_segilima():

# AMBIL DATA DARI INPUT USER 

    LA = int(input("Masukkan Luas Alas Prisma Segilima : "))
    T = int(input("Masukkan Tinggi Prisma Segilima: "))
    S = int(input("Masukkan Sisi Prisma Segilima : "))

# ALGORITMA

    K = lambda S:  5*S
    V = lambda LA,T : LA*T

    print(f'''KELILING PRISMA SEGILIMA ADALAH = {K(S)}
VOLUME PRISMA SEGILIMA ADALAH = {V(LA,T)}''')
    
prisma_segilima()