#Program shortcut simple
#Catatan program ini hanya berfungsi untuk windows atau hanya untuk windows 10 

import time
import subprocess
import os

main_text = "SELAMAT DATANG DI PROGRAM SHORTCUT BETA"
width = 80
print("")
print(main_text.center(width))
print("")
print("Yang kamu harus ketahui tentang program ini!")
print("Program ini masih beta dan terdapat banyak kekurangan di program ini semoga kalian mengerti")
print("Program ini hanya berfungsi untuk pengguna windows")
print("")

def main_menu():
    loading_text = "Loading..."
    width = 80
    print(loading_text.center(width))
    print("")
    time.sleep(5)
    print("Menu Shortcut: ")
    print("1. CMD")
    print("2. This PC")
    print("3. Settings")
    print("4. Documents")
    print("5. Downloads")
    print("6. Notepad")
    print("7. Paint")
    print("8. Calculator")
    print("9. Wifi Password Beta(Only see wifi history)")
    print("10. Credits")
    print("11. Exit")

def prompt_cmd():
    subprocess.call('start cmd /k "dir"', shell=True)

def open_thispc():
    subprocess.Popen('explorer /select,shell:ThisPCFolder', shell=True)
def open_settings():
    subprocess.call('start cmd /c "start ms-settings:"', shell=True)

def show_documents():
    subprocess.Popen('explorer C:/Users/Username/Downloads', shell=True)

def show_downloads():
    subprocess.Popen('explorer shell:Downloads', shell=True)

def show_notepad():
    subprocess.call('start cmd /c "notepad"', shell=True)

def show_paint():
    subprocess.call('start cmd /c "mspaint"', shell=True)

def show_calculator():
    subprocess.call('start cmd /c "calc"', shell=True)

def show_password():
    command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in command if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    
    input("Tekan Enter untuk kembali ke menu...")


def show_credits():
    print("")
    print("Software Created By sgt.Zach Noland")
    print("Software is made in Python")
    print("")

while True:
    main_menu()
    selection = input("Pilih (1/2/3): ")
    if selection == "1":
        prompt_cmd()
    elif selection == "2":
        open_thispc()
    elif selection == "3":
        open_settings()
    elif selection == "4":
        show_documents()
    elif selection == "5":
        show_downloads()
    elif selection == "6":
        show_notepad()
    elif selection == "7":
        show_paint()
    elif selection == "8":
        show_calculator()
    elif selection == "9":
        show_password()
    elif selection == "10":
        show_credits()
    elif selection == "11":
        print("Terima kasih karena telah mencoba beta ini. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih opsi yang benar.")

        
