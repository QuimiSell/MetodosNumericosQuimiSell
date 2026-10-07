import numpy as np
import matplotlib.pyplot as plt

print("==========================================================")
print("   CLASE 11: SCRIPT DE REGRESIÓN LINEAL MÚLTIPLE (MCO)    ")
print("==========================================================\n")

# 1. BASE DE DATOS (Modificable por el estudiante)
# X1: Humedad (%), X2: Temperatura (°C), Y: Presión de Gas (kPa)
x1 = np.array([45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0])
x2 = np.array([22.0, 24.0, 21.0, 25.0, 28.0, 26.0, 29.0])
y = np.array([101.3, 102.1, 100.9, 103.4, 104.2, 103.9, 105.1])
n = len(y)

# 2. CONSTRUCCIÓN MATRICIAL (Forma Cerrada)
# Creamos la matriz de diseño X agregando una columna de 1s para el intercepto (Beta_0)
X = np.vstack([np.ones(n), x1, x2]).T
Y = y.reshape(-1, 1)

# 3. SOLUCIÓN ANALÍTICA VÍA ECUACIONES NORMALES: Beta = (X^T * X)^(-1) * X^T * Y
XtX = np.dot(X.T, X)
XtY = np.dot(X.T, Y)
beta = np.dot(np.linalg.inv(XtX), XtY)

# Extracción de coeficientes para la interpretación del alumno
beta_0 = beta[0][0]
beta_1 = beta[1][0]
beta_2 = beta[2][0]

print("--- COEFICIENTES ESTIMADOS (MÍNIMOS CUADRADOS) ---")
print(f"Beta_0 (Intercepto/Bias)        : {beta_0:.4f}")
print(f"Beta_1 (Pendiente Humedad X1)    : {beta_1:.4f}")
print(f"Beta_2 (Pendiente Temperatura X2): {beta_2:.4f}")
print(f"Ecuación del Modelo: Y = {beta_0:.4f} + ({beta_1:.4f})*X1 + ({beta_2:.4f})*X2\n")

# 4. FASE DE PREDICCIÓN (INFERENCIA CON NUEVOS DATOS)
# Caso de estudio: Predecir la presión con Humedad = 62% y Temperatura = 27°C
x1_nuevo = 62.0
x2_nuevo = 27.0
y_predicho = beta_0 + (beta_1 * x1_nuevo) + (beta_2 * x2_nuevo)

print("--- FASE DE PREDICCIÓN (INFERENCIA) ---")
print(f"Nuevas entradas -> Humedad: {x1_nuevo}%, Temperatura: {x2_nuevo}°C")
print(f"Resultado de la predicción (Y estimada): {y_predicho:.4f} kPa\n")

# 5. VISUALIZACIÓN CIENTÍFICA EN 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Puntos reales observados
ax.scatter(x1, x2, y, color='red', s=60, label='Datos Históricos (Muestras)')

# Punto nuevo predicho
ax.scatter(x1_nuevo, x2_nuevo, y_predicho, color='black', marker='X', s=150, label='Predicción del Modelo')

# Generación del plano de regresión
x1_r, x2_r = np.meshgrid(np.linspace(min(x1)-2, max(x1)+2, 10), np.linspace(min(x2)-2, max(x2)+2, 10))
y_plano = beta_0 + beta_1 * x1_r + beta_2 * x2_r
ax.plot_surface(x1_r, x2_r, y_plano, alpha=0.3, cmap='viridis')

# Etiquetas del gráfico
ax.set_xlabel('Humedad (%)')
ax.set_ylabel('Temperatura (°C)')
ax.set_zlabel('Presión (kPa)')
ax.set_title('Plano de Regresión Lineal Múltiple e Inferencia')
ax.legend()
plt.show()