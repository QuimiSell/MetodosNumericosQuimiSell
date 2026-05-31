import numpy as np
import matplotlib.pyplot as plt

# 1. ENTRADA DE DATOS (Nuestros puntos conocidos)
# x: Meses o días, y: Ventas o rendimiento
x = np.array([1, 2, 4, 5, 6], dtype=float) 
y = np.array([1.1, 1.5, 12.8, 15.3, 15.5], dtype=float)
n = x.size

# 2. CONSTRUCCIÓN DE LA TABLA (El "cerebro" del método)
# Creamos una matriz de ceros y llenamos la primera columna con 'y'
t = np.zeros((n, n))
t[:, 0] = y

# Calculamos las diferencias divididas (Complejidad O(n^2))
for c in range(1, n):
    for r in range(0, n - c):
        t[r, c] = (t[r + 1, c - 1] - t[r, c - 1]) / (x[r + c] - x[r])

print("Tabla de Diferencias Divididas:")
print(t)

# 3. INTERPOLACIÓN (Buscamos el dato que falta)
xi = 3  # Queremos saber qué pasó en el punto 3
xt = 1
yi = t[0, 0] # Empezamos con el primer coeficiente

for k in range(0, n - 1):
    xt = xt * (xi - x[k])       # Acumula los productos (x - x0)(x - x1)...
    yi = yi + t[0, k + 1] * xt  # Suma el término correspondiente del polinomio

print(f"\nLa aproximación en x={xi} es y={yi:.4f}")

# 4. EXTRAPUNTOS PARA LA CURVA (Para que en YouTube se vea una curva suave)
x_curva = np.linspace(min(x), max(x), 100) # 100 puntos entre el inicio y el fin
y_curva = []

for p in x_curva:
    # Repetimos el cálculo para cada punto de la curva
    val_t = 1
    val_y = t[0, 0]
    for k in range(0, n - 1):
        val_t *= (p - x[k])
        val_y += t[0, k + 1] * val_t
    y_curva.append(val_y)

# 5. VISUALIZACIÓN
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', label='Datos Reales (Cierre de mes)')
plt.plot(x_curva, y_curva, '-', label='Polinomio de Newton (La tendencia)')
plt.plot(xi, yi, 'bs', label=f'Punto Interpolado (x={xi})')

plt.title('Interpolación de Newton: Predicción de Ventas')
plt.xlabel('Tiempo (Meses / Días)')
plt.ylabel('Valor (Ventas)')
plt.legend()
plt.grid(True)
plt.show()