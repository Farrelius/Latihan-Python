# PROGRAM FORMULA LIMAS SEGITIGA BY FARREL
# 08/10/2024 07:02
def limas_segitiga():
    # MENGAMBIL DATA DARI INPUT USER

    LA = int(input("Masukkan Luas Alas : "))
    LST = int(input("Masukkan Luas Sisi Tegak : "))
    T = int(input("Masukkan Tinggi : "))

# ALGORITMA
    
    LP= lambda LA,LST : LA + (3*LST)
    V = lambda LA,T : 1/3 * LA * T
    print(f'''LUAS PERMUKAAN LIMAS SEGITIGA : {LP(LA,LST)}
VOLUME LIMAS SEGITIGA : {round(V(LA,T))}''')

limas_segitiga()