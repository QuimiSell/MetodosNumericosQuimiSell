# Cos(x) alrededor de x=0 usando la serie de Taylor (Maclaurin)
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0 = 0 # Punto de expansión
n = 7  # Orden de la serie
x = sp.Symbol('x')

# Generar la serie y remover el término de error O(x^n)
t_expr = sp.cos(x).series(x, x0, n).removeO()
print(f"Polinomio aproximado: {t_expr}")

# Convertir a función de numpy para graficar
t_func = sp.lambdify(x, t_expr, 'numpy')

xx = np.linspace(-5, 5, 1000)
plt.plot(xx, np.cos(xx), label='cos(x) Real')
plt.plot(xx, t_func(xx), '--', label=f'Serie de Taylor (Orden {n})')
plt.axvline(x=0, color='k', alpha=0.3)
plt.title('Aproximación de cos(x)')
plt.legend()
plt.grid(True)
plt.show()
