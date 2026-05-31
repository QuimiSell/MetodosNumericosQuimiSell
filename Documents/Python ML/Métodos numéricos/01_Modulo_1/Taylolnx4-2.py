import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x0 = 1 # Punto de expansión
n = 5
x = sp.Symbol('x')

t_expr = sp.log(x).series(x, x0, n).removeO()
print(f"Polinomio aproximado (orden {n}) alrededor de x0={x0}: {t_expr}")
t_func = sp.lambdify(x, t_expr, 'numpy')

xx = np.linspace(0.1, 3, 100) # Evitamos el cero
plt.plot(xx, np.log(xx), label='ln(x) Real')
plt.plot(xx, t_func(xx), '--', label='Aproximación Taylor')
plt.scatter([x0], [np.log(x0)], color='red', label='Punto de expansión (x0=1)')
plt.title('Aproximación de ln(x) alrededor de x=1')
plt.legend()
plt.grid(True)
plt.show()