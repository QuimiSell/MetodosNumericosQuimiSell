"""
CLASE 16 - PARTE 3: SISTEMAS SUBDETERMINADOS CON SYMPY (RREF)
Caso: Balanceo de la reacción química homogénea:
      x1*AgNO3 + x2*K2CrO4 -> x3*Ag2CrO4 + x4*KNO3

ANALOGÍA FEYNMAN (EL MISTERIO DE LAS INFINITAS SOLUCIONES):
Si tienes 4 incógnitas pero solo 3 elementos (conservación de Ag, N, O, K, Cr),
tienes más variables que restricciones independientes: el sistema es rectangular.
Los algoritmos clásicos de punto flotante fallan o se dividen entre cero al buscar
una respuesta única que no existe. La química no tiene una sola solución:
puedes hacer la reacción con 1 mol, 2 moles o 1000 moles.
Buscamos el 'espacio nulo' (Kernel): una familia infinita de soluciones donde
elegimos el menor multiplicador entero que mantenga las moléculas enteras.
"""

import sympy as sp

# 1. Definición analítica de los elementos:
# Ecuación balanceada: x1*AgNO3 + x2*K2CrO4 - x3*Ag2CrO4 - x4*KNO3 = 0
# Elementos evaluados: [Ag, N, O, K, Cr] (5 filas x 4 columnas)

A_quimica = sp.Matrix(
    [
        # x1(AgNO3)  x2(K2CrO4)  x3(Ag2CrO4)  x4(KNO3)
        [1, 0, -2, 0],  # Plata (Ag)
        [1, 0, 0, -1],  # Nitrógeno (N)
        [3, 4, -4, -3],  # Oxígeno (O)
        [0, 2, 0, -1],  # Potasio (K)
        [0, 1, -1, 0],  # Cromo (Cr)
    ]
)

print("MATRIZ ESTEQUIOMÉTRICA ORIGINAL (5 elementos x 4 especies):")
sp.pprint(A_quimica)

# 2. Reducción a la Forma Escalonada Reducida por Filas (RREF)
# rref() devuelve una tupla: (matriz_reducida, indices_columnas_pivote)
rref_matriz, pivotes = A_quimica.rref()

print("\n--- FORMA ESCALONADA REDUCIDA POR FILAS (RREF) ---")
sp.pprint(rref_matriz)
print(f"Columnas con pivote (variables dependientes): {pivotes}")

# 3. Detección de variables libres y cálculo del espacio nulo
columnas_totales = A_quimica.shape[1]
variables_libres = [
    col for col in range(columnas_totales) if col not in pivotes
]
print(f"Columnas libres (grados de libertad): {variables_libres}")

# nullspace() halla la base del Kernel del sistema homogéneo A * x = 0
espacio_nulo = A_quimica.nullspace()
vector_parametrico = espacio_nulo[0]

print("\nVector base del espacio nulo (Solución paramétrica en fracciones):")
sp.pprint(vector_parametrico)

# 4. Obtención de los coeficientes estequiométricos enteros mínimos
# Buscamos el mínimo común múltiplo (MCM) de los denominadores para eliminar fracciones
denominadores = [sp.denom(val) for val in vector_parametrico]
mcm_denominadores = sp.lcm(denominadores)

coeficientes_enteros = vector_parametrico * mcm_denominadores

# Aseguramos que la solución sea estrictamente positiva
if coeficientes_enteros[0] < 0:
    coeficientes_enteros = -coeficientes_enteros

x1, x2, x3, x4 = coeficientes_enteros

print("\n========================================================")
print("             COEFICIENTES ESTEQUIOMÉTRICOS BALANCEADOS   ")
print("========================================================")
print(f"x1 (AgNO3)    : {x1}")
print(f"x2 (K2CrO4)   : {x2}")
print(f"x3 (Ag2CrO4)  : {x3}")
print(f"x4 (KNO3)     : {x4}")

ecuacion_quimica = f"{x1} AgNO3 + {x2} K2CrO4 -> {x3} Ag2CrO4 + {x4} KNO3"
print(f"\nEcuación final balanceada:\n{ecuacion_quimica}")