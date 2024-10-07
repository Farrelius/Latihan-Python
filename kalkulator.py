<<<<<<< HEAD
print(f'''{55*"="}
KALKULATOR 2 BILANGAN OPERASI ARITMATIKA DARI PYTHON BY FARREL
{55*"="}''')

print(f'''{45*"="}
    OPERASI ARITMATIKA DUA BILANGAN
    {45*"="}''')

# AMBIL INPUT

angka_1 = float(input("Masukkan Angka ke 1 : "))
operasi_bilangan = str(input("Masukkan operasi bilangan (+, -, x, : ): "))
angka_2 = float(input("Masukkan Angka ke 2 : "))

# ALGORITMA DAN HASIL

if operasi_bilangan == "+":
    print(f"{angka_1} + {angka_2} = {angka_1+angka_2}")
elif operasi_bilangan == "-":
    print(f"{angka_1} - {angka_2} = {angka_1-angka_2}")
elif operasi_bilangan == "x":
    print(f"{angka_1} x {angka_2} = {angka_1*angka_2}")
elif operasi_bilangan == ":":
    print(f"{angka_1} : {angka_2} = {angka_1/angka_2}")
else:
=======
print(f'''{55*"="}
KALKULATOR 2 BILANGAN OPERASI ARITMATIKA DARI PYTHON BY FARREL
{55*"="}''')

print(f'''{45*"="}
    OPERASI ARITMATIKA DUA BILANGAN
    {45*"="}''')

# AMBIL INPUT

angka_1 = float(input("Masukkan Angka ke 1 : "))
operasi_bilangan = str(input("Masukkan operasi bilangan (+, -, x, : ): "))
angka_2 = float(input("Masukkan Angka ke 2 : "))

# ALGORITMA DAN HASIL

if operasi_bilangan == "+":
    print(f"{angka_1} + {angka_2} = {angka_1+angka_2}")
elif operasi_bilangan == "-":
    print(f"{angka_1} - {angka_2} = {angka_1-angka_2}")
elif operasi_bilangan == "x":
    print(f"{angka_1} x {angka_2} = {angka_1*angka_2}")
elif operasi_bilangan == ":":
    print(f"{angka_1} : {angka_2} = {angka_1/angka_2}")
else:
>>>>>>> 4b56fd6a9cadec6fb89a2dd9343ea9458f3d7821
    print("Ada yang salah, coba lagi")