# PROGRAM BY FARREL
# 23-11-2024 16:11

var = 'abcdefghijklmnopqrstuvwxyz'
list = []
n = 0
a = 1
for i in var:
    try:
        list.append(int(input(f"Masukkan nilai {a} : ")))
        a+=1
        n+=1
    except ValueError:
        print(list)
        break

print(f"Total : {sum(list)}")
print(f"Rata Rata : {sum(list)/n}")
print(f"Tertinggi : {max(list)}")
print(f"Terendah : {min(list)}")