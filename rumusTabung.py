# PROGRAM FORMULA RUMUS TABUNG BY FARREL
# 07/10/2024

def tabung():

# MENGAMBIL DATA DARI INPUT USER

    r = int(input("Masukkan jari jari tabung : "))
    t = int(input("Masukkan tinggi tabung : "))

# ALGORITMA

    luasT = lambda r,t : 3.14*r**2*t
    volumeT = lambda r,t : 2*3.14*r*t + 2*3.14*r**2

# HASIL/OUTPUT

    print(f'''LUAS TABUNG = {luasT(r,t)}
VOLUME TABUNG = {volumeT(r,t)}''')
    
tabung()