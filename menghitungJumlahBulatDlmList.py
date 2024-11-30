def count_integers(numbers):
    count = 0
    for num in numbers:
        if isinstance(num, int): 
            count += 1
    return count


user_input = input("Masukkan angka-angka (pisahkan dengan spasi): ")

numbers = user_input.split()


converted_numbers = []
for item in numbers:
    try:
        converted_numbers.append(int(item))
    except ValueError:
        try:
            converted_numbers.append(float(item))
        except ValueError:
            continue


jumlah_bulat = count_integers(converted_numbers)
print("Jumlah angka bulat dalam list:", jumlah_bulat)