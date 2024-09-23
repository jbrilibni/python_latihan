print('\033[78m==========SELAMAT DATANG DI TOKO ALAT TULIS==========')
harga_buku = 5000
harga_penghapus = 1000
harga_pulpen = 3000
harga_pensil = 2000
harga_serutan = 4000
harga_spidol = 2000
harga_penggaris = 3000

buku = int(input('ingin membeli berapa buku?: '))
penghapus = int(input('ingin membeli berapa penghapus?: '))
pulpen = int(input('ingin membeli berapa pulpen?: '))
pensil = int(input('ingin membeli berapa pensil?: '))
serutan = int(input('ingin membeli berapa serutan?: '))
spidol = int(input('ingin membeli berapa spidol?: '))
penggaris = int(input('ingin membeli berapa penggaris?: '))

jml_buku = harga_buku*buku
jml_penghapus = harga_penghapus*penghapus
jml_pulpen = harga_pulpen*pulpen
jml_pensil = harga_pensil*pensil
jml_serutan = harga_serutan*serutan
jml_spidol = harga_spidol*spidol
jml_penggaris = harga_penggaris*penggaris
total = jml_buku+jml_penghapus+jml_pulpen+jml_pensil+jml_serutan+jml_spidol+jml_penggaris

diskon = total*12.5/100
jumlah = total-diskon

print('\033[34mjumlah: ',total)
print('\033[34mdiskon: ', diskon)
print('harus bayar: ',jumlah)