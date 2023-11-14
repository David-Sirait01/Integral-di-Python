from expr import *
import os, time, gc, winsound as wns
import psutil, warnings_lang as wn, time

gc.collect()

def chk_RamPercent():
    # Mengambil informasi penggunaan RAM
    ram = psutil.virtual_memory()

    # Mengambil persentase RAM yang digunakan
    ram_percent = ram.percent

    return ram_percent

def get_total_ram():
    ram = psutil.virtual_memory()
    total_ram_mb = ram.total / (1024 * 1024)  # Konversi dari byte ke megabyte
    return total_ram_mb

def get_available_ram():
    ram = psutil.virtual_memory()
    available_ram_mb = ram.available / (1024 * 1024)  # Konversi dari byte ke megabyte
    return available_ram_mb

def printmid(text, p=True, color=""):
    # Mendapatkan lebar terminal saat ini
    terminal_width = os.get_terminal_size().columns

    # Menghitung panjang teks yang akan ditampilkan
    text_length = len(text)

    # Menghitung jumlah karakter "-" yang diperlukan untuk mengelilingi teks
    border_length = (terminal_width - text_length - 4) // 2  # 4 adalah untuk tanda "="

    # Membuat garis batas atas
    top_border = "=" * border_length

    # Membuat garis batas bawah
    bottom_border = "=" * (border_length + (text_length % 2))  # Menambahkan satu "=" jika panjang teks ganjil

    # Menampilkan teks di tengah layar dengan batasan atas dan bawah
    content = top_border + f"[{color}{text}{Style.RESET_ALL}]" + bottom_border + "\n"
    if p == True:
        print(content)
        return content
    else:
        return content
    
def main():
    init(autoreset=True)
    
    try:
        printmid(" Integral with Python! ", color=Fore.YELLOW)
        # Beep(2000, 1500)
        wn.german()
        # print(f"{Fore.RED}  WARNING : Integration may took long time to finish")
        # print(f"{Fore.RED}            One Integration may took around 1 minute, depending on")
        # print(f"{Fore.RED}            how complex the expression, specially if it \\frac{{u}}{{v}}\n")
        # Beep(2000, 800)
        # time.sleep(0.5)
        # print(f"{Fore.RED}  WARNING : Some problems may use a lot of memory and CPU runtime,")
        # print(f"{Fore.RED}            make sure no NOT RUN any heavy applications such as games,")
        # print(f"{Fore.RED}            Adbobe Prmiere, and any CPU or RAM demanding apps\n")
        # Beep(2000, 800)
        # time.sleep(0.5)
        # print(f"{Fore.BLUE}  INFO    : Derrivation after integration maybe not the same as ")
        # print(f"{Fore.BLUE}            the base This is likely due to SymPy limitation\n")
        # Beep(2000, 800)
        # time.sleep(0.5)
        # print(f"{Fore.BLUE}  INFO    : Some may showing \"Integral({{expr}})\" this is also ")
        # print(f"{Fore.BLUE}            likely to be SymPy limitation\n")
        
        RAM_REQ = 5*1024
        print("Checking RAM ", end="")
        for i in range(3):
            print(". ", end="")
            time.sleep(0.8)
        ram_av = get_total_ram()
        if ram_av < RAM_REQ:
            cn = input(f"\n{Fore.RED} WARNING : RAM usage is over limit, continue?\n Available: {ram_av}\n Required: {RAM_REQ}\n Continue? {Fore.RESET}[y/n]\n> ")
            if cn in ("Y", "y"):
                pass
            elif cn in ("N", "n"):
                print("\nExiting now ", end="")
                for i in range(3):
                    print(". ", end="")
                    time.sleep(0.8)
                exit(0)
        else:
            time.sleep(0.2)
            print(f"{Fore.BLUE}RAM OK! {Fore.YELLOW}[ {get_available_ram():.2F} MB Available @ {time.ctime()}]")
                
        time.sleep(1)
        print("\nStarting ", end="")
        for i in range(3):
            print(". ", end="")
            time.sleep(0.8)
            
        time.sleep(1)
        print("\n\n")
        for n, i in enumerate(expr):
            # Initialisation variables to avoid unbounds
            fx_diff = None
            gx_diff = None
            hx_diff = None
            fx_int = None
            gx_int = None
            hx_int = None
            
            start = None
            end = None
            elapsed = None
            
            # # For LaTeX
            # fx_diff_tx = None
            # gx_diff_tx = None
            # hx_diff_tx = None
            # fx_int_tx = None
            # gx_int_tx = None
            # hx_int_tx = None
            try:
                print(f"\n{Fore.YELLOW}No. {n+1}")
                print("Base: ")
                for id, j in enumerate(i):
                    for k in j:
                        if id == 0:
                            print(f" f(x) = {Fore.LIGHTRED_EX} {k}")
                        if id == 1:
                            print(f" g(x) = {Fore.GREEN} {k}")
                        if id == 2:
                            print(f" H(x) = {Fore.CYAN} {k}")
                    
                Beep(2000, 400)
                Beep(2000, 400)
                print("\nIntegrate: ")
                for id, j in enumerate(i):
                    for k in j:
                        if id == 0:
                            print(f" f(x) = ", end="")
                            start = time.time()
                            fx_int = integrate(k, x)
                            end = time.time()
                            elapsed = (end - start)*1000
                            print(f" {Fore.LIGHTRED_EX} {fx_int}\t{Fore.YELLOW}[{elapsed:.2F} ms]")
                        if id == 1:
                            print(f" g(x) = ", end="")
                            start = time.time()
                            gx_int = integrate(k, x)
                            end = time.time()
                            elapsed = (end - start)*1000
                            print(f" {Fore.GREEN} {gx_int}\t{Fore.YELLOW}[{elapsed:.2F} ms]")
                        if id == 2:
                            print(f" H(x) = ", end="")
                            start = time.time()
                            hx_int = integrate(k, x)
                            end = time.time()
                            elapsed = (end - start)*1000
                            print(f" {Fore.CYAN} {hx_int}\t{Fore.YELLOW}[{elapsed:.2F} ms]")
                # print(f"{elapsed} ms")

                Beep(2000, 400)
                Beep(2000, 400)
                print("\nDiff from integrated: ")
                for id, j in enumerate(i):
                    for k in j:
                        if id == 0:
                            fx_diff = diff(fx_int, x)
                            print(f" f(x) = {Fore.LIGHTRED_EX} {fx_diff}")
                        if id == 1:
                            gx_diff = diff(gx_int, x)
                            print(f" g(x) = {Fore.GREEN} {gx_diff}")
                        if id == 2:
                            hx_diff = diff(gx_int, x)
                            print(f" H(x) = {Fore.CYAN} {hx_diff}")
                
                
                # Free up memory after integrating and derivating
                del fx_int, gx_int, hx_int
                del fx_diff, gx_diff, hx_diff
                # del fx_int_tx, gx_int_tx, hx_int_tx
                # del fx_diff_tx, gx_diff_tx, hx_diff_tx
                gc.collect()
                
            except MemoryError or KeyboardInterrupt as e:
                try:
                    wns.MessageBeep(wns.MB_ICONHAND)
                    print(f"\n{Fore.RED} Operation Canceled! {str(e)}\a")
                    n = n+1
                    break
                    # continue
                except MemoryError as e:
                    wns.MessageBeep(wns.MB_ICONEXCLAMATION)
                    print(f"\n{Fore.RED}Fatal Error! {str(e)}")
                    break
    except KeyboardInterrupt:
        wns.MessageBeep(wns.MB_ICONEXCLAMATION)
        print("\n\nExiting now ", end="")
        for i in range(3):
            print(". ", end="")
            time.sleep(0.8)
        exit(code=1)
    
main()