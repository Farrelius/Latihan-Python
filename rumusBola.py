# PROGRAM FORMULA BOLA BY FARREL
# 07/10/2024 19:26

# MENGAMBIL DATA DARI INPUT USER

def bola():
    r = int(input("Masukkan jari jari bola : "))

# ALGORITMA

    luasB = lambda r : 4*3.14*r**2
    volumeB = lambda r : 4/3*3.14*r**3

# HASIL/OUTPUT

    print(f'''LUAS BOLA : {luasB(r)}
VOLUME BOLA : {volumeB(r)}''')
    
bola()