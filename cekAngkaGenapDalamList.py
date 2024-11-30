list = []

b_list = int(input("Masukkan banyaknya list : "))

add_list = 1

while add_list<=b_list:
    list.append(int(input("Masukkan angka ke dalam list : ")))
    add_list+=1

bilangan_genap = sum(1 for i in list if i % 2 == 1)

print("Total bilangan genap dalam list adalah : ", bilangan_genap)