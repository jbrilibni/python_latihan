HARI_PERTAHUN = 365
HARI_PERBULAN = 30
hari = int(input('hari : '))
tahun = int(hari / HARI_PERTAHUN)
hari = hari % HARI_PERTAHUN
bulan = int(hari / HARI_PERBULAN)
sisa_hari = hari % HARI_PERBULAN
bulan = int(hari/ 30)
hari = hari % 30

print(tahun, 'tahun',bulan, 'bulan',hari, 'hari')