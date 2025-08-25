# Importamos las librerias math y sympy para utilizar la nomenclatura tecnica de matematica y que se entienda al escribir en consola y realizar las cuentas
from math import *
import sympy as sp

def biseccion():
    # Definimos la variable X como un simbolo matematico para poder utilizar a futuro
    x = sp.symbols('x')
    func_str = input("Ingrese la función en x: ")
    try:
        # Habilitamos utilizar terminologia especifica somo "seno" y demas para que se interprete desde la consola y asi realizar calculos a futuro
        f_expr = sp.sympify(func_str,locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,"sin": sp.sin, "cos": sp.cos, "tan": sp.tan,"pi": sp.pi, "E": sp.E, "e": sp.E})
    except Exception as e:
        print(f"Función inválida: {e}")
        return
    
    # Convertimos la funcion simbolica en una funcion que sea interpretada por python
    f = sp.lambdify(x, f_expr, "math")
    f_np = sp.lambdify(x, f_expr, "numpy") #funcion que me permite graficar
    num = lambda msg: float(sp.sympify(msg, locals={"pi": sp.pi, "E": sp.E, "e": sp.E, "sqrt": sp.sqrt}))

    # Solicitamos los valores de x0, x1 y tolerancia
    a = num(input("Ingrese el valor de A: "))
    b = num(input("Ingrese el valor de B: "))
    tol = float(sp.sympify(input("Ingrese el valor de la tolerancia: ")))
    m1 = a
    m = b
    k = 0

    # Realizamos las cuentas para cada intervalo y mostramos por consola los intervalos con las raices
    if (f(a)*f(b)>0):
        print("La funcion no cambia de signo")
    while(abs(m1-m)>tol):
        m1 = m
        m = (a+b)/2
        if(f(a)*f(m)<0):
            b = m
        if(f(m)*f(b)<0):
            a = m 
        print(f"x0 = {a} | x1 = {b}]")
        k = k+1
    print (f"X -> {k} = {m} es una buena aproximacion como raiz")

def iteraciones():
    # Recibimos del usuario los valores de x0, x1 y tolerancia
    x0 = int(input("Ingrese el valor de x0: "))
    x1 = int(input("Ingrese el valor de x1: "))
    tol = float(sp.sympify(input("Ingrese el valor de la tolerancia: ")))

    # Calculamos el log en base 2 de la division entre la diferencia de x1 - x0 sobre la tolerancia
    diferencia = abs(x1 - x0)
    n = sp.log(diferencia/tol, 2)

    # Redondeamos para arriba
    cantidad_iteraciones = int(sp.ceiling(n))
    print(f"Cantidad de iteraciones necesarias = {cantidad_iteraciones}")
    return 

# Ejecutamos el codigo con un menu para calcular la raiz aproximada de una funcion o la cantidad de iteraciones necesarias
if __name__ == "__main__":
    while True:
        while True:
            try:
                opcion = int(input("Seleccione qué desea calcular -> [1] Cantidad Iteraciones | [2] Raíces | [0] Salir: "))
                if opcion in (1, 2, 0):
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")
            except ValueError:
                print("Debe ingresar un número (1 | 2 | 0). Intente de nuevo.")
        if opcion == 1:
            iteraciones()
        elif opcion == 2:
            biseccion()
        elif opcion == 0:
            break