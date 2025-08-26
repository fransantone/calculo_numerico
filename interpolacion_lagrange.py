import numpy as np
import sympy as sp

def lagrange_grado_1 (x, x0, x1, y0, y1):
    lx0 = (x-x1)/(x0-x1)
    lx1 = (x-x0)/(x1-x0)
    fx = y0 * lx0 + y1 * lx1
    return fx

def lagrange_grado_2 (x, x0, x1, x2, y0, y1, y2):
    lx0 = ((x - x1) * (x - x2)) / ((x0 - x1) * (x0 - x2))
    lx1 = ((x - x0) * (x - x2)) / ((x1 - x0) * (x1 - x2))
    lx2 = ((x - x0) * (x - x1)) / ((x2 - x0) * (x2 - x1))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2
    return fx

def lagrange_grado_3 (x, x0, x1, x2, x3, y0, y1, y2, y3):
    lx0 = ((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
    lx1 = ((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))
    lx2 = ((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))
    lx3 = ((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2 + y3 * lx3
    return fx

def lagrange_grado_4 (x, x0, x1, x2, x3, x4, y0, y1, y2, y3, y4):
    lx0 = ((x - x1) * (x - x2) * (x - x3) * (x - x4)) / ((x0 - x1) * (x0 - x2) * (x0 - x3) * (x0 - x4))
    lx1 = ((x - x0) * (x - x2) * (x - x3) * (x - x4)) / ((x1 - x0) * (x1 - x2) * (x1 - x3) * (x1 - x4))
    lx2 = ((x - x0) * (x - x1) * (x - x3) * (x - x4)) / ((x2 - x0) * (x2 - x1) * (x2 - x3) * (x2 - x4))
    lx3 = ((x - x0) * (x - x1) * (x - x2) * (x - x4)) / ((x3 - x0) * (x3 - x1) * (x3 - x2) * (x3 - x4))
    lx4 = ((x - x0) * (x - x1) * (x - x2) * (x - x3)) / ((x4 - x0) * (x4 - x1) * (x4 - x2) * (x4 - x3))
    fx = y0 * lx0 + y1 * lx1 + y2 * lx2 + y3 * lx3 + y4 * lx4
    return fx

def leer_grado():
    while True:
        try:
            g = int(input("Seleccione el grado que desea [1,2,3,4]: "))
            if g in (1,2,3,4):
                return g
            print("ERROS! Ingrese 1, 2, 3 o 4.")
        except ValueError:
            print("ERROR! Ingrese un número válido.")

def leer_nodos(n):
    x_nodos = []
    for i in range(n+1):
        x_nodos.append(float(input(f"Ingrese el valor de x{i}: ")))
    if len(set(x_nodos)) != len(x_nodos):
        raise ValueError("ERROR! Los nodos deben ser distintos.")
    return x_nodos

def preguntar_funcion():
    r = input("Tenés f(x) para calcular los valores correspondientes automáticamente? [si/no]: ").strip().lower()
    return r == 'si'

def parsear_funcion(func_str):
    x = sp.symbols('x')
    loc = {"x": x, "sin": sp.sin, "sen": sp.sin, "cos": sp.cos, "tan": sp.tan, "exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt, "pi": sp.pi, "e": sp.E, "E": sp.E}
    f_expr = sp.sympify(func_str, locals=loc)
    funcion =sp.lambdify(x, f_expr, "math")
    return funcion

def leer_y(n):
    f_x_y = []
    for i in range(n+1):
        f_x_y.append(float(input(f"Ingrese y{i}: ")))
    return f_x_y

def leer_x_eval():
    s = input("Ingrese el/los punto(s) a evaluar (separados por coma si son varios): ").strip()
    if "," in s:
        return [float(v) for v in s.split(",")]
    x_puntos = [float(s)]
    return x_puntos

def main():
    print("\n=== Interpolación de Lagrange ===\n")
    grado = leer_grado()
    n = grado

    print(f"\nIngrese {n+1} nodos:")
    xs = leer_nodos(n)

    if preguntar_funcion():
        func_str = input("Ingrese f(x): ")
        f = parsear_funcion(func_str)
        ys = [f(xi) for xi in xs]
        print("y_i calculados:", ys)
    else:
        ys = leer_y(n)

    xe = leer_x_eval()

    print("\n--- Resultados ---")
    for xv in xe:
        if grado == 1:
            x0,x1 = xs; y0,y1 = ys
            print(f"P({xv}) =", lagrange_grado_1(xv, x0,x1, y0,y1))
        elif grado == 2:
            x0,x1,x2 = xs; y0,y1,y2 = ys
            print(f"P({xv}) =", lagrange_grado_2(xv, x0,x1,x2, y0,y1,y2))
        elif grado == 3:
            x0,x1,x2,x3 = xs; y0,y1,y2,y3 = ys
            print(f"P({xv}) =", lagrange_grado_3(xv, x0,x1,x2,x3, y0,y1,y2,y3))
        elif grado == 4:
            x0,x1,x2,x3,x4 = xs; y0,y1,y2,y3,y4 = ys
            print(f"P({xv}) =", lagrange_grado_4(xv, x0,x1,x2,x3,x4, y0,y1,y2,y3,y4))

if __name__ == "__main__":
    main()