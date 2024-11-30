def reverse_list(lst):
    return lst[::-1]

lst = list(map(int, input("Masukkan angka-angka (pisahkan dengan spasi): ").split()))
print("List terbalik:", reverse_list(lst))