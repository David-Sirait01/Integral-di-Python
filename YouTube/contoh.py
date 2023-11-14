from sympy import symbols, sin, cos, tan, diff, integrate, Integral, latex

def main():
    x = symbols("x")
    
    expr = [
        # No Trigonometri (Nomor 1)
        [
            # f(x)
            x*sin(5*x),                         #type: ignore
            
            # g(x)
            tan(2*x)**2,
            
            # H(x)
            (x*(sin(5*x))/(tan(2*x)**2))
        ],
        
        # Dengan Trigonometri (Nomor 3)
        [
            # f(x)
            cos(7*x) - cos(3*x),                #type: ignore
            
            # g(x)
            cos(4*x-1),
            
            # H(x)
            (cos(7*x) - cos(3*x))/(cos(4*x-1))  #type: ignore
        ]
    ]
    
    exp_diff = diff(expr[1][2], x)
    print(f"{expr[1][2]} dy/dx = {exp_diff}")
    
    exp_int = integrate(exp_diff, x)
    print(f"\u222B {exp_diff} = {exp_int}")
    
main()