import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Datos: Meses (1 a 5) y Ventas (y)
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([1.1, 1.5, 12.8, 15.3, 15.5], dtype=float)
n = x.size
xi = 2.75 # Queremos saber la mitad del mes 2
yi = 0

# 1. Cálculo manual: El corazón de Lagrange
for i in range(0, n):
    # 'producto' es nuestro "Filtro" (L_i)
    # Empezamos en y[i] porque al final multiplicamos L_i * y_i
    filtro = y[i]
    for j in range(0, n):
        if i != j:
            # Esta es la fórmula: (x - xj) / (xi - xj)
            filtro = filtro * (xi - x[j]) / (x[i] - x[j])
    yi = yi + filtro

print(f"Resultado manual (Lagrange): {yi:.4f}")

# 2. Comparación con Scipy
# Scipy ya tiene esto optimizado, ideal para validar
poly_lagrange = interpolate.lagrange(x, y)
print(f"Resultado con Scipy: {poly_lagrange(xi):.4f}")

# 3. Gráfica para YouTube
x_curva = np.linspace(min(x), max(x), 100)
y_curva = poly_lagrange(x_curva) # Scipy nos permite evaluar toda la curva fácil

plt.figure(figsize=(10,6))
plt.plot(x, y, 'o', label='Datos Reales')
plt.plot(x_curva, y_curva, '--', label='Curva de Lagrange')
plt.plot(xi, yi, 'sr', label=f'Punto Interpolado ({xi})')
plt.title('Interpolación de Lagrange')
plt.legend()
plt.grid(True)
plt.show()