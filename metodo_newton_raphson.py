# Importamos las librerias math y sympy para utilizar la nomenclatura tecnica de matematica y que se entienda al escribir en consola y realizar las cuentas
import sympy as sp
from math import *

# Librerias para graficar
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson():
    # Definimos la variable X como un simbolo matematico para poder utilizar a futuro    
    x = sp.symbols('x')
    func_str = input("Ingrese la función en x: ")
    try:
        # Habilitamos utilizar terminologia especifica somo "seno" y demas para que se interprete desde la consola y asi realizar calculos a futuro
        f_expr = sp.sympify(func_str, locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt, "sen": sp.sin, "cos": sp.cos, "tan": sp.tan, "pi": sp.pi, "E": sp.E, "e": sp.E})
    except Exception as e:
        print(f"Función inválida: {e}")
        return

    # Convertimos la funcion simbolica ingresada por el usuario a una funcion que pueda ser interpreta por python y asi poder derivarla y trabajarla
    f = sp.lambdify(x, f_expr, "math")
    f_np = sp.lambdify(x, f_expr, "numpy")
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    # Solicitamos al usuario que ingrese el valor inicial x0 y la tolerancia    
    try:
        x0 = float(input("Ingrese el valor de x0: "))
    except Exception:
        print("x0 inválido.")
        return
    tol = float(sp.sympify(input("Ingrese tolerancia: ")))
    max_iter = 1000 #tomamos como valor maximo de iteraciones 1000, pero se podria ingresar por el usuario

    #Comenzamos a realizar las cuentas correspondientes al metodo de newton
    print("\n--- Iteraciones método de Newton-Raphson --- \n")

    for k in range(1, max_iter + 1): # Recorremos un máximo de 'max_iter' iteraciones

        # Evaluamos la función y su derivada en el punto actual x0
        fx0 = f(x0)
        dfx0 = df(x0)

        # Si la derivada es cero, no podemos seguir (división por cero en la fórmula)
        if dfx0 == 0:
            print(f"Iteración X{k}: derivada nula en x = {x0}. Se detiene.")
            return

        # Fórmula de Newton-Raphson: x1 = x0 - f(x0)/f'(x0)
        x1 = x0 - fx0 / dfx0

        #  La variable 'paso' mide cuánto se movió la raíz en esta iteración y la variable 'fval' el valor de f(x) en ese punto
        paso = abs(x1 - x0)
        fval = abs(f(x1))

        # Si aparece un valor NaN o infinito → se corta el algoritmo
        if any(isnan(v) or isinf(v) for v in [x1, paso, fval]):
            print(f"Iteración X{k}: valores no numéricos/inf. Se detiene.")
            break
        
        # Mostramos el estado de la iteración actual
        print(f"Iteración X{k} -> x0 = {x0} | x1 = {x1} | Paso = {paso} | Valor de f(x1) = {fval}")

        # Criterio de convergencia: si el paso es menor a la tolerancia → se detiene
        if paso < tol:
            convergio = True
            print(f"Convergió en x{k} -> x1 ≈ {x1} con paso = {paso} y valor de f(x1) = {fval}.")
            break
        
        # Control adicional: si la aproximación explota a un valor muy grande → sospecha de divergencia
        if abs(x1) > 1e12:
            print(f"Iteración {k}: posible divergencia (|x| muy grande). Se detiene.")
            break

        # Actualizamos x0 para la siguiente iteración
        x0 = x1

    # De no encontrar una raiz dentro de las 1000 iteraciones mostramos donde quedo la ultima y sus valores correspondientes
    if not convergio:
        print(f"No se alcanzó la tolerancia en {max_iter} iteraciones o se detuvo antes. Último x ≈ {x1}, |Δ|={paso}, |f(x)|={fval}.")
        raiz = x1

    # Grafico
    ancho_ref = 5.0 * (paso if paso not in (None, 0.0) else 1e-2)
    ancho = max(1.0, ancho_ref)
    Xmin, Xmax = x1 - ancho, x1 + ancho
    X = np.linspace(Xmin, Xmax, 1000)
    Y = f_np(X)
    mask = np.isfinite(Y)
    X = X[mask]
    Y = Y[mask]
    plt.figure(figsize=(7,4))
    plt.plot(X, Y, label='f(x)')
    plt.axhline(0, linewidth=1, color='k')
    plt.axvline(0, linewidth=1, color='k')
    plt.plot(x1, 0, 'o', label=f'raíz ≈ {x1:.6f}')
    plt.annotate(f"f({x1:.6f}) = {f(x1):.2e}", xy=(x1, 0), xytext=(10, 15), textcoords='offset points', arrowprops=dict(arrowstyle='->', lw=1))
    plt.title('Función con raíz marcada (Newton-Raphson)')
    plt.xlabel('x'); plt.ylabel('f(x)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    newton_raphson()