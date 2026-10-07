"""
======================================================================
CLASE 19: OPTIMIZANDO EN MULTIPLES DIMENSIONES
SCRIPT 1: METODO DEL PUNTO FIJO MULTIVARIABLE (JACOBI / SIMULTANEO)
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Por que despejamos cada variable?
   Imagina que tienes dos ecuaciones entrelazadas. Para resolverlas por
   punto fijo, aislamos una variable en cada ecuacion:
      x = g1(x, y)
      y = g2(x, y)
   Esto crea una 'receta de cocina': le das las coordenadas actuales y
   la formula te entrega el siguiente paso.

2. ¿Que significa que el sistema sea contractivo?
   Significa que las formulas actuan como un iman o un embudo. Cada vez
   que aplicas g1 y g2, los resultados no explotan hacia el infinito, sino
   que dan saltos cada vez mas pequenos hasta quedarse quietos en la solucion.
   (Matematicamente, las derivadas parciales deben ser pequenas, < 1).

3. ¿Por que usamos la 'foto anterior' del vector?
   En el Punto Fijo estandar, calculamos el nuevo 'x' y el nuevo 'y' usando
   EXCLUSIVAMENTE los valores de la vuelta anterior (k-1). Es como tomar
   una foto fija del estado y calcular todo con base en esa foto.
"""

import numpy as np

# ====================================================================
# SECCION PARA LA TAREA: EDITA AQUI TUS ECUACIONES DESPEJADAS
# Sistema de ejemplo:
#   Ecuacion 1: x^2 + y = 3   -->  x = sqrt(3 - y)
#   Ecuacion 2: x + y^2 = 3   -->  y = sqrt(3 - x)
# ====================================================================

def g1(x, y):
    """Despeje de x en funcion de (x, y)"""
    return np.sqrt(3.0 - y)

def g2(x, y):
    """Despeje de y en funcion de (x, y)"""
    return np.sqrt(3.0 - x)


# ====================================================================
# ALGORITMO PRINCIPAL
# ====================================================================

def punto_fijo_multivariable(x_inicial, y_inicial, tolerancia=1e-6, max_iter=100):
    print("=" * 68)
    print(" METODO DEL PUNTO FIJO MULTIVARIABLE")
    print("=" * 68)
    print(f"{'Iter':<5} | {'x':<15} | {'y':<15} | {'Error (Norma)':<15}")
    print("-" * 68)

    # Valores iniciales (k = 0)
    x_anterior = x_inicial
    y_anterior = y_inicial

    for iteracion in range(1, max_iter + 1):
        # 1. Calculamos los nuevos valores usando solo la foto anterior
        x_nuevo = g1(x_anterior, y_anterior)
        y_nuevo = g2(x_anterior, y_anterior)

        # 2. Medimos la distancia (error) entre el punto nuevo y el anterior
        #    Formula de distancia euclidiana: d = sqrt((x_n - x_a)^2 + (y_n - y_a)^2)
        error = np.sqrt((x_nuevo - x_anterior)**2 + (y_nuevo - y_anterior)**2)

        # 3. Mostramos la fila de la tabla formateada
        print(f"{iteracion:<5} | {x_nuevo:<15.8f} | {y_nuevo:<15.8f} | {error:<15.8e}")

        # 4. Verificamos si ya llegamos a la precision deseada
        if error < tolerancia:
            print("-" * 68)
            print(" RESULTADO FINAL:")
            print(f" -> Convergencia alcanzada en {iteracion} iteraciones.")
            print(f" -> x = {x_nuevo:.8f}")
            print(f" -> y = {y_nuevo:.8f}")
            print(f" -> Error final = {error:.8e}")
            print("=" * 68)
            return x_nuevo, y_nuevo

        # 5. Actualizamos los valores anteriores para la siguiente ronda
        x_anterior = x_nuevo
        y_anterior = y_nuevo

    print("-" * 68)
    print(" Advertencia: Se alcanzo el maximo de iteraciones sin converger.")
    print("=" * 68)
    return x_anterior, y_anterior


# ====================================================================
# EJECUCION DEL CODIGO
# ====================================================================
if __name__ == "__main__":
    # Cambia estos valores iniciales segun el problema de tu tarea
    x0 = 1.5
    y0 = 1.5
    
    punto_fijo_multivariable(x_inicial=x0, y_inicial=y0, tolerancia=1e-6)