# PROGRAM FORMULA JAJAR GENJANG BY FARREL
# 07/10/2024 14:32

def jajarGenjang():
# MENGAMBIL DATA DARI INPUT USER
    a = int(input("Masukkan alas jajar genjang : "))
    t = int(input("Masukkan tinggi jajar genjang : "))
    b = int(input("Masukkan sudut jajar genjang : "))

# ALGORITMA

    luasJG = lambda a,t : a*t
    kelilingJG = lambda a,b : 2*a+b

# OUTPUT/HASIL

    print(f'''LUAS JAJAR GENJANG : {luasJG(a,t)}
    KELILING JAJAR GENJANG : {kelilingJG(a,b)}''')

jajarGenjang()