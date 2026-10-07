"""
===============================================================================
CLASE 25 - INTRODUCCIÓN: ¿Cómo se Discretiza una Ecuación de Derivadas Parciales?
===============================================================================
Propósito:
  Mostrar el salto conceptual de EDOs (1 variable independiente: t) a EDPs 
  (múltiples variables independientes: x y t) mediante la discretización de 
  segunda derivada en espacio y primera derivada en tiempo.

Problema:
  Ecuación de Advección/Difusión Simplificada 1D en x ∈ [0, L], t ∈ [0, T]
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# 1. EXPLICACIÓN FEYNMAN: EL PASO DE EDO A EDP EN UNA MALLA (GRID)
# -----------------------------------------------------------------------------
"""
¿QUÉ CAMBIA CUANDO PASAMOS DE UNA EDO A UNA EDP?

- En una EDO avanzamos en una sola dimensión (por ejemplo, el tiempo 't').
- En una EDP, la función u(x, t) cambia simultáneamente en ESPACIO (x) y TIEMPO (t).

¿CÓMO LO REPRESENTAMOS EN CÓDIGO?
En lugar de un arreglo 1D (vector), creamos una MALLA (Matriz 2D) donde:
  - Las filas representan el TIEMPO (índice n)
  - Las columnas representan el ESPACIO (índice i)

Para la segunda derivada espacial (Curvatura):
  ∂²u/∂x² ≈ (u_{i+1}^n - 2*u_i^n + u_{i-1}^n) / (dx²)

Para la primera derivada temporal (Cambio en el tiempo):
  ∂u/∂t ≈ (u_i^{n+1} - u_i^n) / dt

Al despejar u_i^{n+1} (el futuro), obtenemos una regla explícita que calcula el
nuevo valor usando el nodo actual y sus dos vecinos espaciales inmediatos.
"""


def resolver_edp_basica():
    # Parámetros del dominio
    L = 1.0          # Longitud espacial [m]
    T_final = 0.1    # Tiempo total [s]
    alpha = 0.01     # Difusividad [m²/s]

    Nx = 20          # Puntos en espacio
    Nt = 100         # Puntos en tiempo

    dx = L / (Nx - 1)
    dt = T_final / Nt
    r = alpha * dt / (dx**2)

    x = np.linspace(0, L, Nx)
    u = np.zeros((Nt, Nx))

    # Condición Inicial: Pulso térmico en el centro
    u[0, :] = np.sin(np.pi * x)

    # Condiciones de Frontera Dirichlet (Extremos fijos a 0)
    u[:, 0] = 0.0
    u[:, -1] = 0.0

    # Bucle en tiempo (Avanzando nivel por nivel)
    for n in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            u[n + 1, i] = u[n, i] + r * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

    print("=" * 65)
    print(" DISCRETIZACIÓN BÁSICA DE EDP (Malla de Espacio-Tiempo)")
    print("=" * 65)
    print(f" Dimensión Espacial (Nx): {Nx} | Paso dx: {dx:.4f}")
    print(f" Dimensión Temporal (Nt): {Nt} | Paso dt: {dt:.4f}")
    print(f" Parámetro de malla (r): {r:.4f}")
    print("=" * 65)

    # Visualización de la Malla Espacio-Tiempo
    plt.figure(figsize=(9, 5))
    plt.imshow(u, aspect='auto', extent=[0, L, T_final, 0], cmap='viridis')
    plt.colorbar(label='Temperatura $u(x,t)$')
    plt.title('Evolución de $u(x,t)$ en la Malla Espacio-Tiempo', fontsize=12)
    plt.xlabel('Espacio $x$ [m]', fontsize=11)
    plt.ylabel('Tiempo $t$ [s]', fontsize=11)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    resolver_edp_basica()