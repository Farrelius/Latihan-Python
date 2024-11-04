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

elif bmi >=35:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu Sangat Obesitas")
    
elif bmi >=24.9<=35:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu Obesitas")

elif  bmi >=18.5 <=24.9:
    print(f"Nilai Index Massa Tubuhmu adalah : {bmi}, Tubuhmu normal.")




