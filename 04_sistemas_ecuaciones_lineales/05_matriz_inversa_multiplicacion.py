import numpy as np

def separador(titulo):
    print("\n" + "="*70)
    print(f" {titulo.upper()} ")
    print("="*70)

separador("Programa 4.6: Inversa-Multiplicación (Reactores Químicos Continuos)")

# -----------------------------------------------------------------------------
# 1. MODELO MATEMÁTICO DEL SISTEMA DE REACTORES
# -----------------------------------------------------------------------------
# Balances de masa en estado estacionario para 4 reactores acoplados (C1, C2, C3, C4):
# [ 6 -1  0  0 ] [C1]   [ 120 ] (Alimentación externa al Reactor 1)
# [-3  7 -2  0 ] [C2] = [   0 ]
# [ 0 -2  8 -1 ] [C3]   [   0 ]
# [ 0  0 -3  5 ] [C4]   [   0 ]

A = np.array([
    [ 6.0, -1.0,  0.0,  0.0],
    [-3.0,  7.0, -2.0,  0.0],
    [ 0.0, -2.0,  8.0, -1.0],
    [ 0.0,  0.0, -3.0,  5.0]
])

b = np.array([120.0, 0.0, 0.0, 0.0]) # Entrada de reactivo [mol/L * h]

print("Matriz de Interconexión y Flujos A:")
print(A)
print("\nVector de Cargas/Entradas Externas b [mol/(L*h)]:")
print(b)

# -----------------------------------------------------------------------------
# 2. CÁLCULO DE LA MATRIZ INVERSA
# -----------------------------------------------------------------------------
# FEYNMAN EXPLICACIÓN:
# ¿Qué significa INVERTIR una matriz A en el mundo real?
# La matriz A representa "Cómo los estados internos generan las salidas".
# La matriz A^-1 representa la "Función de Transferencia Directa":
# Nos dice cuánta concentración se genera en CUALQUIER reactor por cada unidad
# de reactivo que alimentemos en CUALQUIER entrada.
# Cada fila 'i', columna 'j' de A^-1 nos da el impacto directo del reactor 'j' sobre el 'i'.

A_inv = np.linalg.inv(A)

print("\n--- MATRIZ INVERSA A^-1 (Respuesta Fundamental del Sistema) ---")
print(np.round(A_inv, 4))

# -----------------------------------------------------------------------------
# 3. SOLUCIÓN MEDIANTE MULTIPLICACIÓN MATRICIAL
# -----------------------------------------------------------------------------
# x = A^-1 * b
concentraciones = np.dot(A_inv, b)

print("\n--- VECTOR DE SOLUCIÓN x = A^-1 * b ---")
for i, C in enumerate(concentraciones, 1):
    print(f"Concentración en Reactor C{i}: {C:8.4f} mol/L")

# -----------------------------------------------------------------------------
# ADVVERTENCIA PEDAGÓGICA (COSTO COMPUTACIONAL)
# -----------------------------------------------------------------------------
# FEYNMAN ADVERTENCIA:
# Aunque x = A^-1 * b es elegante visualmente, ¡NUNCA la uses en la práctica industrial
# para sistemas grandes!
# Invertir una matriz requiere aprox. 3 veces más operaciones flotantes que la Descomposición LU.
# Calcular A^-1 introduce además mayor error de redondeo numérico.