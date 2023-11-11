#Ini adalah project kalkulator yang sebelumnya ini adalah update terbaru
#Kau bisa menggunakan project ini di platform manapun :D

import time

main_text = "SELAMAT DATANG DI PROGRAM CALCULATOR V5.0"
width = 80
print("")
print(main_text.center(width))
print("")
print("Yang kamu harus ketahui tentang program ini!")
print("Program ini masih beta dan terdapat banyak kekurangan di program ini semoga kalian mengerti")
print("Untuk saat ini hanya tersedia Pertambahan, pengurangan, Perkalian, Pembagian")
print("Untuk saat ini hanya bisa memasukan 2 angka")
print("")

def main_menu():
    loading_text = "Loading..."
    width = 80
    print(loading_text.center(width))
    print("")
    time.sleep(5)
    print("Menu Calculator: ")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Modulus")
    print("6. Perpangkatan")
    print("7. Pembagian Bulat")
    print("8. Credits")
    print("9. Exit")

def pertambahan():
    
    angka_tam1 = int(input("Masukan angka pertama: "))
    angka_tam2 = int(input("Masukan angka kedua : "))
    hasil_p = angka_tam1 + angka_tam2
    print("")
    print(angka_tam1, "+", angka_tam2, "=", hasil_p )

def pengurangan():
    angka_kur1 = int(input("Masukan angka pertama: "))
    angka_kur2 = int(input("Masukan angka kedua: "))
    hasil_kur = angka_kur1 - angka_kur2
    print("")
    print(angka_kur1, "-", angka_kur2, "=", hasil_kur)

def perkalian():
    angka_kal1 = int(input("Masukan angka pertama: "))
    angka_kal2 = int(input("Masukan angka kedua: "))
    hasil_kal = angka_kal1 * angka_kal2
    print("")
    print(angka_kal1, "*", angka_kal2, "=", hasil_kal)


def pembagian():
    angka_bag1 = int(input("Masukan angka pertama: "))
    angka_bag2 = int(input("Masukan angka kedua: "))
    hasil_bag = angka_bag1 / angka_bag2
    print("")
    print(angka_bag1, "/", angka_bag2, "=", hasil_bag)

def modulus():
    angka_modul1 = int(input("Masukan angka pertama: "))
    angka_modul2 = int(input("Masukan angka kedua: "))
    hasil_modul = angka_modul1 % angka_modul2
    print("")
    print(angka_modul1, "%", angka_modul2, "=", hasil_modul)

def perpangkatan():
    angka_pang1 = int(input("Masukan angka pertama: "))
    angka_pang2 = int(input("Masukan angka kedua: "))
    hasil_pang = angka_pang1 ** angka_pang2
    print("")
    print(angka_pang1, "**", angka_pang2, "=", hasil_pang)

def pembagianbulat():
    angka_bul1 = int(input("Masukan angka pertama: "))
    angka_bul2 = int(input("Masukan angka kedua: "))
    hasil_bul = angka_bul1 // angka_bul2
    print("")
    print(angka_bul1, "//",  angka_bul2, "=", hasil_bul)

def credits():
    print("")
    print("Calculator Created By sgt.Zach Noland")
    print("Calculator is made in Python")
    print("")

while True:
    main_menu()
    selection = input("Pilih (1/2/3): ")
    if selection == "1":
        pertambahan()

    elif selection == "2":
        pengurangan()
    elif selection == "3":
        perkalian()
    elif selection == "4":
        pembagian()
    elif selection == "5":
        modulus()
    elif selection == "6":
        perpangkatan()
    elif selection == "7":
        pembagianbulat()
    elif selection == "8":
        credits()
    elif selection == "9":
        print("Terima kasih karena telah mencoba beta ini. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")