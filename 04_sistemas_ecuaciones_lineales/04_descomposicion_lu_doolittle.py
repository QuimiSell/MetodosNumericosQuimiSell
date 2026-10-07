import numpy as np
import scipy.linalg as la

def separador(titulo):
    print("\n" + "="*70)
    print(f" {titulo.upper()} ")
    print("="*70)

separador("Programa 4.5: Descomposición LU (Transferencia de Calor Radial)")

# -----------------------------------------------------------------------------
# 1. DEFINICIÓN DEL SISTEMA FÍSICO Y MATRICIAL
# -----------------------------------------------------------------------------
# Balance de energía por conducción radial en 3 nodos de la tubería aislada:
# -3T1 + T2         = -100  (Condición de frontera interna: vapor a alta temp)
#  T1 - 2T2 + T3    =    0  (Conducción intermedia)
#       T2 - 2T3    =  -25  (Condición de frontera externa: convección aire)

A = np.array([
    [-3.0,  1.0,  0.0],
    [ 1.0, -2.0,  1.0],
    [ 0.0,  1.0, -2.0]
])

b1 = np.array([-100.0, 0.0, -25.0]) # Temperaturas de frontera originales

print("Matriz de Coeficientes A (Geometría y Propiedades Térmicas):")
print(A)
print("\nVector b1 (Temperaturas de Frontera Escenario 1 - [°C]):")
print(b1)

# -----------------------------------------------------------------------------
# 2. FACTORIZACIÓN / DESCOMPOSICIÓN LU
# -----------------------------------------------------------------------------
# MÉTODOS NUMÉRICOS EXPLICADOS (Método Feynman):
# ¿Qué es la Descomposición LU?
# En lugar de resolver Ax = b todo de golpe, "desarmamos" la matriz A en dos triangulares:
# - L (Lower/Inferior): Guarda los "multiplicadores" usados en la eliminación gaussiana.
#   Representa la estructura interna de cómo interactúan las variables.
# - U (Upper/Superior): Es la matriz escalonada/triangulada resultante.
# - lu_factor devuelve (lu, piv): 'lu' empaqueta L y U en una sola matriz para ahorrar memoria.

lu, piv = la.lu_factor(A)

# Extraemos L y U explícitamente solo para fines didácticos en consola:
P, L, U = la.lu(A)

print("\n--- MATRICES INTERMEDIAS DE LA DESCOMPOSICIÓN ---")
print("Matriz L (Triangular Inferior - Multiplicadores de Eliminación):")
print(L)
print("\nMatriz U (Triangular Superior - Sistema Triangulado):")
print(U)

# -----------------------------------------------------------------------------
# 3. RESOLUCIÓN DEL SISTEMA MEDIANTE LU
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# Resolver Ax = b pasa a ser dos pasos de sustitución ultra rápidos:
# 1) L * y = b  -> Sustitución hacia adelante para hallar vector intermedio 'y'
# 2) U * x = y  -> Sustitución hacia atrás para hallar las 'T' reales

T_escenario1 = la.lu_solve((lu, piv), b1)

print("\n--- RESULTADOS ESCENARIO 1 ---")
for i, T in enumerate(T_escenario1, 1):
    print(f"Temperatura en Nodo T{i}: {T:8.2f} °C")

# -----------------------------------------------------------------------------
# 4. REUTILIZACIÓN DE LU (VENTAJA COMPETITIVA EN INGENIERÍA)
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# Imagina que cambia la temperatura del aire exterior (vector b cambia a b2).
# ¡NO necesitamos volver a triangular A! El esfuerzo pesado (O(n^3)) ya se hizo al hallar L y U.
# Resolver para el nuevo escenario toma casi 0 milisegundos (O(n^2)).

b2 = np.array([-100.0, 0.0, -40.0]) # Aire exterior se enfrió a -40°C

T_escenario2 = la.lu_solve((lu, piv), b2)

print("\n--- RESULTADOS ESCENARIO 2 (Cambio de Temperatura Ambiental a -40 °C) ---")
print("Resuelto reutilizando las matrices L y U ya calculadas:")
for i, T in enumerate(T_escenario2, 1):
    print(f"Temperatura en Nodo T{i}: {T:8.2f} °C")