import math
import sympy as sp

def nodos(a, n, h):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    xs = []
    for i in range(n + 1):
        xi = a + i * h
        xs.append(xi)
    return xs

def integral_trapecio (f, a, b, n, h):
    xs = nodos(a, n, h)   
# esto seria la parte del trapecio que suma f(x0) + f(xn)
    s = f(xs[0]) + f(xs[-1])
# esto seria la parte de 2 * la sumatoria de f(xi) hasta f(xn-1)
    for i in range (1,n):
        s = s + 2 * f(xs[i])
    resultado_final = (h/2) * s
    return resultado_final

#Cota teotrica del error
def error_trapecio_en_base_n(n, a, b, f_expr):
    x = sp.Symbol('x')
    segunda_derivada_f = sp.diff(f_expr, x, 2)
    segunda_derivada_python = sp.lambdify(x, segunda_derivada_f, "math")
    m2 = max(abs(segunda_derivada_python(a)), abs(segunda_derivada_python(b)))
    L = abs(b - a)
    error = (L**3 * m2) / (12 * n**2) 
    return error

def main():
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    n = int(input("Ingrese el valor de N: "))
    funcion = input("Ingrese f(x) a evaluar: ")
    try:
        x = sp.Symbol('x')
# Habilitamos utilizar terminologia especifica somo "seno" y demas para que se interprete desde la consola y asi realizar calculos a futuro
        f_expr = sp.sympify(funcion,locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,"sin": sp.sin, "cos": sp.cos, "tan": sp.tan,"pi": sp.pi, "E": sp.E, "e": sp.E})
        f_num = sp.lambdify(x, f_expr, "math")
    except Exception as e:
        print(f"Función inválida: {e}")
        return
    h = (b-a)/n
    Tn = integral_trapecio(f_num, a, b, n, h)
    error_esperado = error_trapecio_en_base_n(n,a,b,f_expr)
    print("======= Resultados =======")
    print (f"Intervalo: {a} ; {b} | con {n} subintervalos")
    print(f"Integral de f(x) por trapecio: {Tn}")
    print(f"Cota teorica del error con {n} subintervalos: {error_esperado}")

if __name__ == "__main__":
    main()