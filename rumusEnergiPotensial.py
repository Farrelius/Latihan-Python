def energi_potensial():

    m = float(input("Masukkan massanya : "))
    g = float(input("Masukkan kecepatan gravitasi : "))
    h = float(input("Masukkan ketinggian : "))

    EP = m*g*h
    print(EP, "Joule")

energi_potensial()