username = 'jibrilibnijubair@gmail.com'
password = '12345678911'

USERNAME = input('masukkan username\t: ')
PASSWORD = input('masukkan password\t: ')

if username != USERNAME:
    print('username tidak tersedia')
elif username == USERNAME and PASSWORD != password:
    print('password salah')
else:
    print('selamat datang', username)