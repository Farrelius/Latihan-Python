import math

def permutasi(n, r):
    """Menghitung permutasi nP_r"""
    return math.factorial(n) / math.factorial(n - r)

def kombinasi(n, r):
    """Menghitung kombinasi nC_r"""
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

def main():
    try:
        n = int(input("Masukkan nilai n (total item): "))
        r = int(input("Masukkan nilai r (item yang dipilih): "))
        
        if r > n:
            print("Nilai r tidak boleh lebih besar dari n.")
            return

        print(f"Permutasi {n}P{r} = {permutasi(n, r)}")
        print(f"Kombinasi {n}C{r} = {kombinasi(n, r)}")
    
    except ValueError:
        print("Silakan masukkan angka yang valid.")

if __name__ == "_main_":
    main()