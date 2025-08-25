import sympy as sp
from math import isnan, isinf

def newton_raphson():
    x = sp.symbols('x')
    func_str = input("Ingrese la función en x: ")
    try:
        f_expr = sp.sympify(func_str, locals={"exp": sp.exp, "log": sp.log, "sqrt": sp.sqrt, "sen": sp.sin, "cos": sp.cos, "tan": sp.tan, "pi": sp.pi, "E": sp.E, "e": sp.E})
    except Exception as e:
        print(f"Función inválida: {e}")
        return

    f = sp.lambdify(x, f_expr, "math")
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    try:
        x0 = float(input("Ingrese el valor de x0: "))
    except Exception:
        print("x0 inválido.")
        return
    tol = float(sp.sympify(input("Ingrese tolerancia: ")))
    max_iter = 1000

    print("\n--- Iteraciones método de Newton-Raphson ---\n")
    for k in range(1, max_iter + 1):
        fx0 = f(x0)
        dfx0 = df(x0)

        if dfx0 == 0:
            print(f"Iteración X{k}: derivada nula en x = {x0}. Se detiene.")
            return

        x1 = x0 - fx0 / dfx0
        paso = abs(x1 - x0)
        fval = abs(f(x1))

        if any(isnan(v) or isinf(v) for v in [x1, paso, fval]):
            print(f"Iteración X{k}: valores no numéricos/inf. Se detiene.")
            return

        print(f"Iteración X{k} -> x0 = {x0} | x1 = {x1} | Paso = {paso} | Valor de f(x1) = {fval}")

        if paso < tol:
            print(f"Convergió en x{k} -> x1 ≈ {x1} con paso = {paso} y valor de f(x1) = {fval}.")
            return

        if abs(x1) > 1e12:
            print(f"Iteración {k}: posible divergencia (|x| muy grande). Se detiene.")
            return

        x0 = x1
    print(f"No se alcanzó la tolerancia en {max_iter} iteraciones. Último x ≈ {x1}, |Δ|={paso}, |f(x)|={fval}.")

newton_raphson()