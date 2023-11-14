import time
from colorama import init, Fore
from sympy import symbols, sin, tan, integrate, limit, latex

def convert_to_letter(number):
    if isinstance(number, int):
        if 1 <= number <= 26:
            return chr(ord('a') + number - 1)
        else:
            return None
    elif isinstance(number, tuple) or isinstance(number, list):
        result = []
        for num in number:
            if 1 <= num <= 26:
                result.append(chr(ord('a') + num - 1))
            else:
                result.append(None)
        return result
    else:
        return None
    

init(autoreset=True)
def main():
    x = symbols("x")
    expr = [
        # f(x) = x\sin{\left(5x\right)}
        x*sin(5*x),
            
        # g(x) = \tan^2{\left(2x\right)}
        tan(2*x)**2
    ]
    
    # print(f"{Fore.YELLOW}Integral && Limit on Python!")
    print(f"{Fore.YELLOW}~ $ {Fore.RESET}main.py")
    
    result = []
    # \lim_{x \rightarrow 0}\frac{\int x \sin{\left(5 x \right)} dx}{\int \tan^{2}{\left(2 x \right)} dx} = \lim_{x \rightarrow 0}\frac{- \frac{x \cos{\left(5 x \right)}}{5} + \frac{\sin{\left(5 x \right)}}{25}}{- x + \frac{\sin{\left(2 x \right)}}{2 \cos{\left(2 x \right)}}}=\frac{5}{4}
    
    for n, i in enumerate(expr):
        start = time.time()
        
        # print(f"\n{convert_to_letter(n+1)} = {Fore.GREEN}\u222B {i} dx\n    {latex(i)} dx", end="\n  = ")
        print(f"\n{convert_to_letter(n+1)} = {Fore.GREEN}\u222B {i} dx", end="\n  = ")
        result.append(integrate(i))
        
        end = time.time()
        elapsed = (end - start) * 1000
        
        # print(f"{Fore.BLUE}{result[n]}\n    {latex(result[n])}")
        print(f"{Fore.BLUE}{result[n]}\t  [{elapsed:.2F} ms]")
    
    print("\n")
    lim_exp = result[0]/result[1]
    h = 0
    
    start = time.time()
    lim = limit(lim_exp, x, h)
    end = time.time()
    elapsed = (end - start) * 1000
    
    print(f"{Fore.GREEN}lim(x, 0) a/b = {Fore.BLUE}{lim}\t\t  {Fore.RED}[{elapsed:.2F} ms]\n\n")
    
main()