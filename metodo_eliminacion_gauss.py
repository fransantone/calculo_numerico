import re

pat_var = re.compile(r'^([+-]?)(\d+(?:\.\d+)?)?(?:\*)?E(\d+)$')
pat_num = re.compile(r'^([+-]?\d+(?:\.\d+)?)$')

def visualizar_matriz(A, b, titulo=""):
    if titulo:
        print(f"\n{titulo}")
    n = len(A)
    for i in range(n):
        fila = "  ".join(f"{A[i][j]:10.6f}" for j in range(n))
        print(f"[ {fila} ] | {b[i]:10.6f}")
    print()

def ecuacioens():
    while True:
        try:
            n = int(input("Cantidad de ecuaciones (incognitas)): ").strip())
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("ERROR! Ingresá un entero positivo.")
    
    lista_incognitas = []
    lista_constantes = []
    for i in range(n):
        while True:
            linea = input(f"Ingrese la ecuacion {i+1}: ").strip()
            if "=" not in linea:
                print("ERROR! la ecuacion ingresda debe contener '='")
                continue
            lado_izquierdo, lado_derecho = linea.split("=", 1)

            ecuacion_1 = lado_izquierdo.replace(" ", "")
            ecuacion_1 = ecuacion_1.replace("-", "+-")
            parts = ecuacion_1.split("+")
            fila = [0.0]*n
            lado_izquierdo_validado = True
            try:
                for t in parts:
                    if t == "" or t == "+":
                        continue
                    if "E" not in t:
                        raise ValueError(f"Constante no permitida en LHS: '{t}'")
                    m = pat_var.match(t)
                    if not m:
                        raise ValueError(f"Término variable inválido: '{t}'. Usa 2E1, -E2, E3.")
                    sgn, a_str, idx_str = m.groups()
                    k = int(idx_str)
                    if not (1 <= k <= n):
                        raise ValueError(f"Variable E{k} fuera de rango (1..{n}) en '{t}'")
                    a = 1.0 if not a_str else float(a_str)
                    if sgn == "-":
                        a = -a
                    fila[k-1] += a
            except Exception as e:
                print(f"ERROR! {e}. Probá de nuevo.")
                lado_izquierdo_validado = False
            if not lado_izquierdo_validado:
                continue
            ecuacion_2 = lado_derecho.replace(" ", "")
            if "E" in ecuacion_2: 
                print("ERROR! El lado derecho no puede contener variables E.")
                continue
            ecuacion_2 = ecuacion_2.replace("-", "+-")
            parts = ecuacion_2.split("+")
            try:
                bi = 0.0
                for t in parts:
                    if t == "" or t == "+":
                        continue
                    if "e" in t or "E" in t:
                        raise ValueError(f"No se permite notación científica en RHS: '{t}'")
                    m = pat_num.match(t)
                    if not m:
                        raise ValueError(f"RHS inválido: término '{t}'. Debe ser numérico.")
                    bi += float(m.group(1))
            except Exception as e:
                print(f"ERROR! {e}. Probá de nuevo.")
                continue

            lista_incognitas.append(fila)
            lista_constantes.append(bi)
            break

    visualizar_matriz(lista_incognitas, lista_constantes, "Matriz construida [E(i) | K]")
    return lista_constantes, lista_incognitas, n

def eliminacion_gauss(A, b, verbose=True):
    n = len(A)
    A = [row[:] for row in A]
    b = b[:]

    if verbose:
        visualizar_matriz(A, b, "Estado inicial")

    for k in range(n-1):
        if abs(A[k][k]) == 0.0:
            p = None
            for i in range(k+1, n):
                if abs(A[i][k]) != 0.0:
                    p = i
                    break
            if p is None:
                raise ZeroDivisionError("No hay pivote no nulo: el sistema no tiene solución única.")
            A[k], A[p] = A[p], A[k]
            b[k], b[p] = b[p], b[k]
        for i in range(k+1, n):
            if A[i][k] == 0.0:
                continue
            m = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= m * A[k][j]
            b[i] -= m * b[k]
    return A, b

def sustitucion_desde_atras(U, c):
    n = len(U)
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        if U[i][i] == 0.0:
            raise ZeroDivisionError("Pivote nulo durante la sustitución hacia atrás.")
        s = c[i] - sum(U[i][j]*x[j] for j in range(i+1, n))
        x[i] = s / U[i][i]
    return x

def resolver_sistema():
    b, A, n = ecuacioens()
    U, c = eliminacion_gauss(A, b, verbose=True)
    x = sustitucion_desde_atras(U, c)
    print("\nSolución (valores de cada Ei):")
    for i, xi in enumerate(x, start=1):
        print(f"E{i} = {xi:.10f}")

if __name__ == "__main__":
    resolver_sistema()
