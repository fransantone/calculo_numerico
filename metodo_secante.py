# Importamos las librerias math y sympy para utilizar la nomenclatura tecnica de matematica y que se entienda al escribir en consola y realizar las cuentas
from math import *
import sympy as sp

def secante():
    # Definimos la variable X como un simbolo matematico para poder utilizar a futuro    
    x = sp.symbols('x')
    func_str = input("Ingrese la función en x: ")
    try:
        # Habilitamos utilizar terminologia especifica somo "seno" y demas para que se interprete desde la consola y asi realizar calculos a futuro
        f_expr = sp.sympify(func_str,locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt,"sin": sp.sin, "cos": sp.cos, "tan": sp.tan,"pi": sp.pi, "E": sp.E, "e": sp.E})
    except Exception as e:
        print(f"Función inválida: {e}")
        return
    
    # Convertimos la funcion simbolica ingresada por el usuario a una funcion que pueda ser interpreta por python y asi poder derivarla y trabajarla
    f = sp.lambdify(x, f_expr, "math")

    # Solicitamos al usuario que ingrese el valor inicial x0, x1 y tolerancia   
    x1 = int(input("Ingrese el valor de x1: "))
    x2 = int(input("Ingrese el valor de x2: "))
    tol = float(input("Ingrese el valor de la tolerancia: "))
    error = 1e3
    n = 0
    x3 = 0

    #Calculamos las raices mientras que el error calculado sea mayor a la tolerancia
    while error > tol:
        # Fórmula de la secante
        x3 = x1 - ((x2 - x1)/(f(x2)-f(x1)))*f(x1)

        # Mostrar en pantalla los puntos que definen la secante actual
        print(f"Iteración {n+1}: intervalo [{x1:.6f}, {x2:.6f}]")

        #Actualizamos los valores de las variables
        x1 = x2
        x2 = x3
        error = abs(f(x3))
        n = n + 1
        
        print(f"X -> {n} = {x3}")
    print("============================")
    print(f"X -> {n} = {x3} es una aproximacion valida de la raiz")

secante()
    
