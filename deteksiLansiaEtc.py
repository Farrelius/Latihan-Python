umur = int(input("Masukkan umurmu : "))

if 0<=umur<=4:
    print("Kamu adalah bayi")
elif 5<=umur<=10:
    print("Kamu adalah anak kecil")
elif 11<=umur<=15:
    print("Kamu adalah Anak beranjak remaja")
elif 16<=umur<=20:
    print("Kamu adalah remaja")
elif 25<=umur<=49:
    print("Kamu Adalah orang tua")
elif umur>55:
    print("Kamu adalah lansia")