# PROGRAM FORMULA LIMAS SEGILIMA BY FARREL
# 22/10/2024 06:35

def limas_segilima():
    # MENGAMBIL DATA DARI INPUT USER
    La = float(input("Masukkan Luas alas limas segilima : "))
    t = float(input("Masukkan tinggi limas segilima : "))
    # ALGORITMA

    V = lambda La,t : 1/3*La*t

    # OUTPUT/HASIL

    print(f'''VOLUME LIMAS SEGILIMA : {V(La,t)}''')

limas_segilima()