import numpy as np
import matplotlib.pyplot as plt

print("==========================================================")
print(" CLASE 11: SCRIPT DE REGRESIÓN NO LINEAL MÚLTIPLE (POL)   ")
print("==========================================================\n")

# 1. BASE DE DATOS (Comportamiento con curvatura en el espacio)
x1 = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0])
x2 = np.array([2.0, 3.0, 5.0, 6.0, 5.0, 8.0, 9.0])
y = np.array([4.2, 7.5, 12.1, 16.8, 19.0, 24.3, 28.1])
n = len(y)

# 2. EXPANSIÓN NO LINEAL DE LA MATRIZ DE DISEÑO
# El orden estricto de las columnas es: [1, X1, X2, X1^2, X2^2, X1*X2]
X = np.vstack([np.ones(n), x1, x2, x1**2, x2**2, x1*x2]).T
Y = y.reshape(-1, 1)

# 3. SOLUCIÓN ANALÍTICA MEDIANTE ECUACIONES NORMALES
XtX = np.dot(X.T, X)
XtY = np.dot(X.T, Y)
beta = np.dot(np.linalg.inv(XtX), XtY).flatten()  # Lo aplanamos a 1D para manipular los índices fácilmente

print("--- COEFICIENTES DEL PARABOLOIDE DE AJUSTE ---")
for i, b in enumerate(beta):
    print(f"Beta_{i}: {b:.4f}")
print(f"\nEcuación matemática resultante:\n"
      f"Y = {beta[0]:.4f} + {beta[1]:.4f}*X1 + {beta[2]:.4f}*X2 + {beta[3]:.4f}*X1² + {beta[4]:.4f}*X2² + {beta[5]:.4f}*X1X2\n")

# 4. FASE DE PREDICCIÓN (INFERENCIA MATRICIAL NO LINEAL)
# Caso de estudio: Predecir el valor de Y cuando X1 = 4.5 y X2 = 5.5
x1_n = 4.5
x2_n = 5.5

# Construimos el vector de entrada expandido exactamente igual que la matriz de diseño
vector_nuevo = np.array([1, x1_n, x2_n, x1_n**2, x2_n**2, x1_n * x2_n])

# Calculamos la inferencia mediante el producto punto (Multiplicación matricial simplificada)
y_predicho_nl = np.dot(vector_nuevo, beta)

print("--- FASE DE PREDICCIÓN (INFERENCIA NO LINEAL) ---")
print(f"Nuevas entradas -> X1: {x1_n}, X2: {x2_n}")
print(f"Resultado de la predicción (Y estimada): {y_predicho_nl:.4f}\n")

# 5. VISUALIZACIÓN DE LA SUPERFICIE CURVA EN 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Puntos reales observados
ax.scatter(x1, x2, y, color='blue', s=60, label='Datos Históricos')

# Punto nuevo predicho
ax.scatter(x1_n, x2_n, y_predicho_nl, color='black', marker='X', s=150, label='Predicción No Lineal')

# Generación de la superficie del paraboloide de regresión
x1_r, x2_r = np.meshgrid(np.linspace(min(x1)-1, max(x1)+1, 15), np.linspace(min(x2)-1, max(x2)+1, 15))
y_superficie = (beta[0] + beta[1]*x1_r + beta[2]*x2_r + 
                beta[3]*(x1_r**2) + beta[4]*(x2_r**2) + beta[5]*(x1_r*x2_r))
ax.plot_surface(x1_r, x2_r, y_superficie, alpha=0.3, cmap='plasma')

# Etiquetas del gráfico
ax.set_xlabel('Variable X1')
ax.set_ylabel('Variable X2')
ax.set_zlabel('Variable Y')
ax.set_title('Superficie de Regresión No Lineal e Inferencia')
ax.legend()
plt.show()