"""
Clase 21 - Script 1: Sumas de Riemann y Trapecio Compuesto
Funcion de Ingenieria: Flujo de calor f(x) = 300 + 50*sin(0.5*x)*exp(-0.1*x) en [0, 10]

EXPLICACION (ESTILO FEYNMAN):
1. Lagrange grado 1 une 2 puntos con una recta. Integrar esa recta da:
   Area_i = (h/2) * [f(x_i) + f(x_{i+1})].
2. Formula compuesta: los nodos internos se tocan dos veces (derecha de uno,
   izquierda del otro), por eso pesan el doble: (1, 2, 2, ..., 2, 1).
3. Error O(h^2): cada panel falla en O(h^3); al sumar (b-a)/h paneles,
   el error global se reduce a O(h^2).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad


def f(x):
    return 300.0 + 50.0 * np.sin(0.5 * x) * np.exp(-0.1 * x)


def riemann_rectangulos(f, a, b, n, modo="punto_medio"):
    h = (b - a) / n
    if modo == "punto_medio":
        x = np.linspace(a + h / 2.0, b - h / 2.0, n)
    elif modo == "izquierda":
        x = np.linspace(a, b - h, n)
    elif modo == "derecha":
        x = np.linspace(a + h, b, n)
    else:
        raise ValueError("Modo no valido")
    return np.sum(f(x)) * h


def trapecio_compuesto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2.0) * (y[0] + 2.0 * np.sum(y[1:-1]) + y[-1])


a, b = 0.0, 10.0
valor_exacto, _ = quad(f, a, b)
subintervalos = [2, 4, 10, 100]

print("=====================================================================")
print("TABLA DE CONVERGENCIA: TRAPECIO COMPUESTO")
print(f"Valor analitico de referencia: {valor_exacto:.8f}")
print("=====================================================================")
print(
    f"{'n':>5} | {'h':>8} | {'Trapecio':>14} | {'Error Abs':>12} | {'Riemann (PM)':>14}"
)
print("-" * 65)

for n in subintervalos:
    h = (b - a) / n
    i_trap = trapecio_compuesto(f, a, b, n)
    err = abs(valor_exacto - i_trap)
    i_rie = riemann_rectangulos(f, a, b, n, modo="punto_medio")
    print(f"{n:5d} | {h:8.4f} | {i_trap:14.8f} | {err:12.4e} | {i_rie:14.8f}")
print("=====================================================================")

# Grafica explicativa para YouTube (n = 4 para ver claramente los trapecios)
n_grafica = 4
x_trap = np.linspace(a, b, n_grafica + 1)
y_trap = f(x_trap)
x_fino = np.linspace(a, b, 500)
y_fino = f(x_fino)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_fino, y_fino, "b-", linewidth=2, label="Curva Real f(x)")
ax.scatter(x_trap, y_trap, color="red", s=40, zorder=5, label="Nodos de Muestreo")

# Relleno del area bajo los trapecios
ax.fill_between(
    x_trap,
    0,
    y_trap,
    color="orange",
    alpha=0.35,
    label=f"Trapecios (n={n_grafica})",
)

# Lineas divisorias de cada trapecio
for xi, yi in zip(x_trap, y_trap):
    ax.vlines(x=xi, ymin=0, ymax=yi, color="gray", linestyle="--", alpha=0.7)

ax.set_title(
    "Metodo del Trapecio Compuesto - Aproximacion Lineal a Trozos",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("Tiempo x [s]")
ax.set_ylabel("Flujo f(x)")
ax.set_xlim(a, b)
ax.set_ylim(bottom=0)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper right")
plt.tight_layout()
plt.show()