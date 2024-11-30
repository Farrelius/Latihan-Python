list = []

b_char = int(input("Masukkan banyaknya karakter untuk ditambahkan ke list : "))
add_char = 1
char = "abcdefghijklmnopqrstuvwxyz"

while add_char<=b_char:
    list.append(input("Masukkan sembarang angka atau karakteri : "))
    add_char+=1

count_str = sum(1 for i in list if i in char)

print(count_str)