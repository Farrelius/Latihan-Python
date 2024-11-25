# PROGRAM BMI BY FARREL
# 04-11-2024 17:00

# MENGAMBIL DATA DARI INPUT USER

tb = float(input("Masukkan Tinggi Badan (m) : "))
bb = float(input("Masukkan Berat Badan : "))

# ALGORITMA

bmi = bb/(tb*tb)

# OUTPUT

if bmi <=18.5:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuh anda sangat kurus")

elif bmi >= 35:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu Sangat Obesitas")
    
elif 24.9<=bmi<=35:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu Obesitas")

elif  18.5<=bmi<=24.9:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu normal.")