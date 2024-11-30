import random

def tebak_angka():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 hingga 100.")
    
    # Komputer memilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    jumlah_tebakan = 0
    tebakan = None

    while tebakan != angka_rahasia:
        try:
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1
            
            if tebakan < angka_rahasia:
                print("Tebakan Anda terlalu rendah. Coba lagi!")
            elif tebakan > angka_rahasia:
                print("Tebakan Anda terlalu tinggi. Coba lagi!")
            else:
                print(f"Selamat! Anda telah menebak angka {angka_rahasia} dengan benar dalam {jumlah_tebakan} tebakan.")
        
        except ValueError:
            print("Silakan masukkan angka yang valid.")

if __name__ == "_main_":
    tebak_angka()
tebak_angka()