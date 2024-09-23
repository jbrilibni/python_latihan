barang1 = float(input('barang1: '))
barang2 = float(input('barang2: '))
barang3 = float(input('barang3: '))
barang4 = float(input('barang4: '))

total_belanja = barang1 + barang2 +  barang3 + barang4

print(f'total belanja: {total_belanja:.0f}')

if total_belanja > 300000:
    diskon = total_belanja * 0.075
    total_diskon = total_belanja - diskon
    print(f'diskon: {diskon:.0f}')
    print(f'totall bayar:{total_diskon:.0f}')
else:
    print('tidak terdapat diskon')
    print(f'total belanja: {total_belanja:.0f}') 