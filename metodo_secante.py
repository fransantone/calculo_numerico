from math import *
import sympy as sp

def secante():
    x = sp.symbols('x')
    func_str = input("Ingrese la función en x: ")
    try:
        f_expr = sp.sympify(func_str,locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,"sin": sp.sin, "cos": sp.cos, "tan": sp.tan,"pi": sp.pi, "E": sp.E, "e": sp.E})
    except Exception as e:
        print(f"Función inválida: {e}")
        return
    f = sp.lambdify(x, f_expr, "math")
    x1 = int(input("Ingrese el valor de x1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    tol = float(input("Ingrese el valor de la tolerancia: "))
    error = 1e3
    n = 0
    x3 = 0
    while error > tol:
        x3 = x1 - ((x2 - x1)/(f(x2)-f(x1)))*f(x1)
        print(f"Iteración {n+1}: intervalo [{x1:.6f}, {x2:.6f}]")
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n = n + 1
        print(f"X -> {n} = {x3}")
    print("============================")
    print(f"X -> {n} = {x3} es una aproximacion valida de la raiz")

secante()
    
