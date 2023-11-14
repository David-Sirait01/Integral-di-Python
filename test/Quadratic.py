from sympy import symbols, diff, integrate, sin, cos, tan, sqrt, latex
from colorama import init, Fore, Back, Style
import os

init(autoreset=True)

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
    printmid(" diff then intg ! ", color=Fore.YELLOW)
    
    # # Quadratic Equantion
    a, b, c = symbols("a b c")
    expr = (-b+sqrt(b**2-4*a*c))/(2*a)      #type: ignore
    
    # Base
    # x = symbols('x')
    # expr = (2*sin(5*x))*(tan(2*x)**2)**-1 #type: ignore
    
    # LaTeX for base
    print(f"y = {expr}\nLaTeX : {latex(expr)}")
    
    # LaTeX for Integration
    print(f"\n{Fore.BLUE} Integration")
    expr_int = integrate(expr, a)
    print(f"\u222By dx = {expr_int}\nLaTeX : {latex(expr_int)}")
    
    # LaTeX for Darrivative
    print(f"\n{Fore.BLUE} Derrivate")
    expr_diff = diff(expr, a)
    print(f"dy/dx = {expr_diff}\nLaTeX : {latex(expr_diff)}")
    
main()