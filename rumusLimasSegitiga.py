# PROGRAM FORMULA LIMAS SEGITIGA BY FARREL
# 08/10/2024 07:02
def limas_segitiga():
    # MENGAMBIL DATA DARI INPUT USER

    LA = int(input("Masukkan Luas Alas : "))
    LST = int(input("Masukkan Luas Sisi Tegak : "))
    T = int(input("Masukkan Tinggi : "))

# ALGORITMA
    
    LP= LA + (3*LST)
    V = 1/3 * LA * T
    print(f'''LUAS PERMUKAAN LIMAS SEGITIGA : {LP}
VOLUME LIMAS SEGITIGA : {V}''')

limas_segitiga()