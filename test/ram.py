# import psutil

def chk_RamPercent():
    # Mengambil informasi penggunaan RAM
    ram = psutil.virtual_memory()

    # Mengambil persentase RAM yang digunakan
    ram_percent = ram.percent

    return ram_percent

# # Memanggil fungsi dan mencetak persentase RAM yang digunakan
# ram_percent = chk_RamPercent()
# print(f"Persentase RAM yang digunakan: {ram_percent}%")

import psutil, time
from colorama import init, Fore

init(autoreset=True)

def get_available_ram():
    ram = psutil.virtual_memory()
    available_ram_mb = ram.available / (1024 * 1024)  # Konversi dari byte ke megabyte
    return available_ram_mb

# Memanggil fungsi dan mencetak RAM yang tersedia dalam MB
while True:
    available_ram = chk_RamPercent()
    if available_ram < 30.0:
        print(f"Available RAM [MB]: {Fore.BLUE} {available_ram:.2F}", end="\r")
    elif 74.9 > available_ram > 30.0:
        print(f"Available RAM [MB]: ~ {Fore.YELLOW} {available_ram:.2F}", end="\r")
    elif available_ram > 75.0:
        print(f"Available RAM [MB]: ! {Fore.RED} {available_ram:.2F}", end="\r")
    time.sleep(0.1)