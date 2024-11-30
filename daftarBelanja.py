item = []

b_item = int(input("Berapa banyak item yang ingin kamu tambahkan ke daftar belanja? : "))
add_item = 1
while add_item<=b_item:
    item.append(input(f"Masukkan item {add_item} ke daftar belanjamu : "))
    add_item += 1

print(item)