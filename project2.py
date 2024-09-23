print("Selamat datang di ATM saya")
print("Pilih Option : ")
print("1. cek uang saya")
print("2. ambil uang saya")
print("3. tabung uang saya")
option=int(input("silahkan pilih option :"))
uang_kamu=300000
if option==1:
    print("uang kamu berjumlah RP.300.000")
elif option==2:
      print("uang kamu berjumlah RP.300.000, mau ambil berapa?")
      print("1. RP.200.000")
      print("2. RP.300.000")
      option2=int(input("option :"))
      if option2==1:
        hasil=uang_kamu-200000
        print("uang kamu sekarang berjumlah :",hasil)
      elif option2==2:
        hasil2=uang_kamu-300000
        print("uang kamu sekarang berjumlah :",hasil2)
      else:
        print("keyword anda salah!")
elif option==3:
    print("uang berjumlah RP.300.000, mau nabung berapa?")
    option3=int(input("masukkan jumlah uang :"))
    hasil3=uang_kamu+option3
    print("jumlah uang kamu sekarang adalah ",hasil3)
else:
    print("keyword anda salah, mohon coba lagi!") 
    