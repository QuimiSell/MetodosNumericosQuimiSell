import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Este script compara dos formas de aproximar datos:
# 1) Interpolación lineal: une cada par de puntos vecinos con segmentos rectos.
# 2) Regresión lineal: ajusta una sola recta que mejor describe la tendencia general.

# Datos del experimento o del libro: dureza frente a deformación.
# x = valores independientes (dureza)
# y = valores dependientes (deformación)
x = np.array([6, 9, 11, 13, 22, 26, 28, 33, 35])
y = np.array([68, 67, 65, 53, 44, 40, 37, 34, 32])

# Creamos un conjunto de puntos uniforme para graficar las curvas suavemente.
# np.linspace genera 100 puntos entre 6 y 35.
xs = np.linspace(6, 35, 100)

# Interpolación lineal:
# interp1d construye una función que interpola los valores de y en los puntos x.
# kind='linear' significa que se conectan los puntos con segmentos rectos.
f_interp = interp1d(x, y, kind='linear')

# Regresión lineal:
# np.polyfit ajusta un polinomio de grado 1 (recta) a los datos.
# El resultado p_regresion contiene los coeficientes [pendiente, ordenada_en_el_origen].
p_regresion = np.polyfit(x, y, 1)

# Graficamos los datos originales como puntos.
plt.plot(x, y, 'o', label='Datos Originales')

# Usamos la función de interpolación con los puntos densos xs.
# Esto dibuja la curva de interpolación lineal.
plt.plot(xs, f_interp(xs), 'g--', label='Interpolación Lineal')

# Usamos np.polyval para evaluar la recta de regresión en los puntos xs.
# Esto dibuja la línea de tendencia que mejor ajusta todos los datos.
plt.plot(xs, np.polyval(p_regresion, xs), 'r:', label='Regresión Lineal')

# Añadimos título, etiquetas y leyenda para clarificar la comparación.
plt.title('Subtema 2.1: Interpolación vs Regresión')
plt.xlabel('Dureza')
plt.ylabel('Deformación')
plt.legend()
plt.grid(True)

# Muestra la ventana de la gráfica.
plt.show()