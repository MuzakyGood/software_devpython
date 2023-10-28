# Game Simple Python dan sangatlah simple

import time
main_text = "SELAMAT DATANG DI PROGRAM QUIZ BETA"
width = 80
print("")
print(main_text.center(width))
print("")
print("Yang kamu harus ketahui tentang program ini!")
print("Program ini masih beta dan terdapat banyak kekurangan di program ini semoga kalian mengerti")
print("Pilih level secara manual untuk versi beta")
print("Untuk sekarang hanya tersedia 10 level")
print("")
def main_menu():
    loading_text = "Loading..."
    width = 80
    print(loading_text.center(width))
    print("")
    time.sleep(5)
    print("Level Menu: ")
    print("1. Level 1")
    print("2. Level 2")
    print("3. Level 3")
    print("4. Level 4")
    print("5. Level 5")
    print("6. Level 6")
    print("7. Level 7")
    print("8. Level 8")
    print("9. Level 9")
    print("10. Level 10")
    print("")
    print("Extra Menu: ")
    print("11. Credits")
    print("12. Exits")
    
def level_1():
    print("")
    print("Pertanyaan: Apa ibukota Indonesia?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "jakarta":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Jakarta.")
        print("")

def level_2():
    print("")
    print("Pertanyaan: Apa pemrograman yang digunakan program ini?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "python":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Python.")
        print("")

def level_3():
    print("")
    print("Pertanyaan: Unsur terkecil yang tidak dapat di bagi lagi?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "atom":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Atom.")
        print("")

def level_4():
    print("")
    print("Pertanyaan: Python di ciptakan pada tahun?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "1991":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah 1991.")
        print("")

def level_5():
    print("")
    print("Pertanyaan: Siapa presiden rusia saat ini?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "vladimir putin":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Vladimir Putin.")
        print("")
def level_6():
    print("")
    print("Pertanyaan: Untuk apa saya di beta test ini?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "uji coba":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Uji Coba.")
        print("")

def level_7():
    print("")
    print("Pertanyaan: Planet yang memiliki julukan planet merah,yaitu planet?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "mars":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Mars.")
        print("")

def level_8():
    print("")
    print("Pertanyaan: Materi paling langka di dunia ini yaitu?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "materi gelap":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah Materi Gelap.")
        print("")

def level_9():
    print("")
    print("Pertanyaan: Dimana lokasi pulau komodo berada?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "ntt":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah NTT(Nusa Tenggara Timur).")
        print("")

def level_10():
    print("")
    print("Pertanyaan: Siapa pembuat game ini?")
    jawaban = input("Jawaban Anda: ")
    if jawaban.lower() == "sgt.zach noland":
        print("")
        print("Jawaban Anda benar!")
        print("")
    else:
        print("")
        print("Jawaban Anda salah. Jawaban yang benar adalah sgt.Zach Noland.")
        print("")

def show_credits():
    print("")
    print("Game Created By sgt.Zach Noland")
    print("Game is made in Python")
    print("")
    
while True:
    main_menu()
    pilihan = input("Pilih opsi (1/2/3/dll): ")

    if pilihan == "1":
        level_1()
    elif pilihan == "2":
        level_2()
    elif pilihan == "3":
        level_3()
    elif pilihan == "4":
        level_4()
    elif pilihan == "5":
        level_5()
    elif pilihan == "6":
        level_6()
    elif pilihan == "7":
        level_7()
    elif pilihan == "8":
        level_8()
    elif pilihan == "9":
        level_9()
    elif pilihan == "10":
        level_10()
    elif pilihan == "11":
        show_credits()
    elif pilihan == "12":
        print("Terima kasih karena telah mencoba program beta kami, program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

