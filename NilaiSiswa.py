# PROGRAM PENENTU GRADE SISWA BY FARREL
# 04/11/2024

# MENGAMBIL DATA DARI USER

ns = float(input("Masukkan nilai siswa : "))

# ALGORITMA DAN OUTPUT

if 90<=ns<=100:
    print("Nilai siswa = A")
    
elif 70<=ns<=89:
    print("Nilai siswa = B")

elif 60<=ns<=69:
    print("Nilai siswa = C")

elif 50<=ns<=59:
    print("Nilai siswa = D")

elif 40<=ns<=49:
    print("Nilai siswa = E")

elif ns <= 39:
    print("Nilai siswa = F")