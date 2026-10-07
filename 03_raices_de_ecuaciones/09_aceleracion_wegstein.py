"""
LIBRERÍAS DE CÁLCULO CIENTÍFICO:
- NumPy: Estructuras numéricas eficientes.
- Matplotlib: Representación de convergencia acelerada.
- SciPy: SciPy no implementa Wegstein directamente, demostrando la necesidad
  de programar aceleraciones personalizadas sobre punto fijo.
"""

import matplotlib.pyplot as plt
import numpy as np


def g(x):
    # Función de iteración simple
    return np.exp(-x)


def wegstein(x0, tol=1e-6, max_iter=100):
    # CONCEPTO FEYNMAN: El empujón de Wegstein.
    # El punto fijo estándar puede ser muy lento (dar pasos diminutos de bebé).
    # Wegstein evalúa la tendencia del cambio entre los últimos dos pasos
    # y calcula un factor 'w' de aceleración para "empujar" la suposición
    # directamente hacia donde proyecta que estará la solución final.

    print("-" * 65)
    print(
        f"{'Iteración':<10} | {'x_k':<15} | {'Error Absoluto':<15} | {'g(x_k)':<15}"
    )
    print("-" * 65)

    # Paso 1: Primer punto mediante punto fijo simple
    x1 = g(x0)
    print(f"{1:<10} | {x0:<15.8f} | {abs(x1 - x0):<15.8e} | {x1:<15.8f}")

    x_prev = x0
    x_curr = x1

    for i in range(2, max_iter + 1):
        y_prev = g(x_prev)
        y_curr = g(x_curr)

        # Pendiente de la función de iteración entre las dos últimas iteraciones
        q = (y_curr - y_prev) / (x_curr - x_prev)

        # Factor de aceleración de Wegstein
        w = q / (q - 1.0)

        # Actualización acelerada: mezcla ponderada
        x_next = (1.0 - w) * x_curr + w * y_curr
        error = abs(x_next - x_curr)

        print(
            f"{i:<10} | {x_curr:<15.8f} | {error:<15.8e} | {y_curr:<15.8f}"
        )

        if error < tol:
            print("-" * 65)
            print(f"Convergencia acelerada alcanzada en la iteración {i}.")
            return x_next

        x_prev = x_curr
        x_curr = x_next

    return x_curr


# Ejecución
x0 = 0.0
raiz = wegstein(x0)

# Gráfica
x_vals = np.linspace(-0.2, 1.2, 200)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, x_vals, label="y = x", color="gray")
plt.plot(x_vals, g(x_vals), label="y = e^(-x)", color="green")
plt.plot(
    raiz,
    g(raiz),
    "ro",
    label=f"Raíz (Acelerada por Wegstein) ≈ {raiz:.5f}",
)
plt.axvline(x=raiz, color="red", linestyle="--", alpha=0.5)
plt.title("Aceleración de Wegstein sobre Iteración de Punto Fijo")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()