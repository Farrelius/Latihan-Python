# KERTAS GUNTING BATU BY FARREL
# 08-11-2024

import random

print('WELCOME TO PERMAINAN KERTAS GUNTING BATU, ANDA AKAN MELAWAN DENGAN BOT')
opsiMain = input('''Apakah anda ingin bermain??
''').capitalize()



pilihanLawan = ["Kertas", "Gunting", "Batu"]
bot = random.choice(pilihanLawan)
pemain = False
user_skor = 0
bot_skor = 0

match(opsiMain):
    case 'Ya':
        while True:
            pemain = input("Ketas, Gunting atau batu??").capitalize()
            if pemain == bot:
                print("Seri")
            elif pemain == "Kertas":
                if bot == "Gunting":
                    print("Kamu kalah, dipotong oleh bot")
                    bot_skor += 1
                else:
                    print("Kamu menang! Memotong bot")
                    user_skor += 1
            elif pemain == "Batu":
                if bot == "Kertas":
                    print("Kamu kalah. Kamu ditutup kertas oleh bot")
                    bot_skor+=1
                else:
                    print("Kamu menang! menutup bot oleh kertas")
                    user_skor+=1
            elif pemain == "Gunting":
                if bot == "Batu":
                    print("Kamu kalah. dihancurkan dengan batu oleh bot!")
                    bot_skor+=1
                else:
                    print("Kamu menang! berhasil menghancurkan bot")
                    user_skor+=1
            elif pemain=='End':
                print("Hasil:")
                print(f"Bot:{bot_skor}")
                print(f"Anda:{user_skor}")
                break

    case 'Tidak':
        print("Silahkan Kembali Lagi")