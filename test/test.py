from sympy import symbols, sin, cos, tan, sqrt, pi, integrate

def main():
    x = symbols('x')
    expr = [
        [
            [(2*sin(5*x))],                                 #type: ignore
            [(tan(2*x)**2)],
            [(x*(sin(5*x))/(tan(2*x)**2))]
        ],
        # [
        #     [((sqrt(x + 1) - sqrt(x))**pi)]                 #type: ignore
        # ]
    ]
    
    for n, i in enumerate(expr):
        fx_diff = None
        gx_diff = None
        hx_diff = None
        fx_int = None
        gx_int = None
        hx_int = None
        
        print(f"\nNo. {n+1}")
        print("\nBase: ")
        for id, j in enumerate(i):
            for k in j:
                if id == 1-1:
                    print(f"f(x) = {k}")
                if id == 2-1:
                    print(f"g(x) = {k}")
                if id == 3-1:
                    print(f"H(x) = {k}")
        
        print("\nIntegrate: ")
        for id, j in enumerate(i):
            for k in j:
                if id == 0:
                    fx_int = integrate(k, x)
                    print(f"f(x) = {fx_int}")
                if id == 1:
                    gx_int = integrate(k, x)
                    print(f"g(x) = {gx_int}")
                if id == 2:
                    hx_int = integrate(k, x)
                    print(f"H(x) = {hx_int}")

    # for i in expr:
    #     print()
    #     for id, k in enumerate(i):
    #         if id == 0:
    #             print(f"f(x) = {k}")
    #         if id == 1:
    #             print(f"g(x) = {k}")
    #         if id == 2:
    #             print(f"H(x) = {k}")
                    
            # for k in range(len(j)):
            #     if k == 0:
            #         print(f"f(x) = {j[k]}")
            #     elif k == 1:
            #         print(f"g(x) = {j[k]}")
            #     elif k == 2:
            #         print(f"H(x) = {j[k]}")
            #     k = k+1

    
    # \frac{x \sin{\left(5 x \right)}}{\tan^{2}{\left(2 x \right)}}
    # expr = ((x * sin(5*x))/(tan(2*x)**2))
    # print(f"y = {latex(expr)}\nIntegrating . . . ")
    # print(f"Base\ny\t= {latex(expr)} ")
    
    # derivated = diff(expr, x)
    # print(f"\nDerivated\ndy/dx\t= {latex(derivated)}")
    
    # integral = integrate(expr, x)
    # print(f"\nIntegrated\n\u222By dx\t= {latex(integral)}")
    
    # integral = integrate(derivated, x)
    # print(f"\nIntegrated\n\u222Bdy/dx\t= {latex(integral)}")
    
    # print(f"\\lim{{x \\rightarrow 0}} {latex(expr_int)} = ")
    # result = limit(expr_int, x, 0)
    # print(f"{result}")
main()

