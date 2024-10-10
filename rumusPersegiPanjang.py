# FORMULA PERSEGI PANJANG BY FARREL
# 05/10/2024 15:01

def persegi_panjang():

# MENGAMBIL INPUT DATA DARI USER

    P = int(input("Masukkan panjang persegi panjang : "))
    L = int(input("Masukkan panjang lebar panjang : "))

# ALGORITMA

    luasPP = lambda P,L : P*L
    kelilingPP = lambda P,L : 2*(P+L)

# OUTPUT

    print(f'''LUAS PERSEGI PANJANG : {luasPP(P,L)}cm^2
KELILING PERSEGI PANJANG : {kelilingPP(P,L)}cm^2''')
    
persegi_panjang()