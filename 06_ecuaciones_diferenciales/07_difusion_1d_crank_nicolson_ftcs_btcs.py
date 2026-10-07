"""
===============================================================================
CLASE 25 - PARTE 2: Difusión 1D Transitoria (FTCS vs. BTCS vs. Crank-Nicolson)
===============================================================================
Propósito:
  Comparar esquemas numéricos para ∂T/∂t = α * ∂²T/∂x²:
  1. Explícito (FTCS - Forward Time Centered Space)
  2. Implícito (BTCS - Backward Time Centered Space)
  3. Crank-Nicolson (Promedio Implícito-Explícito O(dt² + dx²))
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# 1. EXPLICACIÓN FEYNMAN: ESTABILIDAD VON NEUMANN Y CRANK-NICOLSON
# -----------------------------------------------------------------------------
"""
¿QUÉ ES EL CRITERIO DE ESTABILIDAD DE VON NEUMANN (r <= 0.5)?

Definimos el número de Fourier mesh: r = α * dt / (dx²)

- ESQUEMA EXPLÍCITO (FTCS):
  Usa solo el pasado para calcular el futuro. Si r > 0.5, el método viola la 2da
  ley de la termodinámica localmente, generando oscilaciones numéricas salvajes
  que crecen exponencialmente hasta destruir la solución.

- LA ELEGANCIA DE CRANK-NICOLSON:
  En lugar de evaluar la derivada espacial solo en el tiempo presente n (FTCS)
  o solo en el futuro n+1 (BTCS), Crank-Nicolson toma EL PROMEDIO EXACTO de ambos.
  
  Esto convierte el esquema en incondicionalmente estable para cualquier dt,
  alcanzando una precisión de segundo orden tanto en espacio como en tiempo: O(dt² + dx²).
  Para resolverlo, ensamblamos un sistema tridiagonal A * T^{n+1} = B * T^n en cada paso.
"""


# -----------------------------------------------------------------------------
# 2. Implementación de los Métodos
# -----------------------------------------------------------------------------
def resolver_difusion(L, T_final, Nx, dt, alpha):
    dx = L / (Nx - 1)
    r = alpha * dt / (dx**2)
    x = np.linspace(0, L, Nx)
    Nt = int(T_final / dt)

    # Condición Inicial (Perfil parabólico de temperatura)
    T0 = 100.0 * np.sin(np.pi * x / L)

    # 1. Método Explícito FTCS
    T_ftcs = T0.copy()
    for _ in range(Nt):
        T_next = T_ftcs.copy()
        for i in range(1, Nx - 1):
            T_next[i] = T_ftcs[i] + r * (T_ftcs[i + 1] - 2 * T_ftcs[i] + T_ftcs[i - 1])
        T_ftcs = T_next

    # 2. Método Crank-Nicolson (Tridiagonal)
    N_int = Nx - 2
    A = np.zeros((N_int, N_int))
    B = np.zeros((N_int, N_int))

    np.fill_diagonal(A, 1.0 + r)
    np.fill_diagonal(A[:-1, 1:], -r / 2.0)
    np.fill_diagonal(A[1:, :-1], -r / 2.0)

    np.fill_diagonal(B, 1.0 - r)
    np.fill_diagonal(B[:-1, 1:], r / 2.0)
    np.fill_diagonal(B[1:, :-1], r / 2.0)

    T_cn = T0.copy()
    for _ in range(Nt):
        b_vec = B @ T_cn[1:-1]
        T_cn[1:-1] = np.linalg.solve(A, b_vec)

    return x, T0, T_ftcs, T_cn, r


# -----------------------------------------------------------------------------
# 3. Simulación y Comparación
# -----------------------------------------------------------------------------
def simular():
    L = 1.0
    T_final = 0.1
    Nx = 21
    alpha = 0.01

    # Caso 1: dt estable (r <= 0.5)
    dt_estable = 0.001
    x, T0, T_ftcs, T_cn, r_est = resolver_difusion(L, T_final, Nx, dt_estable, alpha)

    print("=" * 65)
    print(" ANÁLISIS DE DIFUSIÓN 1D TRANSITORIA")
    print("=" * 65)
    print(f" Parámetro de estabilidad r (dt = {dt_estable}): {r_est:.4f} (Estable)")
    print("=" * 65)

    # Gráfica del perfil
    plt.figure(figsize=(9, 5))
    plt.plot(x, T0, 'k--', label='Condición Inicial $T(x, 0)$')
    plt.plot(x, T_ftcs, 'b-o', label=f'Explícito FTCS ($r={r_est:.2f}$)')
    plt.plot(x, T_cn, 'r-s', label=f'Crank-Nicolson ($r={r_est:.2f}$)')

    plt.title('Evolución Temporal del Perfil de Temperatura $T(x, t)$', fontsize=12)
    plt.xlabel('Posición $x$ [m]', fontsize=11)
    plt.ylabel('Temperatura $T$ [°C]', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    simular()