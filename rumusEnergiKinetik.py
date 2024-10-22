# PROGRAM RUMUS ENERGI KINETIK
# 22/10/2024 19:32

# RUMUS ENERGI KINETIK
def energiKinetik():

    m = float(input('Masukkan massa : '))
    v = float(input('Masukkan kecepatan : '))

    EK = lambda m,v : 1/2*m*v**2

    print('Banyaknya energi kinetik yaitu :', EK(m,v))

energiKinetik()