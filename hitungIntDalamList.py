list = []

b_char = int(input("Masukkan banyaknya karakter untuk ditambahkan ke list : "))
add_char = 1
char = "1234567890"

while add_char<=b_char:
    list.append(input("Masukkan sembarang angka atau karakteri : "))
    add_char+=1

count_int = sum(1 for i in list if i in char)

print(count_int)