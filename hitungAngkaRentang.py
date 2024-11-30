def count_numbers_in_range(start, end):
    return end - start + 1

start = int(input("Masukkan angka awal: "))
end = int(input("Masukkan angka akhir: "))
print(f"Jumlah angka dari {start} hingga {end} adalah {count_numbers_in_range(start, end)}")