from sympy import symbols, limit, sin, cos, tan, pi, sqrt, diff, integrate, latex
from winsound import Beep
from colorama import init, Fore, Back, Style

x = symbols('x')
expr = [
    [ 
        # f(x) = x\sin{\left(5x\right)}
        # g(x) = \tan^2{\left(2x\right)}
        # H(x) = \frac{x\sin{\left(5x\right)}}{\tan^2{\left(2x\right)}}
            
        [(2*sin(5*x))],                                  #type: ignore
        [(tan(2*x)**2)],
        [(x*(sin(5*x))/(tan(2*x)**2))]
    ],
    [
        # f(x) = -4x^2+12x
        # g(x) = \sin{\left(4x\right)}
        # H(x) = frac{-4x^2+12x}{\sin{\left(4x\right)}}
        [(-4*x**2 + 12*x)],
        [(sin(4*x))],
        [((-4*x**2 + 12*x)/(sin(4*x)))]
    ],
    [
        # f(x) = x\sin{\left(5x\right)
        # g(x) = \tan^2{\left(2x\right)
        # H(x) = \frac{x\sin{\left(5x\right)}}{\tan^2{\left(2x\right)}}
            
        [(x*sin(5*x))],
        [(tan(2*x)**2)],
        [((x*sin(5*x))/(tan(2*x)**2))]
    ],
    [
        # f(x) = \left(1-x^2\right)\left(3x+2\right)
        # g(x) = x^2\left(x+5\right)+3
        # H(x) = frac{\left(1-x^2\right)\left(3x+2\right)}{x^2\left(x+5\right)+3}
            
        [((1 - x**2)*(3*x+2))],
        [(x**2*(x+5) + 3)],
        [((1 - x**2)*(3*x+2))/(x**2*(x + 5)+3)]  
    ],
    [
        # f(x) = \sin{\left(\frac{7}{x}\right)}+\tan{\left(\frac{3}{x}\right)}
        # g(x) = \sin{\left(\frac{8}{x}\right)}-\tan{\left(\frac{3}{x}\right)}
        # H(x) = frac{\sin{\left(\frac{7}{x}\right)}+\tan{\left(\frac{3}{x}\right)}}{\sin{\left(\frac{8}{x}\right)}-\tan{\left(\frac{3}{x}\right)}}
            
        [(sin(7/x) + tan(3/x))],                        #type: ignore
        [(sin(8/x) - tan(3/x))],                        #type: ignore
        [(sin(7/x) + tan(3/x))/(sin(8/x) - tan(3/x))]   #type: ignore
    ],
    [
        # \int\left(\sqrt{x+1}-\sqrt x\right)^\pi dx
            
        [((sqrt(x + 1) - sqrt(x))**pi)]                 #type: ignore
    ]
]