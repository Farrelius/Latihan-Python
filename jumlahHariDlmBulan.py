def days_in_month():
    month = int(input("Masukkan bulan (1-12): "))
    year = int(input("Masukkan tahun: "))
    if month in [1, 3, 5, 7, 8, 10, 12]:
        print("Jumlah hari:", 31)
    elif month in [4, 6, 9, 11]:
        print("Jumlah hari:", 30)
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Jumlah hari:", 29)
        else:
            print("Jumlah hari:", 28)
    else:
        print("Bulan tidak valid.")

days_in_month()