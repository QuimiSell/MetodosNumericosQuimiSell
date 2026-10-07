import numpy as np

def separador(titulo):
    print("\n" + "="*70)
    print(f" {titulo.upper()} ")
    print("="*70)

separador("Programa 4.8: Regla de Cramer (Demostración y Análisis de Complejidad)")

# -----------------------------------------------------------------------------
# 1. DEFINICIÓN DEL SISTEMA 3x3
# -----------------------------------------------------------------------------
# 3x1 + 2x2 - 1x3 = 1
# 2x1 - 1x2 + 4x3 = 6
# 1x1 + 1x2 + 1x3 = 4

A = np.array([
    [ 3.0,  2.0, -1.0],
    [ 2.0, -1.0,  4.0],
    [ 1.0,  1.0,  1.0]
])

b = np.array([1.0, 6.0, 4.0])

print("Matriz Principal A:")
print(A)
print("\nVector de Términos Independientes b:")
print(b)

# -----------------------------------------------------------------------------
# 2. CÁLCULO DEL DETERMINANTE PRINCIPAL
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# El determinante (det A o Delta A) mide el "factor de escala de volumen" de la matriz.
# Si det(A) == 0, la matriz colapsa el espacio a 0 dimensiones (es singular);
# las ecuaciones se cruzan de forma paralela o son infinitas, ¡no hay solución única!

det_A = np.linalg.det(A)
print(f"\nDeterminante Principal (Delta A): {det_A:8.4f}")

if np.isclose(det_A, 0.0):
    raise ValueError("El determinante es 0. El sistema no tiene solución única (Matriz Singular).")

# -----------------------------------------------------------------------------
# 3. APLICACIÓN DE LA REGLA DE CRAMER
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# ¿Cómo funciona Cramer? Para hallar la incógnita x_i:
# 1. Tomamos la matriz A y REEMPLAZAMOS su columna 'i' con el vector 'b'.
# 2. Calculamos el nuevo determinante (Delta A_i).
# 3. La solución es simplemente la razón: x_i = Delta A_i / Delta A.

x = np.zeros(len(b))

print("\n--- SUSTITUCIÓN DE COLUMNAS Y CÁLCULO DE DETERMINANTES INTERMEDIOS ---")
for i in range(len(b)):
    # Creamos una copia de A para no alterar la matriz original
    A_i = A.copy()
    
    # Sustituimos la columna 'i' por el vector 'b'
    A_i[:, i] = b
    
    det_A_i = np.linalg.det(A_i)
    x[i] = det_A_i / det_A
    
    print(f"\nMatriz A_{i+1} (Columna {i+1} reemplazada por b):")
    print(A_i)
    print(f"Determinante Delta A_{i+1}: {det_A_i:8.4f}")
    print(f"-> x_{i+1} = {det_A_i:.4f} / {det_A:.4f} = {x[i]:8.4f}")

# -----------------------------------------------------------------------------
# 4. IMPRESIÓN DE RESULTADOS FINALES Y ADVERTENCIA COMPUTACIONAL
# -----------------------------------------------------------------------------
print("\n--- SOLUCIÓN FINAL DEL SISTEMA ---")
print(f"x1 = {x[0]:8.4f} unidades")
print(f"x2 = {x[1]:8.4f} unidades")
print(f"x3 = {x[2]:8.4f} unidades")

# FEYNMAN EXPLICACIÓN: ¿POR QUÉ CRAMER ES UNA PESADILLA COMPUTACIONAL?
# Para resolver un sistema de n x n ecuaciones con Cramer, necesitas calcular (n + 1) determinantes.
# El cálculo de un determinante por definición requiere n! (factorial) operaciones.
# El número total de operaciones flota en O((n+1)!).
#
# EJEMPLO EN LA VIDA REAL:
# - Para un sistema de 10x10:
#   * Cramer necesita ~39,916,800 operaciones.
#   * Eliminación Gaussiana o LU necesita solo ~667 operaciones.
# - Para un sistema industrial de 100x100:
#   * Cramer requeriría más de 10^157 operaciones. ¡Incluso la supercomputadora más rápida
#     del mundo tardaría más que la edad del universo en resolverlo!
#   * LU lo resuelve en menos de 1 milisegundo.
# POR ESTO la industria jamas usa Cramer en software de producción real.