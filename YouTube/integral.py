# Problems (Integral only and with limit):
# 1. \lim_{x\rightarrow0}\int{\frac{x\sin{\left(5x\right)}}{\tan^2{\left(2x\right)}}}=\frac{5}{4}=\frac{5}{4}
# 2. \lim_{x\rightarrow0}\int{\frac{-4x^2+12x}{\sin{\left(4x\right)}}}=3=3
# 3. \lim_{x\rightarrow0}\int{\frac{-\cos{\left(3x\right)}+\cos{\left(7x\right)}}{\cos{\left(4x\right)}-1}}=\frac{5}{2}=\frac{5}{2}
# 4. \lim_{x\rightarrow0}\int{\frac{5x^2-10x}{\sin{\left(5x\right)}}}=-2=-2
# 5. \lim_{x\rightarrow\infty}\int\frac{\left(1-x^2\right)\left(3x+2\right)}{x^2\left(x+5\right)+3}=-3=-3

# Bonuses:
# \int_{0}^{\frac{\pi}{2}}\frac{\sqrt[3]{\tan\ x}}{\left(\sin{x}+\cos{x}\right)^2}
# \int_{-2}^{2}{\left(x^3\cos{\frac{x}{2}}+\frac{1}{2}\right)\sqrt{4-x^2}}dx

import time
from sympy import symbols, sin, cos, tan, integrate, diff, limit, latex, sqrt, cbrt, pi, oo

def main():
    x = symbols('x')
    
    expr = [
        # No. 1
        [
            # f(x) = x\sin{\left(5x\right)}
            x*sin(5*x),
            
            # g(x) = \tan^2{\left(2x\right)}
            tan(2*x)**2,
            
            # H(x) = \frac{x\sin{\left(5x\right)}}{\tan^2{\left(2x\right)}}
            (x*sin(5*x))/(tan(2*x)**2)
        ],
        
        # No.2
        [
            # f(x) = -4x^2+12x
            -4*x**2+12*x,
            
            # g(x) = \sin{\left(4x\right)}
            sin(4*x),
            
            # H(x) = \frac{-4x^2+12x}{\sin{\left(4x\right)}}
            (-4*x**2+12*x)/(sin(4*x))
        ],
        
        # No. 3
        [
            # f(x) = -\cos{\left(3x\right)}+\cos{\left(7x\right)}
            -cos(3*x)+cos(7*x),                             #type: ignore
            
            # g(x) = \cos{\left(4x\right)}-1
            cos(4*x)-1,                                     #type: ignore
            
            # H(x) = \frac{-\cos{\left(3x\right)}+\cos{\left(7x\right)}}{\cos{\left(4x\right)}-1}
            (-cos(3*x)+cos(7*x))/(cos(4*x)-1)               #type: ignore
        ],
        
        # No. 4
        [
            # f(x) = 5x^2-10x
            5*x**2 - 10*x,
            
            # g(x) = \sin{\left(5x\right)}
            sin(5*x),
            
            # H(x) = \frac{5x^2-10x}{\sin{\left(5x\right)}}
            (5*x**2 - 10*x)/(sin(5*x))
        ],
        
        # No. 5
        [
            # f(x) = \left(1-x^2\right)\left(3x+2\right)
            (1 - x**2)*(3*x + 1),
            
            # g(x) = x^2\left(x+5\right)+3
            x**2 * (x + 5) + 3,
            
            # H(x) = \frac{\left(1-x^2\right)\left(3x+2\right)}{x^2\left(x+5\right)+3}
            ((1 - x**2)*(3*x + 1))/(x**2 * (x + 5) + 3)
        ]
    ]
    
    # For loop to access all expressions
    # Also to numerize, so that we're not confused
    for no, i in enumerate(expr):
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
                result = integrate(j, x)
                # Stop timer
                end = time.time()
                # Calculate timer
                elapsed = (end - start) * 1000
                
                # Show result adn time
                print(f"\u222B f(x) dx = {result}\t[{elapsed:.2F} ms]\n")
            
            # The g(x)
            elif id == 1:
                # Show g(x)
                print(f"g(x) = {j}")
                
                # Start timer
                start = time.time()
                # INTEGRATE!!
                result = integrate(j, x)
                # Stop timer
                end = time.time()
                # Calculate timer
                elapsed = (end - start) * 1000
                
                # Show result adn time
                print(f"\u222B g(x) dx = {result}\t[{elapsed:.2F} ms]\n")
            
            # The H(x)
            elif id == 2:
                # Show H(x)
                print(f"H(x) = {j}")
                
                # Start timer
                start = time.time()
                # INTEGRATE!!
                result = integrate(j, x)
                # Stop timer
                end = time.time()
                # Calculate timer
                elapsed = (end - start) * 1000
                
                # Show result adn time
                print(f"\u222B H(x) dx = {result}\t[{elapsed:.2F} ms]\n")
                
            
    expr_bonus = [
        # No. 1
        [
            # \int_{0}^{\frac{\pi}{2}}\frac{\sqrt[3]{\tan\ x}}{\left(\sin{x}+\cos{x}\right)^2}
            "MIT Integration Bee 2023 Finals",
            # Main func
            cbrt(tan(x)) / ((sin(x) + cos(x))**2),          #type: ignore
            
            # UB, LB
            pi/2, 0
        ],
        
        # No. 2
        [
            # \int_{-2}^{2}{\left(x^3\cos{\frac{x}{2}}+\frac{1}{2}\right)\sqrt{4-x^2}}dx
            "Integral Wi-Fi password",
            
            # Main func
            (x**3 * cos(x/2) + 1/x) * sqrt(4 - x**2),
            
            # UB, LB
            2, -2
        ]
    ]

    for i in range(len(expr_bonus)):
        
        # Show name
        print(f"{expr_bonus[i][0]}")
        
        # Start timer
        start = time.time()
        # INTEGRATE!!
        result = integrate(expr_bonus[i][1], (x, expr_bonus[i][2], expr_bonus[i][3]))
        # Stop timer
        end = time.time()
        # Calculate timer
        elapsed = (end - start) * 1000
        
        # Result and time
        print(f"{result}\t[{elapsed:.2F} ms]")
    
main()