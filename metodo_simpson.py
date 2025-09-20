import sympy as sp

def nodos(a, n, h):
    xs = []
    for i in range (n+1):
        xi = a + i * h
        xs.append(xi)
    return xs

def integral_simpson(f, a, b):
    xi = (a + b)/2
    simpson_simple = ((b-a)/6) * (f(a) + f(b) + (4 * f(xi)))
    return simpson_simple

def integral_simpson_compuesta (f, a, n, h):
    xs = nodos(a, n, h)
    simpson = f(xs[0]) + f(xs[-1])
    for i in range (1,n):
        simpson = simpson + 2 * f(xs[i])
    xm = []
    for i in range (0,n):
        xmi = (xs[i] + xs[i+1]) / 2
        xm.append(xmi)
    for i in range (0, n):
        simpson = simpson + 4 * f(xm[i])
    resultado_final = (h/6) * simpson
    return resultado_final

def main():
    a = float(input("Ingrese el valor de A: "))
    b = float(input("Ingrese el valor de B: "))
    n = int(input("Ingrese el valor de N: "))
    if n <= 1 or n % 2 != 0:
        raise ValueError("n debe ser positiva y par")
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
    if n == 2:
        smp = integral_simpson(f_num, a, b)
        print("======= Resultados =======")
        print (f"Intervalo: {a} ; {b} | con {n} subintervalos")
        print(f"Integral de f(x) por simpson: {smp}")
    else:
        smp_compuesta = integral_simpson_compuesta(f_num, a, n, h)
        print("======= Resultados =======")
        print (f"Intervalo: {a} ; {b} | con {n} subintervalos")
        print(f"Integral de f(x) por simpson compuesta: {smp_compuesta}")

if __name__ == "__main__":
    main()