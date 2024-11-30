text = input("Masukkan karakter sembarang untuk mendeteksi huruf vokal : ")
vokal = "aeiouAEIOU"
count = sum(1 for char in text if char in vokal)
print("Jumlah Vokal:", count)