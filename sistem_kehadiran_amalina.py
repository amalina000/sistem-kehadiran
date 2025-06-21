
# Sistem Kehadiran Ringkas oleh Nur Amalina
import csv

def rekod_kehadiran(nama_fail='kehadiran.csv'):
    nama = input("Masukkan nama pelajar: ")
    with open(nama_fail, mode='a', newline='') as file:
        penulis = csv.writer(file)
        penulis.writerow([nama])
    print(f"Kehadiran untuk {nama} telah direkodkan.")

def paparkan_kehadiran(nama_fail='kehadiran.csv'):
    print("\nSenarai Kehadiran:")
    try:
        with open(nama_fail, mode='r') as file:
            pembaca = csv.reader(file)
            for baris in pembaca:
                print(f"- {baris[0]}")
    except FileNotFoundError:
        print("Tiada rekod kehadiran lagi.")

while True:
    print("\n1. Rekod Kehadiran")
    print("2. Paparkan Kehadiran")
    print("3. Keluar")
    pilihan = input("Pilih menu (1-3): ")

    if pilihan == '1':
        rekod_kehadiran()
    elif pilihan == '2':
        paparkan_kehadiran()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak sah. Sila cuba lagi.")
