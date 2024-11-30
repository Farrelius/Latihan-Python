tugas = []

b_tugas = int(input("Berapa banyak tugas yang ingin kamu tambahkan ke daftar tugas? : "))
add_tugas = 1
while add_tugas<=b_tugas:
    tugas.append(input(f"Masukkan tugas {add_tugas} ke daftar tugasmu : "))
    add_tugas += 1

print(tugas)