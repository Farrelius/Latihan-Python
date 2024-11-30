def currency_converter(amount, rate):
    return amount * rate

amount = float(input("Masukkan jumlah uang: "))
rate = float(input("Masukkan nilai tukar: "))
converted_amount = currency_converter(amount, rate)
print("Jumlah setelah konversi:", converted_amount)