# Método de Neville para interpolación
import numpy as np
import matplotlib.pyplot as plt

# 1. DATOS DE ENTRADA
# Corregimos los arreglos para que tengan el mismo tamaño (5 puntos)
# Queremos aproximar la función Gamma/Factorial. Datos: (x, x!)
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([1.0, 2.0, 6.0, 24.0, 120.0]) # 1!, 2!, 3!, 4!, 5!
n = x.size

# Creamos la tabla de Neville vacía (Matriz de n x n)
G = np.zeros((n, n))

# Valor que queremos calcular (en este caso, pi)
xi = np.pi 

# 2. ALGORITMO DE NEVILLE
# Paso A: La primera columna de la tabla son simplemente los valores de 'y' conocidos
G[:, 0] = y

# Paso B: Llenamos el resto de la tabla de forma dinámica
for j in range(1, n):
    for i in range(j, n):
        # Esta es la fórmula matemática de Neville que combina aproximaciones anteriores
        numerador = (xi - x[i-j]) * G[i, j-1] - (xi - x[i]) * G[i-1, j-1]
        denominador = x[i] - x[i-j]
        G[i, j] = numerador / denominador

# El resultado final de la interpolación es el último elemento calculado (esquina inferior derecha)
yi = G[n-1, n-1]

# 3. IMPRESIÓN DE RESULTADOS
print("=== TABLA DE NEVILLE ===")
# Formateamos la matriz para que se vea bonita con 4 decimales
print(np.round(G, 4))
print(f"\nEl valor aproximado de {xi:.4f}! usando Neville es: {yi:.4f}")

# 4. GRAFICAR RESULTADOS
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'ob-', label='Datos conocidos (n!)', markersize=8)
plt.plot(xi, yi, 'sr', label=f'Aproximación de pi! ({yi:.2f})', markersize=10)
plt.text(xi + 0.1, yi - 10, f'  ! ≈ {yi:.4f}', color='red', weight='bold')
plt.title('Interpolación del Factorial usando el Método de Neville')
# Ajustamos los límites para que la gráfica se vea centrada y clara
plt.xlim(0, 6)
plt.ylim(-5, 140)
plt.xlabel('n')
plt.ylabel('n!')
plt.legend()
plt.grid(True, linestyle='--')
plt.show()