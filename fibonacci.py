# PROGRAM GAYA BY FARREL
# 22-11-2024 23:01


# MENGAMBIL DATA DARI INPUT USER

n = int(input("Masukkan banyaknya deretan fibonacci : "))

# ALGORITMA
nn = 1
ln = [0, 1]
while nn <= n:
    ln.append(ln[-1] + ln[-2])
    nn+=1

# OUTPUT
print(ln)