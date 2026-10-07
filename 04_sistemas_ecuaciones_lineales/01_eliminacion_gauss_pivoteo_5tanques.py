"""
CLASE 16 - PARTE 1: ELIMINACIÓN GAUSSIANA CON SUSTITUCIÓN HACIA ATRÁS
Caso: Balance de masa en estado estacionario de 5 tanques interconectados (5x5).

ANALOGÍA FEYNMAN (PIVOTEO PARCIAL):
Imagina que vas a construir una torre de bloques y la base de apoyo es un palillo
que apenas soporta peso. Si intentas dividir el peso de todo el edificio entre
un número muy cercano a cero, la estructura colapsa (error por redondeo de punto flotante).
Pivotar es simplemente revisar la columna actual, buscar el bloque más pesado
(el valor absoluto más grande) y colocarlo como soporte principal intercambiando filas.
"""

import numpy as np


def imprimir_matriz(matriz, etiqueta=""):
    """Muestra la matriz aumentada con formato tabular legible."""
    print(f"\n--- {etiqueta} ---")
    filas, columnas = matriz.shape
    for i in range(filas):
        fila_str = " | ".join(f"{matriz[i, j]:8.3f}" for j in range(columnas - 1))
        print(f"| {fila_str} || {matriz[i, -1]:8.3f} |")


# 1. Definición del sistema A * x = b
# Concentraciones de soluto y flujos volumétricos entre 5 reactores continuos (CSTR)
A = np.array(
    [
        [15.0, -3.0, -1.0, 0.0, 0.0],
        [-3.0, 18.0, -6.0, -1.0, 0.0],
        [-1.0, -4.0, 12.0, -2.0, -1.0],
        [0.0, -1.0, -2.0, 10.0, -3.0],
        [0.0, 0.0, -1.0, -2.0, 8.0],
    ],
    dtype=float,
)

b = np.array([3200.0, 1200.0, 500.0, 0.0, 200.0], dtype=float)

# Creamos la matriz aumentada [A | b] trabajando sobre copias de precisión flotante
M = np.hstack([A, b.reshape(-1, 1)])
n = len(b)

imprimir_matriz(M, "ESTADO INICIAL DEL SISTEMA DE 5 TANQUES [A | b]")

# 2. Fase de Eliminación Hacia Adelante (Triangularización Superior)
for k in range(n - 1):
    # PIVOTEO PARCIAL:
    # Localizamos el coeficiente de mayor magnitud en la columna k desde la fila k hacia abajo.
    fila_max = k + np.argmax(np.abs(M[k:, k]))

    if fila_max != k:
        # Intercambio de filas en Python usando desempaquetado de tuplas
        M[[k, fila_max]] = M[[fila_max, k]]
        imprimir_matriz(
            M,
            f"PIVOTEO: Intercambio fila {k + 1} con fila {fila_max + 1} (Elemento pivote: {M[k, k]:.3f})",
        )

    # Verificación de singularidad
    if np.isclose(M[k, k], 0.0):
        raise ValueError(
            "El sistema no tiene solución única (pivote nulo detectado)."
        )

    # Anulación de coeficientes por debajo del pivote
    for i in range(k + 1, n):
        factor = M[i, k] / M[k, k]
        # Operación elemental por filas: F_i = F_i - (factor * F_k)
        M[i, k:] -= factor * M[k, k:]

    imprimir_matriz(
        M, f"PASO {k + 1}: Ceros completados debajo de la columna {k + 1}"
    )

# 3. Fase de Sustitución Hacia Atrás
# La última fila es ahora una ecuación simple de una variable: M[n-1, n-1] * x[n-1] = M[n-1, n]
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    suma_conocidos = np.dot(M[i, i + 1 : n], x[i + 1 : n])
    x[i] = (M[i, -1] - suma_conocidos) / M[i, i]

# 4. Verificación industrial
x_numpy = np.linalg.solve(A, b)

print("\n========================================================")
print("              RESULTADOS FINALES DE CONCENTRACIÓN        ")
print("========================================================")
for i in range(n):
    print(
        f"Tanque {i + 1} (x{i + 1}): {x[i]:10.4f} mg/L | NumPy: {x_numpy[i]:10.4f} mg/L"
    )

error_maximo = np.max(np.abs(x - x_numpy))
print(f"\nDiferencia absoluta máxima frente a LAPACK: {error_maximo:.2e}")