# FORMULA SEGITIGA BY FARREL
# 05/10/2024 15:46

def segitiga():

# MENGAMBIL INPUT DATA DARI USER

    S = int(input("Masukkan Sisi Segitiga : "))
    A = int(input("Masukkan Alas Segitiga : "))
    T = int(input("Masukkan Tinggi Segitiga : "))

#ALGORITMA

    luasS = lambda A,T : 0.5*A*T 
    kelilingS = lambda S : S*3 

# OUTPUT/HASIL

    print(f'''LUAS SEGITIGA : {luasS(A,T)}cm
KELILING SEGITIGA : {kelilingS(S)}cm''')
    
segitiga()