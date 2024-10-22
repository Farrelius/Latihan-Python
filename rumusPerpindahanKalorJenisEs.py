#  PROGRAM RUMUS PERPINDAHAN KALOR JENIS ES BY FARREL
# 22/10/2024 17:19

def PKJ ():
    # AMBIL DATA DARI INPUT USER
    m = float(input("Masukkan massa kalor : "))
    c = float(input("Masukkan kalor zatnya : "))
    delta = float(input("Masukkan perubahan suhu zatnya : "))
    t = float(input("Masukkan waktunya: "))

    Q1 = lambda m,c,delta,t : m*c*delta*t

    print(f"Jadi, banyaknya perpindahan kalor es nya yaitu: {Q1(m,c,delta,t)}")

PKJ()