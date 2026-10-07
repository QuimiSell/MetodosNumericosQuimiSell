"""
======================================================================
CLASE 19: OPTIMIZANDO EN MULTIPLES DIMENSIONES
SCRIPT 2: METODO DE GAUSS-SEIDEL MULTIVARIABLE (SUSTITUCION SUCESIVA)
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Cual es la diferencia clave con el Punto Fijo estandar?
   En el Punto Fijo normal, calculas 'x' y 'y' con datos viejos.
   En Gauss-Seidel, en cuanto calculas el nuevo valor de 'x', ¡lo usas
   inmediatamente para calcular 'y' en esa misma iteracion!

2. ¿Por que acelera la convergencia?
   Imagina que vas buscando un objeto con los ojos vendados y un amigo te
   va guiando. El punto fijo normal espera a dar dos pasos antes de pedir
   una pista. Gauss-Seidel ajusta el rumbo en cada paso individual con la
   informacion mas fresca posible.
"""

import numpy as np

# ====================================================================
# SECCION PARA LA TAREA: EDITA AQUI TUS ECUACIONES DESPEJADAS
# ====================================================================

def g1(x, y):
    """Despeje de x: x = g1(x, y)"""
    return np.sqrt(3.0 - y)

def g2(x, y):
    """Despeje de y: y = g2(x, y)"""
    return np.sqrt(3.0 - x)


# ====================================================================
# ALGORITMO PRINCIPAL
# ====================================================================

def gauss_seidel_multivariable(x_inicial, y_inicial, tolerancia=1e-6, max_iter=100):
    print("=" * 68)
    print(" METODO DE GAUSS-SEIDEL MULTIVARIABLE (SUSTITUCION SUCESIVA)")
    print("=" * 68)
    print(f"{'Iter':<5} | {'x':<15} | {'y':<15} | {'Error (Norma)':<15}")
    print("-" * 68)

    x_actual = x_inicial
    y_actual = y_inicial

    for iteracion in range(1, max_iter + 1):
        # Guardamos copia del estado anterior para medir el error al final
        x_anterior = x_actual
        y_anterior = y_actual

        # PASO CLAVE 1: Calculamos x usando los valores disponibles
        x_actual = g1(x_anterior, y_anterior)

        # PASO CLAVE 2: Calculamos y USANDO DIRECTAMENTE el x_actual recien calculado
        y_actual = g2(x_actual, y_anterior)

        # Calculamos la distancia respecto a la ronda anterior
        error = np.sqrt((x_actual - x_anterior)**2 + (y_actual - y_anterior)**2)

        # Mostramos el progreso en consola
        print(f"{iteracion:<5} | {x_actual:<15.8f} | {y_actual:<15.8f} | {error:<15.8e}")

        # Condicion de parada
        if error < tolerancia:
            print("-" * 68)
            print(" RESULTADO FINAL:")
            print(f" -> Convergencia alcanzada en {iteracion} iteraciones.")
            print(f" -> x = {x_actual:.8f}")
            print(f" -> y = {y_actual:.8f}")
            print(f" -> Error final = {error:.8e}")
            print("=" * 68)
            return x_actual, y_actual

    print("-" * 68)
    print(" Advertencia: Se alcanzo el maximo de iteraciones sin converger.")
    print("=" * 68)
    return x_actual, y_actual


# ====================================================================
# EJECUCION DEL CODIGO
# ====================================================================
if __name__ == "__main__":
    x0 = 1.5
    y0 = 1.5
    
    gauss_seidel_multivariable(x_inicial=x0, y_inicial=y0, tolerancia=1e-6)