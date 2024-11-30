def arithmetic_sequence_with_input():
    a = int(input("Masukkan suku pertama: "))
    d = int(input("Masukkan beda: "))
    n = int(input("Masukkan jumlah suku: "))
    sequence = [a + i * d for i in range(n)]
    print("Deret aritmatika:", sequence)

arithmetic_sequence_with_input()