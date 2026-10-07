import numpy as np

def separador(titulo):
    print("\n" + "="*70)
    print(f" {titulo.upper()} ")
    print("="*70)

separador("Programa 4.7: Inversa Múltiple (Transferencia 2D - Multi-Escenario)")

# -----------------------------------------------------------------------------
# 1. MATRIZ DEL SISTEMA Y MATRIZ DE CONDICIONES B
# -----------------------------------------------------------------------------
# Mismo dominio físico (placa triangular de 3 nodos interiores), pero evaluando:
# Columna B[:, 0] -> Escenario 1: Verano (Fronteras a alta temperatura)
# Columna B[:, 1] -> Escenario 2: Invierno (Fronteras bajo cero)

A = np.array([
    [ 4.0, -1.0, -1.0],
    [-1.0,  4.0, -1.0],
    [-1.0, -1.0,  4.0]
])

# Matriz B con 2 columnas (2 escenarios de frontera simultáneos)
B = np.array([
    [150.0, -10.0],  # Frontera Nodo 1 (Verano vs Invierno)
    [200.0,  -5.0],  # Frontera Nodo 2
    [100.0, -20.0]   # Frontera Nodo 3
])

print("Matriz Físico-Estructural A:")
print(A)
print("\nMatriz de Cargas B (Columna 1: Verano [K], Columna 2: Invierno [K]):")
print(B)

# -----------------------------------------------------------------------------
# 2. INVERSIÓN Y RESOLUCIÓN SIMULTÁNEA
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# Si AX = B, entonces X = A^-1 * B.
# En lugar de resolver 2 sistemas lineales independientes de 3x3,
# invertimos A una sola vez y multiplicamos por la MATRIZ B de (3x2).
# Esto nos devuelve una MATRIZ X de (3x2), donde cada columna es la solución completa
# para ese escenario meteorológico.

A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)

print("\n--- MATRIZ INVERSA CALCULADA A^-1 ---")
print(np.round(A_inv, 4))

print("\n--- MATRIZ DE SOLUCIONES X (Temperaturas Nodal en K) ---")
print(" Fila = Nodo | Columna 1 = Verano | Columna 2 = Invierno")
print(np.round(X, 2))

# -----------------------------------------------------------------------------
# 3. DESGLOSE DE RESULTADOS
# -----------------------------------------------------------------------------
print("\n--- RESULTADOS POR ESCENARIO ---")
nodos = ["Nodo T1", "Nodo T2", "Nodo T3"]

print("ESCENARIO 1 (VERANO):")
for nodo, temp in zip(nodos, X[:, 0]):
    print(f"  {nodo}: {temp:7.2f} K")

print("\nESCENARIO 2 (INVIERNO):")
for nodo, temp in zip(nodos, X[:, 1]):
    print(f"  {nodo}: {temp:7.2f} K")