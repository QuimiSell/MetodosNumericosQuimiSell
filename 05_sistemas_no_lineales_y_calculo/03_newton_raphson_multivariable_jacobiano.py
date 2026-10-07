"""
======================================================================
CLASE 19: OPTIMIZANDO EN MULTIPLES DIMENSIONES
SCRIPT 3: METODO DE NEWTON-RAPHSON MULTIVARIABLE (CON JACOBIANA)
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Que es la Matriz Jacobiana J(x, y)?
   En una dimension, Newton usa la derivada simple (la pendiente de la recta).
   En dos dimensiones, la Jacobiana es una tabla 2x2 que reune todas las
   derivadas parciales posibles:
      J = [ [df1/dx, df1/dy],
            [df2/dx, df2/dy] ]
   Representa las pendientes del plano tangente a la curva en ese punto.

2. ¿Por que resolvemos J * delta = -F en vez de despejar?
   Invertir matrices a mano o en computadora es lento y propenso a errores
   numericos. En su lugar, resolvemos el sistema lineal auxiliar:
      J * [delta_x, delta_y]^T = -[f1, f2]^T
   Ese vector 'delta' nos dice exactamente cuanto debemos sumar a (x, y)
   para dar un 'salto cuadratico' directo a la raiz. En cada iteracion,
   el numero de decimales correctos casi se duplica.
"""

import numpy as np

# ====================================================================
# SECCION PARA LA TAREA: EDITA AQUI TUS FUNCIONES F(x, y) = 0 Y SU JACOBIANA
# Sistema original:
#   f1(x, y) = x^2 + y - 3 = 0
#   f2(x, y) = x + y^2 - 3 = 0
# ====================================================================

def funciones_F(x, y):
    """Evalua el vector de funciones f1 y f2 igualadas a cero"""
    f1 = x**2 + y - 3.0
    f2 = x + y**2 - 3.0
    return np.array([f1, f2], dtype=float)

def matriz_jacobiana(x, y):
    """
    Derivadas parciales del sistema:
      df1/dx = 2x,   df1/dy = 1
      df2/dx = 1,    df2/dy = 2y
    """
    df1_dx = 2.0 * x
    df1_dy = 1.0
    df2_dx = 1.0
    df2_dy = 2.0 * y
    
    J = np.array([
        [df1_dx, df1_dy],
        [df2_dx, df2_dy]
    ], dtype=float)
    return J


# ====================================================================
# ALGORITMO PRINCIPAL
# ====================================================================

def newton_raphson_multivariable(x_inicial, y_inicial, tolerancia=1e-6, max_iter=50):
    print("=" * 68)
    print(" METODO DE NEWTON-RAPHSON MULTIVARIABLE (SALTO CUADRATICO)")
    print("=" * 68)
    print(f"{'Iter':<5} | {'x':<15} | {'y':<15} | {'Norma Delta':<15}")
    print("-" * 68)

    x = float(x_inicial)
    y = float(y_inicial)

    for iteracion in range(1, max_iter + 1):
        # 1. Evaluamos funciones y derivadas en el punto actual
        F_val = funciones_F(x, y)
        J_val = matriz_jacobiana(x, y)

        # 2. Resolvemos el sistema lineal: J * delta = -F
        try:
            delta = np.linalg.solve(J_val, -F_val)
        except np.linalg.LinAlgError:
            print("Error numerico: La matriz Jacobiana es singular (determinante = 0).")
            print("Elige otro punto inicial.")
            return x, y

        delta_x = delta[0]
        delta_y = delta[1]

        # 3. Aplicamos el salto correctivo a nuestras variables
        x = x + delta_x
        y = y + delta_y

        # 4. La norma del vector delta nos dice cuanto nos movimos (tamano del salto)
        norma_delta = np.sqrt(delta_x**2 + delta_y**2)

        # 5. Mostramos la fila en la tabla
        print(f"{iteracion:<5} | {x:<15.8f} | {y:<15.8f} | {norma_delta:<15.8e}")

        # 6. Criterio de paro: si el salto es casi cero, ya llegamos
        if norma_delta < tolerancia:
            print("-" * 68)
            print(" RESULTADO FINAL:")
            print(f" -> Convergencia cuadratica alcanzada en {iteracion} iteraciones.")
            print(f" -> x = {x:.8f}")
            print(f" -> y = {y:.8f}")
            print(f" -> Error estimado = {norma_delta:.8e}")
            print("=" * 68)
            return x, y

    print("-" * 68)
    print(" Advertencia: Se alcanzo el maximo de iteraciones sin converger.")
    print("=" * 68)
    return x, y


# ====================================================================
# EJECUCION DEL CODIGO
# ====================================================================
if __name__ == "__main__":
    x0 = 1.5
    y0 = 1.5
    
    newton_raphson_multivariable(x_inicial=x0, y_inicial=y0, tolerancia=1e-6)