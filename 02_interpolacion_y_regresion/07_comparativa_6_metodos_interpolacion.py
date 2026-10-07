import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# 1. ORIGEN DE DATOS
# Conjunto de 9 puntos discretos distribuidos simétricamente en el plano cartesiano.
x = np.array([-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
y = np.array([0.03846, 0.06639, 0.13793, 0.39024, 1.0, 0.39024, 0.13793, 0.06639, 0.03846])

# 2. CONFIGURACIÓN DE ALGORITMOS Y MUESTREO
# Tupla que define las 6 estrategias matemáticas de interpolación que soporta interp1d.
tipos = ('nearest', 'zero', 'linear', 'slinear', 'quadratic', 'cubic')
# Generación de 50 puntos de alta resolución para evaluar la suavidad de cada curva generada.
xs = np.linspace(-1, 1, 50)

# 3. CONSTRUCCIÓN DE LA COMPARATIVA VISUAL
# Inicializa el lienzo asignándole dimensiones explícitas en pulgadas (ancho, alto).
plt.figure(figsize=(10,6))

# Bucle de automatización: Se ejecuta una vez por cada uno de los 6 métodos de la tupla.
for tipo in tipos:
    # Genera dinámicamente el modelo matemático adaptado al método en turno.
    f = interpolate.interp1d(x, y, kind=tipo)
    # Evalúa los 50 puntos del rango 'xs' usando dicho modelo.
    ys = f(xs)
    # Dibuja la curva correspondiente en el gráfico asignándole el nombre del método como etiqueta.
    plt.plot(xs, ys, '-', label=tipo)

# 4. CAPA DE REFERENCIA Y METADATOS DEL GRÁFICO
# Superpone los puntos originales como círculos discretos para evaluar qué tan bien se adapta cada método a ellos.
plt.plot(x, y, 'o', label='Datos reales', color='black')
plt.title('Comparativa de los 6 Métodos de Interpolación') # Título principal del gráfico.
plt.legend()  # Despliega el cuadro de convenciones con los 6 métodos mas los puntos reales.
plt.grid(True) # Habilita la malla para el análisis visual de las coordenadas.

# 5. DESPLIEGUE EN INTERFAZ
# Levanta la ventana del sistema operativo con la gráfica interactiva en pantalla.
plt.show()