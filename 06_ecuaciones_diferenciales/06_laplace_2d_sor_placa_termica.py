"""
===============================================================================
CLASE 25 - PARTE 1: Ecuación de Laplace 2D (Estado Estacionario) y Método SOR
===============================================================================
Propósito:
  Resolver ∇²T = 0 en una placa metálica 2D con Condiciones Dirichlet.
  Demostrar cómo la sobre-relajación sucesiva (SOR) acelera la convergencia.
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# 1. EXPLICACIÓN FEYNMAN: PROMEDIO DE 4 VECINOS Y ACELERACIÓN SOR
# -----------------------------------------------------------------------------
"""
¿POR QUÉ CADA NODO ES EL PROMEDIO DE SUS 4 VECINOS?

En estado estacionario (∂T/∂t = 0), la Ecuación de Laplace 2D es:
   ∂²T/∂x² + ∂²T/∂y² = 0

Al discretizar con diferencias finitas centradas igualando dx = dy:
   (T_{i+1, j} - 2*T_{i,j} + T_{i-1, j}) + (T_{i, j+1} - 2*T_{i,j} + T_{i, j-1}) = 0

Despejando T_{i,j}:
   T_{i,j} = (T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1}) / 4

¡Físicamente significa que en equilibrio térmico, cada punto toma exactamente
la temperatura promedio de sus 4 vecinos inmediatos (Arriba, Abajo, Izq, Der)!

¿CÓMO ACELERA SOR (Successive Over-Relaxation)?
Gauss-Seidel actualiza el nodo paso a paso. SOR toma ese cambio y lo "empuja"
un poco más allá usando un factor ω (omega):
   T_nuevo = (1 - ω) * T_viejo + ω * T_GaussSeidel

- Si ω = 1: Es Gauss-Seidel estándar.
- Si 1 < ω < 2: Es Sobre-Relajación (SOR). ¡Reduce las iteraciones dramáticamente!
"""


# -----------------------------------------------------------------------------
# 2. Solver Laplace 2D con SOR
# -----------------------------------------------------------------------------
def resolver_laplace_2d(Nx, Ny, tol=1e-5, max_iter=10000, omega=1.5):
    # Inicialización de la placa
    T = np.zeros((Ny, Nx))

    # Condiciones de Frontera Dirichlet (°C)
    T[-1, :] = 100.0  # Borde Superior (Caliente)
    T[0, :] = 0.0     # Borde Inferior
    T[:, 0] = 75.0    # Borde Izquierdo
    T[:, -1] = 50.0   # Borde Derecho

    # Inicializar el interior con el promedio de las fronteras para acelerar
    T[1:-1, 1:-1] = np.mean([100.0, 0.0, 75.0, 50.0])

    iteraciones = 0
    error = 1.0

    while error > tol and iteraciones < max_iter:
        T_old = T.copy()

        for j in range(1, Ny - 1):
            for i in range(1, Nx - 1):
                # Valor Gauss-Seidel
                t_gs = 0.25 * (T[j, i + 1] + T[j, i - 1] + T[j + 1, i] + T[j - 1, i])
                # Aplicación de SOR
                T[j, i] = (1 - omega) * T[j, i] + omega * t_gs

        error = np.max(np.abs(T - T_old))
        iteraciones += 1

    return T, iteraciones


# -----------------------------------------------------------------------------
# 3. Ejecución y Mapa de Contorno
# -----------------------------------------------------------------------------
def ejecutar():
    Nx, Ny = 50, 50
    omega_opt = 1.8  # Factor SOR optimizado

    T_matriz, iters = resolver_laplace_2d(Nx, Ny, omega=omega_opt)

    print("=" * 65)
    print(" SOLUCIÓN ECUACIÓN DE LAPLACE 2D (ESTADO ESTACIONARIO)")
    print("=" * 65)
    print(f" Malla Espacial          : {Nx} x {Ny} nodos")
    print(f" Factor de Relajación (ω): {omega_opt}")
    print(f" Iteraciones a convergencia: {iters}")
    print("=" * 65)

    # Graficar Mapa Térmico
    plt.figure(figsize=(8, 6))
    x = np.linspace(0, 1, Nx)
    y = np.linspace(0, 1, Ny)
    X, Y = np.meshgrid(x, y)

    contour = plt.contourf(X, Y, T_matriz, 20, cmap='thermal' if 'thermal' in plt.colormaps() else 'inferno')
    plt.colorbar(contour, label='Temperatura [°C]')
    plt.title(f'Distribución de Temperatura 2D (Laplace) - {iters} iteraciones (SOR)', fontsize=12)
    plt.xlabel('Posición X [m]', fontsize=11)
    plt.ylabel('Posición Y [m]', fontsize=11)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    ejecutar()