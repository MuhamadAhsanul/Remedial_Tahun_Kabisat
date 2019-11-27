'''
Diketahui

Tahun Kabisat
365 Hari
'''

Year = int(input('Insert tahun : '))

def KabisatYear(x):
    if x % 400 == 0:
        ck = "'TAHUN KABISAT'"
    else:
        if x % 100 == 0:
            ck = "'BUKAN TAHUN KABISAT'"
        else:
            if x % 4 == 0:
                ck = "'TAHUN KABISAT'"
            else:
                ck = "'BUKAN TAHUN KABISAT'"
    return ck
result = KabisatYear(Year)

print(f'Hasil : {result}')