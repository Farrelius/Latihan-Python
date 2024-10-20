# PROGRAM KUBUS BY FARREL
# 20/10/2024 14:37

def kubus():

# AMBIL DATA DARI INPUT USER 

    R = int(input("Masukkan Rusuk Kubus : "))

# ALGORITMA

    L = lambda R:  6*R**2
    V = lambda R : R*3

    print(f'''LUAS KUBUS ADALAH = {L(R)}
VOLUME KUBUS ADALAH = {V(R)}''')
    
kubus()