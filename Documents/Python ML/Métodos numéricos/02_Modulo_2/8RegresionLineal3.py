import numpy as np
import matplotlib.pyplot as plt

"""
Conexión entre la regresión lineal y el perceptrón lineal (neurona simple).

Este ejemplo muestra cómo los coeficientes de una regresión lineal (pendiente
y ordenada en el origen) pueden interpretarse como `peso` y `bias` en una
neurona lineal. Es útil para explicar a estudiantes de IA la relación entre
modelos estadísticos clásicos y modelos simples de redes neuronales.
"""

# Datos: dureza (x) vs deformación (y)
x = np.array([6, 9, 11, 13, 22, 26, 28, 33, 35])
y = np.array([68, 67, 65, 53, 44, 40, 37, 34, 32])

# En un ejemplo previo calculamos (con linregress) aproximadamente:
# pendiente m ≈ -1.3323  -> lo interpretamos como peso (w)
# ordenada b ≈ 78.4116  -> lo interpretamos como sesgo/bias
# Aquí los fijamos manualmente para demostrar equivalencia.
peso_w = -1.3323      # w (peso) equivalente a la pendiente m
sesgo_bias = 78.4116  # b (bias) equivalente a la ordenada en el origen


def perceptron_lineal(entrada_x):
    """
    Simula una neurona lineal (perceptrón sin función de activación no lineal).

    Fórmula: salida = entrada_x * peso_w + sesgo_bias

    Parámetros:
    - entrada_x: array o valor escalar de la variable de entrada (x)

    Retorna:
    - salida: valor(es) predichos por la neurona para la(s) entrada(s)
    """
    salida = (entrada_x * peso_w) + sesgo_bias
    return salida


# Evaluamos la 'neurona' sobre las durezas originales
y_neurona = perceptron_lineal(x)

print('--- SALIDA DE LA NEURONA ARTIFICIAL (PERCEPTRÓN) ---')
print('Predicciones del Perceptrón para cada Dureza:', y_neurona, sep='\n')

# Graficamos para comparar: puntos reales vs predicción de la neurona
plt.plot(x, y, 'o', label='Datos Reales')
plt.plot(x, y_neurona, 'b--', label='Predicción del Perceptrón (y = x·w + b)')
plt.title('Conexión con IA: Perceptrón y parámetros numéricos')
plt.xlabel('Dureza (Entrada)')
plt.ylabel('Deformación (Salida)')
plt.legend()
plt.grid(True)
plt.show()