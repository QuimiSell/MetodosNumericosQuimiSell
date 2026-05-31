import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

"""
Ejemplo: Ajuste de una recta por regresión lineal y visualización.

Este script muestra cómo usar `scipy.stats.linregress` para obtener la
recta de mejor ajuste (regresión lineal) entre dos variables y cómo
interpretar y graficar los resultados.
"""

# Datos de ejemplo: x = dureza (variable independiente),
# y = deformación (variable dependiente) obtenidos del libro/ejercicio.
x = np.array([6, 9, 11, 13, 22, 26, 28, 33, 35])
y = np.array([68, 67, 65, 53, 44, 40, 37, 34, 32])

# linregress calcula la regresión lineal simple y devuelve:
# slope: pendiente (m)
# intercept: ordenada en el origen (b)
# rvalue: coeficiente de correlación de Pearson (r)
# pvalue: valor-p para la hipótesis nula (pendiente = 0)
# stderr: error estándar de la pendiente
m, b, r, p, std_err = stats.linregress(x, y)

# Mostramos los parámetros más útiles para la interpretación:
print('Ordenada al origen:', b)       # b
print('Pendiente:', m)                # m
print('Coeficiente de correlación (r):', r)

# Construimos la predicción de y usando la recta: y_pred = m*x + b
# Esto representa la 'corrección' o ajuste lineal sobre los puntos originales.
y_pred = m * x + b
print('Datos corregidos (y_pred):', y_pred, sep='\n')

# Visualización:
# - puntos originales (datos reales)
# - línea de regresión (recta ajustada)
plt.plot(x, y, 'o', label='Datos originales')

# Para graficar la recta se puede usar los mismos puntos x o una 'malla'
# más fina. Aquí usamos los puntos originales para enfatizar el ajuste.
plt.plot(x, y_pred, 'r--', label='Regresión lineal (y = m x + b)')

plt.title('Ajuste por Regresión Lineal: Deformación vs Dureza')
plt.xlabel('Dureza')
plt.ylabel('Deformación')
plt.legend()
plt.grid(True)
plt.show()