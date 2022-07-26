#learning python from kelas terbuka
import os

def header():
    os.system("clear")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'FROM KELAS TERBUKA':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    # Mengambil input user
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang
def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):

    return 2*(lebar+panjang)

def display(message,value):
    print(f"hasil perhitungan {message} = {value}")
# Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")