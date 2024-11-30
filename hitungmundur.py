def penghitung_mundur(angka):
    while angka >= 0:
        print(angka)
        angka -= 1

def main():
    try:
        angka_input = int(input("Masukkan angka untuk menghitung mundur: "))
        print("Menghitung mundur:")
        penghitung_mundur(angka_input)
    except ValueError:
        print("Silakan masukkan angka yang valid.")

if __name__ == "__main__":
    main()