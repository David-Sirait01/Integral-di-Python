from sympy import symbols, sin, cos, tan, diff, limit, integrate, pi, latex
from colorama import init, Fore
import time

def main():
    init(autoreset=True)
    x = symbols('x')
    expr = [
        # No. 1
        [
            # f(x) = x\sin{\left(5x\right)}
            x*sin(5*x),                                     # type: ignore
            
            # g(x) = \tan^2{\left(2x\right)}
            tan(2*x)**2,                                    # type: ignore
            
            # H(x) = \frac{x\sin{\left(5x\right)}}{\tan^2{\left(2x\right)}}
            (x*sin(5*x))/(tan(2*x)**2)                      # type: ignore
        ],
        # No. 5
        [
            # f(x) = \left(1-x^2\right)\left(3x+2\right)
            (1 - x**2)*(3*x + 1),                           # type: ignore
            
            # g(x) = x^2\left(x+5\right)+3
            x**2 * (x + 5) + 3,                             # type: ignore
            
            # H(x) = \frac{\left(1-x^2\right)\left(3x+2\right)}{x^2\left(x+5\right)+3}
            ((1 - x**2)*(3*x + 1))/(x**2 * (x + 5) + 3)     # type: ignore
        ]
    ]
    
    # Declare blank variable, to avoid unbounds
    result_fx = None
    result_gx = None
    result = None

    # For loop to access all expressions
    # Also to numerize, so that we're not confused
    for no, i in enumerate(expr):
        try:
            # Show where we are
            print(f"No. {no+1}")
            
            # Same as before, numerize and access
            for id, j in enumerate(i):
                # The f(x)
                if id == 0:
                
                    # Show f(x)
                    print(f"f(x) = {j}")
                    
                    # Start timer
                    start = time.time()
                    
                    # INTEGRATE!!
                    exp = integrate(j, x)
                    # Find limits approx to pi/2
                    result_fx = limit(exp, x, pi/2)
                    
                    # Stop timer
                    end = time.time()
                    # Calculate timer
                    elapsed = (end - start) * 1000
                    
                    # Show result_fx and time
                    print(f"{Fore.RED}lim(x, pi/2) \u222B f(x) dx = {result_fx}\t[{elapsed:.2F} ms]\n{Fore.LIGHTRED_EX}{latex(result_fx)}\n")
                
                # The g(x)
                elif id == 1:
                    # Show g(x)
                    print(f"g(x) = {j}")
                    
                    # Start timer
                    start = time.time()
                    
                    # INTEGRATE!!
                    exp = integrate(j, x)
                    # Find limits approx to pi/2
                    result_gx = limit(exp, x, pi/2)
                    
                    # Stop timer
                    end = time.time()
                    # Calculate timer
                    elapsed = (end - start) * 1000
                    
                    # Show result_gx and time
                    print(f"{Fore.GREEN}lim(x, pi/2) \u222B g(x) dx = {result_gx}\t[{elapsed:.2F} ms]\n{Fore.LIGHTGREEN_EX}{latex(result_gx)}\n")
                
                # The H(x)
                elif id == 2:
                    # Show H(x)
                    print(f"H(x) = {j}")
                    
                    # Start timer
                    start = time.time()
                    
                    # INTEGRATE!!
                    exp = result_fx/result_gx       # type: ignore
                    # Find limits approx to pi/2
                    result = limit(exp, x, pi/2)
                    
                    # Stop timer
                    end = time.time()
                    # Calculate timer
                    elapsed = (end - start) * 1000
                    
                    # Show result and time
                    print(f"{Fore.BLUE}lim(x, pi/2) \u222B H(x) dx = {result}\t[{elapsed:.2F} ms]\n{Fore.LIGHTBLUE_EX}{latex(result)}\n")
        except KeyboardInterrupt:
            exit(1)
                
main()

# Results
# No.1 
# \lim_{x\rightarrow0}{\frac{\frac{1}{25}}{-\frac{\pi}{2}}}=-\frac{2}{25\pi}
# No.2 
# \lim_{x\rightarrow\frac{\pi}{2}}\frac{-\frac{3\pi^4}{64}-\frac{\pi^3}{24}+\frac{\pi}{2}+\frac{3\pi^2}{8}}{\frac{\pi^4}{64}+\frac{3\pi}{2}+\frac{5\pi^3}{24}}=\frac{-\frac{3\pi^4}{64}-\frac{\pi^3}{24}+\frac{\pi}{2}+\frac{3\pi^2}{8}}{\frac{\pi^4}{64}+\frac{3\pi}{2}+\frac{5\pi^3}{24}}