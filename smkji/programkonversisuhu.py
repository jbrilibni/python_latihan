print('='*40)
print('PROGRAM KONVERSI SUHU')
print('='*40)

suhu = int(input('masukkan suhu (dalam celcius):  '))

fahrenheit = 5/9 * (suhu - 32)
reamur = 4/5 * suhu
kelvin = suhu + 273

print(f'fahrenheit{fahrenheit}: ')
print(f'reamur{reamur}: ')
print(f'kelvin{kelvin}: ')