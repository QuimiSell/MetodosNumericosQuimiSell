
import numpy as np  # NumPy: Proporciona estructuras de datos indexadas (arreglos) optimizadas en C para alto rendimiento.
from scipy import interpolate  # SciPy: Módulo específico con algoritmos matemáticos avanzados (en este caso, interpolación).
import matplotlib.pyplot as plt  # Matplotlib: Submódulo pyplot encargado de la generación y renderizado de gráficos.

# 1. ENTRADA DE DATOS (Muestreo discretclo de la Función de Runge)
# x: Representa los puntos medidos u observados en el eje independiente.
x = np.array([-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
# y: Son los valores que toma la función original para cada valor de 'x'.
y = np.array([0.03846, 0.06639, 0.13793, 0.39024, 1.0, 0.39024, 0.13793, 0.06639, 0.03846])

# 2. DEFINICIÓN DEL MODELO MATEMÁTICO
# 'interp1d' genera una función ejecutable en Python basada en los datos (x,y).
# El argumento kind='nearest' le indica a SciPy que aplique la regla del vecino más cercano.
# No computa polinomios; solo busca qué coordenada conocida en 'X' está más cerca de la consulta y hereda su 'Y'.
f = interpolate.interp1d(x, y, kind='nearest')

# 3. EVALUACIÓN DE UN RANGO CONTINUO (Para graficar los escalones)
# Generamos 50 puntos distribuidos uniformemente entre -1 y 1 para mapear el comportamiento de la función 'f'.
xs = np.linspace(-1, 1, 50)
# 'ys' almacena el resultado de evaluar los 50 puntos en nuestro modelo de interpolación.
ys = f(xs)

# 4. CASO DE ESTUDIO ESPECÍFICO (Validación numérica)
# Evaluamos un valor exacto (xi = 0.85) para demostrar el criterio de cercanía.
xi = 0.85
# El valor de x mas cercano a 0.85 en nuestro conjunto original es 0.75 (distancia de 0.10).
# Por lo tanto, yi tomará exactamente el valor de y asignado a 0.75, el cual es 0.06639.
yi = f(xi)

# Imprime el resultado numérico directo en la consola.
print(f"Resultado Nearest en x=0.85: {yi}")

# 5. RENDERIZADO Y CONSTRUCCIÓN DE LA GRÁFICA
plt.plot(x, y, 'o', label='Datos')  # Puntos base originales
plt.plot(xi, yi, 'sr', label='Interpolación')  # Caso de prueba (0.85)
plt.plot(xs, ys, 'r:', label='Nearest')  # Línea de escalones
plt.title('$f(x)=1/(1+25x^2)$')  
plt.legend()  
plt.grid(True)  

# --- AGREGA ESTA LÍNEA AQUÍ ---
plt.show()  # Levanta la interfaz gráfica de Matplotlib en tu sistema operativo

# Puedes dejar o quitar esta línea si ya no necesitas el archivo físico:
plt.savefig('nearest_interpolation.png')