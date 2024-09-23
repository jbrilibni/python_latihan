print('\033[92m==========================')
print('/   PERCEPATAN RATA-RATA    ')
print('\033[92m--------------------------')

while True:
    v2 = input('masukan kecepatan akhir: ')
    v1 = input('masukan kecepatan awal: ')

    t2 = input('masukan waktu akhir: ')
    t1 = input('\nmasukan waktu awal: ')

    v1v2 = int(v1) - int(v2)
    t1t2 = int(t1) - int(t2)

    hasil = int(v1v2)/int(t1t2)

    print(f'\nhasilnya adalah: {round (hasil)/2} w/s')

    print('hasilnya tidak ada : (')





