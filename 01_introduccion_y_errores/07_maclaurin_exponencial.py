import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
n = 5
x = sp.Symbol('x')

t_expr = sp.exp(x).series(x, x0, n).removeO()
print(f"Polinomio aproximado (orden {n}) alrededor de x0={x0}: {t_expr}")
t_func = sp.lambdify(x, t_expr, 'numpy')

xx = np.linspace(-4, 4, 100)
plt.plot(xx, np.exp(xx), label='e^x Real')
plt.plot(xx, t_func(xx), '--', label='Serie de Taylor')
plt.title('Aproximación de la función exponencial e^x')
plt.legend()
plt.grid(True)
plt.show()
