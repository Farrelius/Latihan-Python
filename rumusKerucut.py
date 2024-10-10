# PROGRAM FORMULA KERUCUT
# 07/10/2024 19:37

def kerucut():

# MENGAMBIL DATA DARI INPUT USER

    R = int(input("Masukkan jari jari kerucut : "))
    S = int(input("Masukkan sisi kerucut : "))
    T = int(input("Masukkan tinggi kerucut : "))

# ALGORITMA

    luasK = lambda R,S : 3.14*R*R + R*S
    volumeK = lambda R,T : 1/3*3.14*R**2*T

# HASIL/OUTPUT

    print(f'''LUAS KERUCUT : {luasK(R,S)}
VOLUME KERUCUT : {volumeK(R,T)}''')
    
kerucut()