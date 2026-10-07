"""
Clase 21 - Script 2: Simpson 1/3, Simpson 3/8 y Grafica Comparativa
Compara la aproximacion de una funcion cuadratica a trozos vs la curva continua.

EXPLICACION (ESTILO FEYNMAN):
1. Simpson 1/3 usa parabolas (grado 2). Cada parabola requiere 3 nodos (2 paneles).
   Por eso el numero de paneles n DEBE ser PAR.
2. Pesos (1, 4, 2, 4, ..., 1): El vertice de cada parabola se evalua una vez (peso 4).
   El punto frontera compartido entre dos parabolas se suma dos veces: 1 + 1 = 2.
3. Si n es impar: Simpson 3/8 toma los primeros 3 paneles (polinomio cubico),
   y Simpson 1/3 se encarga de los paneles pares restantes.
4. Precision O(h^4): Por simetria respecto al nodo central, el error cubico se anula.
   Esto permite que polinomios cubicos se integren de forma EXACTA.
"""

import matplotlib.pyplot as plt
import numpy as np


def simpson_13_compuesto(f, a, b, n):
    if n <= 0 or n % 2 != 0:
        raise ValueError("n debe ser par y mayor que 0.")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 3.0) * (
        y[0] + 4.0 * np.sum(y[1:-1:2]) + 2.0 * np.sum(y[2:-1:2]) + y[-1]
    )


def simpson_38_simple(f, a, b):
    h = (b - a) / 3.0
    x = np.linspace(a, b, 4)
    y = f(x)
    return (3.0 * h / 8.0) * (y[0] + 3.0 * y[1] + 3.0 * y[2] + y[3])


def simpson_adaptativo_impar(f, a, b, n):
    if n < 2:
        raise ValueError("Se requieren al menos 2 subintervalos.")
    h = (b - a) / n
    if n % 2 == 0:
        return simpson_13_compuesto(f, a, b, n)
    elif n == 3:
        return simpson_38_simple(f, a, b)
    else:
        x_corte = a + 3.0 * h
        return simpson_38_simple(f, a, x_corte) + simpson_13_compuesto(
            f, x_corte, b, n - 3
        )


# Prueba con funcion trascendente
g = lambda x: np.exp(x) * np.cos(x)
g_antiderivada = lambda x: 0.5 * np.exp(x) * (np.sin(x) + np.cos(x))
a2, b2 = 0.0, np.pi
exacta = g_antiderivada(b2) - g_antiderivada(a2)

print("=====================================================================")
print("CONVERGENCIA SIMPSON ADAPTATIVO: exp(x)*cos(x)")
print(f"Intervalo: [{a2:.2f}, {b2:.4f}] | Valor exacto: {exacta:.10f}")
print("=====================================================================")
print(
    f"{'n':>4} | {'h':>8} | {'Estrategia':>16} | {'Aproximacion':>14} | {'Error Abs':>12}"
)
print("-" * 65)

for n in [3, 4, 5, 6, 7, 10, 20]:
    h = (b2 - a2) / n
    estrategia = (
        "1/3 puro"
        if n % 2 == 0
        else ("3/8 puro" if n == 3 else "3/8 + 1/3")
    )
    aprox = simpson_adaptativo_impar(g, a2, b2, n)
    print(
        f"{n:4d} | {h:8.4f} | {estrategia:>16} | {aprox:14.8f} | {abs(exacta - aprox):12.4e}"
    )
print("=====================================================================")

# Visualizacion grafica de ajuste parabolico con n = 4 (dos parabolas)
n_plot = 4
x_nodos = np.linspace(a2, b2, n_plot + 1)
y_nodos = g(x_nodos)
x_denso = np.linspace(a2, b2, 500)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x_denso, g(x_denso), "b-", linewidth=2, label="Curva Real g(x)")
ax.scatter(x_nodos, y_nodos, color="black", s=45, zorder=5, label="Nodos")

# Construccion de las 2 parabolas de interpolacion de Lagrange (pares de paneles)
for i in range(0, n_plot, 2):
    xs = x_nodos[i : i + 3]
    ys = y_nodos[i : i + 3]
    # Polinomio cuadratico que pasa por los 3 puntos
    coefs = np.polyfit(xs, ys, deg=2)
    poly = np.poly1d(coefs)

    x_segmento = np.linspace(xs[0], xs[-1], 100)
    y_segmento = poly(x_segmento)

    ax.plot(x_segmento, y_segmento, "r--", linewidth=1.8)
    ax.fill_between(
        x_segmento,
        0,
        y_segmento,
        color="red",
        alpha=0.18,
        label="Area Parabolica" if i == 0 else "",
    )
    ax.vlines(
        x=xs[0], ymin=0, ymax=ys[0], color="gray", linestyle=":", alpha=0.6
    )

ax.vlines(
    x=x_nodos[-1],
    ymin=0,
    ymax=y_nodos[-1],
    color="gray",
    linestyle=":",
    alpha=0.6,
)
ax.set_title(
    f"Regla de Simpson 1/3 (n={n_plot}) - Interpolacion Parabolica a Trozos",
    fontsize=12,
    fontweight="bold",
)
ax.set_xlabel("x")
ax.set_ylabel("g(x)")
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="lower left")
plt.tight_layout()
plt.show()