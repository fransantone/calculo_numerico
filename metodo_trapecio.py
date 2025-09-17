import math

def nodos(a, n, h):
    if n <= 0:
        raise ValueError("n debe ser positivo")
    xs = []
    for i in range(n + 1):
        xi = a + i * h
        xs.append(xi)
    return xs

def integral_trapecio (f, a, b, n, h):
    xs = nodos(a, b, n) 
    
    return

if __name__ == "__main__":
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))
    n = int(input("Ingrese el valor de n: "))
    funcion = input("Ingrese f(x) a evaluar")
    h = (b-a)/n
    pass