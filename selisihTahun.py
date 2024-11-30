print(f'''{18*"-"}
WAKTU TANGGAL KE 1
{18*"-"}''')

bulan1 = int(input("Masukkan Bulan : "))
hari1 = int(input("Masukkan Hari: "))
tahun1 = int(input("Masukkan Tahun: "))

print(f'''{18*"-"}
WAKTU TANGGAL KE 2
{18*"-"}''')

bulan2 = int(input("Masukkan Bulan : "))
hari2 = int(input("Masukkan Hari : "))
tahun2 = int(input("Masukkan Tahun: "))


SETAHUN_SEBULAN = int(365*12)

if tahun1<tahun2:
    tahun = int(tahun2-tahun1)
elif tahun1>tahun2:
     tahun = int(tahun1-tahun2)

if bulan1<bulan2:
    bulan = int(bulan2 - bulan1)
elif bulan1>bulan2:
    bulan = int(bulan1-bulan2)

if hari1<hari2:
    hari = int(hari2-hari1)
elif hari1>hari2:
    hari = int(hari1-hari2)

print(f'''TANGGAL KE 1: {bulan1}/{hari1}/{tahun1}
TANGGAL KE 2: {bulan2}/{hari2}/{tahun2}''')

print(f'''Selisih kedua buah tanggal tersebut adalah {tahun} tahun {bulan} bulan, {hari} hari''')