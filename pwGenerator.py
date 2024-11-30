import random
import string

def generate_password(length):
    """
    Generate a random password of a given length
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")

    length = int(input("Masukkan panjang passwordmu (min 8 characters): "))

    if length < 8:
        print("Setidaknya panjang nya password adalah 8")
        return

    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "main_":
    main()
main()