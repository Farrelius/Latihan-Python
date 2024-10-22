#  PROGRAM RUMUS PERCEPATAN BY FARREL
# 22/10/2024 17:27  

def percepatan():
    v2 = float(input('Masukan Kecepatan (Velocity)2 : '))
    v1 = float(input('Masukan Kecepatan (Velocity)1 : '))
    t2 = float(input('Masukan Waktu (time)2 : '))
    t1 = float(input('Masukan Waktu (time)1 : '))


    a = v2 - v1 / t2 - t1

    print('Kecepatan rata ratanya adalah =', a)

percepatan()