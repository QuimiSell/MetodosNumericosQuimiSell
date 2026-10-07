"""
CLASE 16 - PARTE 2: MÉTODO DE GAUSS-JORDAN
Caso: Balance de masa en una columna de destilación fraccionada de 4 hidrocarburos:
      [Para-Xileno, Estireno, Tolueno, Benceno].

ANALOGÍA FEYNMAN (LA BATALLA DE LOS FLOPS):
Gauss-Jordan normaliza la diagonal principal a 1 y anula elementos tanto abajo
como arriba del pivote al mismo tiempo. Al terminar, la solución se lee directamente.
Sin embargo, eliminar hacia arriba mientras avanzas duplica operaciones innecesarias.
- Eliminación Gaussiana: O( (2/3) * n^3 ) operaciones de punto flotante (FLOPs).
- Gauss-Jordan:          O( n^3 ) FLOPs.
Para un sistema 4x4 la diferencia es despreciable, pero en IA (redes neuronales,
visión por computadora o modelos LLM con millones de parámetros), ese 50% extra
de cálculo vuelve inviable a Gauss-Jordan frente a descomposiciones LU o QR.
"""

import numpy as np


def imprimir_matriz(matriz, etiqueta=""):
    """Muestra la matriz aumentada con formato tabular legible."""
    print(f"\n--- {etiqueta} ---")
    filas, columnas = matriz.shape
    for i in range(filas):
        fila_str = " | ".join(f"{matriz[i, j]:8.3f}" for j in range(columnas - 1))
        print(f"| {fila_str} || {matriz[i, -1]:8.3f} |")


# 1. Definición del sistema 4x4
# Fracciones másicas de Para-Xileno, Estireno, Tolueno y Benceno en 4 corrientes
A = np.array(
    [
        [0.40, 0.15, 0.20, 0.10],
        [0.25, 0.45, 0.10, 0.15],
        [0.20, 0.25, 0.55, 0.10],
        [0.15, 0.15, 0.15, 0.65],
    ],
    dtype=float,
)

# Flujos totales de salida requeridos (kg/h)
b = np.array([120.0, 180.0, 260.0, 240.0], dtype=float)

# Matriz aumentada
M = np.hstack([A, b.reshape(-1, 1)])
n = len(b)

imprimir_matriz(M, "SISTEMA ORIGINAL DE DESTILACIÓN (4 COMPONENTES)")

# 2. Algoritmo de Gauss-Jordan
for k in range(n):
    # Pivoteo parcial
    fila_max = k + np.argmax(np.abs(M[k:, k]))
    if fila_max != k:
        M[[k, fila_max]] = M[[fila_max, k]]
        imprimir_matriz(
            M, f"PIVOTEO: Intercambio fila {k + 1} con fila {fila_max + 1}"
        )

    # Normalización de la fila pivote para colocar un 1 en la diagonal
    pivote = M[k, k]
    if np.isclose(pivote, 0.0):
        raise ValueError("Sistema singular o mal condicionado.")

    M[k, :] = M[k, :] / pivote
    imprimir_matriz(
        M, f"NORMALIZACIÓN: Fila {k + 1} dividida por el pivote {pivote:.3f}"
    )

    # Eliminación simultánea arriba y abajo de la diagonal
    for i in range(n):
        if i != k:
            factor = M[i, k]
            M[i, :] -= factor * M[k, :]

    imprimir_matriz(
        M,
        f"ANULACIÓN COMPLETA: Ceros arriba y abajo del pivote en columna {k + 1}",
    )

# 3. Extracción directa del vector solución
x = M[:, -1]
componentes = ["Para-Xileno", "Estireno", "Tolueno", "Benceno"]

print("\n========================================================")
print("             SOLUCIÓN DIRECTA POR GAUSS-JORDAN          ")
print("========================================================")
for comp, flujo in zip(componentes, x):
    print(f"Flujo de alimentación de {comp:12}: {flujo:10.4f} kg/h")

# Costo computacional teórico
flops_gauss = (2 / 3) * (n**3) + 2 * (n**2)
flops_jordan = (n**3) + (n**2)
print(f"\nComparativa analítica de complejidad (n = {n}):")
print(f"- FLOPs aproximados Gauss simple : {flops_gauss:.0f}")
print(f"- FLOPs aproximados Gauss-Jordan : {flops_jordan:.0f}")
print(f"Sobrecosto relativo de Gauss-Jordan: {(flops_jordan/flops_gauss - 1)*100:.1f}%")