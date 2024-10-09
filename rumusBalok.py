# PROGRAM FORMULA BALOK BY FARREL
# 08/10/2024 06:38

# MENGAMBIL DATA DARI INPUT USER

def balok():

    P = int(input("Masukkan panjang balok : "))
    L = int(input("Masukkan lebar balok : "))
    T = int(input("Masukkan tinggi balok : "))

# ALGORITMA

    V = lambda P,L,T : P*L*T
    K = lambda  P,L,T : 2*(P+L+T)
    lP = lambda P,L,T: 2*(P*L)+(P*T)+(L*T)

# OUTPUT/HASIL

    print(f'''VOLUME BALOK\t\t: {V(P,L,T)}
KELILING BALOK\t\t: {K(P,L,T)}
LUAS PERMUKAAN BALOK\t: {lP(P,L,T)}''')
    
balok()