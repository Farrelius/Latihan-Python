year = int(input("Masukkan tahun : "))
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(year, "adalah tahun kabisat:",is_leap)