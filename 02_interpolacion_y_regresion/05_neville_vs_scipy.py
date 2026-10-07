
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

# Datos del problema de Runge (usados como ejemplo en el libro)
x = np.array([-1.0, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1.0])
y = np.array([0.03846, 0.06639, 0.13793, 0.39024, 1, 0.39024, 0.13793, 0.06639, 0.03846])

# 1. Creación de la función de interpolación de spline cúbico
# El parámetro 'cubic' le indica a SciPy que use polinomios de tercer grado
f = interpolate.interp1d(x, y, kind='cubic')

# 2. Generar puntos más finos para graficar la suavidad de la curva
xs = np.linspace(-1, 1, 50)
ys = f(xs)

# 3. Interpolar un punto específico (ejemplo: x = 0.85)
xi = 0.85
yi = f(xi)

print(f"La aproximación en x={xi} usando Spline Cúbico es: {yi}")

# 4. Graficar resultados
plt.plot(x, y, 'o', label='Datos reales')
plt.plot(xi, yi, 'sr', label='Dato interpolado')
plt.plot(xs, ys, 'r:', label='Spline Cúbico')
plt.text(xi + 0.05, yi, 'interpolación ' + str(yi))
plt.title('$f(x)=1/(1+25x^2)$')
plt.legend()
plt.grid(True)
plt.show()