tahun_lahir = int(input("Masukkan tahun lahirmu: "))

tahun = 2024
kabisat_umur = 0

while tahun_lahir<tahun:
    kabisat_umur += 1
    tahun_lahir += 4
    

print(f"Umur anda dalam tahun kabisat adalah : {kabisat_umur}")