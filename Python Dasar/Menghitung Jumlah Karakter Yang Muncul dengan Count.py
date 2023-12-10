# Perlu di ingat ini masih pengembangan
# Jadi saya menggabungkan printah dasar menjadi sesuatu yang bagus dan menarik.
# Saya masukan ke python dasar karena semua perintah di sini masih terbilang dasar menurut saya.
# Fakta kalau saya buat projek simpel ini saat gabud hehehe :V

import time

print("")
main_text = "SELAMAT DATANG DI PERINTAH SIMPLE DENGAN COUNT"
width = 80
print(main_text.center(width))

time.sleep(2)

while (1 + 2 == 3):
    print("=======================================================================")
    pertanyaan = (input("Apakah kau ingin mencoba perintah simpel ini (Y/N): "))
    if(pertanyaan == "Y"):
        print("=======================================================================")
        paragraf = (input("Masukan kalimat atau paragraf: "))
        y = (input("Masukan kalimat yang ingin di hitung jumlahnya: "))
        x = paragraf.count(y)
        print("")

        print('Kata/kalimat "', y,f'" muncul {x} kali')
    
    elif(pertanyaan == "N"):
        print("")
        terima_kasih = "Terima kasih, karena sudah mampir :3"
        width = 40
        print(terima_kasih.center(width))
        break
    
    else:
        print("Sintax salah harus masukan huruf besar dan harus sesuai (Y/N)")
        time.sleep(2)






