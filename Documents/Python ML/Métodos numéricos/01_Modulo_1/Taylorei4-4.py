# Aproximación de e^(ix) alrededor de x=0 usando la serie de Taylor
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x0 = 0
n = 8
x = sp.Symbol('x')

# Definir la exponencial compleja e^(ix)
t_expr = sp.series(sp.exp(1j*x), x, x0, n).removeO()
print(f"Polinomio aproximado de Taylor (orden {n}) alrededor de x0={x0}: {t_expr}")
t_func = sp.lambdify(x, t_expr, 'numpy')

xx = np.linspace(-4, 4, 100)
yc = np.exp(1j*xx) # Valor real
yt = t_func(xx)    # Aproximación de la serie

plt.figure(figsize=(6,6))
plt.plot(yc.real, yc.imag, label='e^{ix} Real (Círculo)')
plt.plot(yt.real, yt.imag, '--', label='Serie de Taylor Compleja')
plt.title('Plano Complejo: Serie de Taylor de e^{ix}')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginaria')
plt.legend()
plt.grid(True)
plt.show()