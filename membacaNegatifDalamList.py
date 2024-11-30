numbers = []
total_number = int(input("Masukkan total angka yang akan di tambahkan dalam list yang mendeteksi angka negatif : "))
add_number = 1
while add_number<=total_number:
    numbers.append(int(input("Masukkan Nilai ke data : ")))
    add_number+=1

negative_count = sum(1 for num in numbers if num < 0)
print("Jumlah Angka Negatif:", (negative_count))