"""
LIBRERÍAS DE CÁLCULO CIENTÍFICO:
- NumPy: Cálculo vectorial de alto rendimiento.
- Matplotlib: Visualización geométrica de la raíz.
- SciPy (scipy.optimize.newton con fprime=None): Algoritmo de secante optimizado para producción.
"""

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    # Función original f(x) = 0
    return x**3 - x - 2


def secante(x0, x1, tol=1e-6, max_iter=100):
    # CONCEPTO FEYNMAN: Triangulación sin derivadas.
    # El método de Newton requiere la derivada exacta. Si no la tenemos,
    # tomamos dos puntos iniciales y trazamos una recta secante entre ellos.
    # Dónde esa recta corta el suelo (eje X) es nuestra nueva mejor suposición.

    print("-" * 65)
    print(
        f"{'Iteración':<10} | {'x_k':<15} | {'Error Absoluto':<15} | {'f(x_k)':<15}"
    )
    print("-" * 65)

    for i in range(1, max_iter + 1):
        f_x0 = f(x0)
        f_x1 = f(x1)

        # Prevenimos división por cero si la pendiente es plana
        denominador = f_x1 - f_x0
        if abs(denominador) < 1e-12:
            print("Error: Pendiente de secante nula. No se puede dividir.")
            return None

        # Fórmula de interpolación lineal proyectada al eje X
        x_next = x1 - f_x1 * (x1 - x0) / denominador
        error = abs(x_next - x1)

        print(
            f"{i:<10} | {x1:<15.8f} | {error:<15.8e} | {f_x1:<15.8f}"
        )

        if error < tol:
            print("-" * 65)
            print(f"Convergencia alcanzada en la iteración {i}.")
            return x_next

        # Actualizamos puntos para la siguiente iteración
        x0 = x1
        x1 = x_next

    return x1


# Ejecución con puntos iniciales x0=1 y x1=2
x0, x1 = 1.0, 2.0
raiz = secante(x0, x1)

# Gráfica
x_vals = np.linspace(0, 2.5, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, f(x_vals), label="f(x) = x^3 - x - 2", color="blue")
plt.axhline(0, color="black", linestyle="--", linewidth=1)  # Eje X
plt.plot(
    raiz, 0, "ro", label=f"Raíz Encontrada ≈ {raiz:.5f}"
)  # Punto sobre el eje X
plt.title("Método de la Secante: Búsqueda del cruce por cero")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()