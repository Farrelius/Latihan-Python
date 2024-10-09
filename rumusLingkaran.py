# FORMULA LINGKARAN BY FARREL
# 05/10/2024 16:01

def lingkaran():

# MENGAMBIL INPUT DATA DARI USER

    r = int(input("Masukkan jari jari lingkaran : "))

# ALGORIMTA

    luasL = lambda r : 3.14 * r**2
    kelilingL = lambda r : 2*3.14*r

# OUTPUT/HASIL

    print(f'''LUAS LINGKARAN : {luasL(r)}cm
KELILING LINGKARAN : {round(kelilingL(r))}cm''')
    
lingkaran()