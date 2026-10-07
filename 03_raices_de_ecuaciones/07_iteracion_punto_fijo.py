"""
LIBRERÍAS DE CÁLCULO CIENTÍFICO:
- NumPy: Utilizado para operaciones matriciales/vectoriales eficientes en memoria C.
- Matplotlib: Generación de gráficos e inspección visual de convergencia.
- SciPy (scipy.optimize.fixed_point): Estándar industrial optimizado para este método.
"""

import matplotlib.pyplot as plt
import numpy as np


def g(x):
    # La función trasformada x = g(x)
    return np.cos(x)


def d_g(x):
    # Derivada de g(x) para validar la condición de convergencia
    return -np.sin(x)


def punto_fijo(x0, tol=1e-6, max_iter=100):
    # CONCEPTO FEYNMAN: Condición de atracción.
    # Imagina que la función es un embudo. Si la pendiente |g'(x)| < 1,
    # cada paso te acerca más al fondo (la raíz). Si es > 1, te expulsa.
    condicion = abs(d_g(x0))
    print(f"Evaluación de convergencia en x0={x0}: |g'(x0)| = {condicion:.4f}")
    if condicion >= 1:
        print(
            "Advertencia: |g'(x)| >= 1. El método puede divergir o no estar garantizado."
        )

    print("-" * 60)
    print(
        f"{'Iteración':<10} | {'x_k':<15} | {'Error Absoluto':<15} | {'g(x_k)':<15}"
    )
    print("-" * 60)

    x_curr = x0
    for i in range(1, max_iter + 1):
        # Avanzamos evaluando la función en el punto actual
        x_next = g(x_curr)
        error = abs(x_next - x_curr)

        print(
            f"{i:<10} | {x_curr:<15.8f} | {error:<15.8e} | {x_next:<15.8f}"
        )

        if error < tol:
            print("-" * 60)
            print(f"Convergencia alcanzada en la iteración {i}.")
            return x_next

        x_curr = x_next

    return x_curr


# Ejecución
x0 = 0.5
raiz = punto_fijo(x0)

# Gráfica
x_vals = np.linspace(0, 1.2, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, x_vals, label="y = x (Línea de identidad)", color="gray")
plt.plot(x_vals, g(x_vals), label="y = cos(x)", color="blue")
plt.plot(
    raiz,
    g(raiz),
    "ro",
    label=f"Punto Fijo (Raíz) ≈ {raiz:.5f}",
)
plt.axvline(
    x=raiz, color="red", linestyle="--", alpha=0.5
)  # Proyección al eje X
plt.title("Método del Punto Fijo: Intersección y = g(x) con y = x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()