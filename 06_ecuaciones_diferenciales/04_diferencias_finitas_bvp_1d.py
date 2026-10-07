"""
===============================================================================
CLASE 24 - PARTE 2: Método de Diferencias Finitas para BVPs 1D
===============================================================================
Propósito:
  Resolver la transferencia de calor estacionaria en una barra metálica 1D
  con generación interna de calor mediante aproximaciones centradas.

Modelo Físico (BVP):
  d²T/dx² + S = 0   en x ∈ [0, L]
  Condiciones de Frontera (Dirichlet):
  T(0) = T_izquierda (e.g., 100 °C)
  T(L) = T_derecha   (e.g., 400 °C)
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve_banded


# -----------------------------------------------------------------------------
# 1. EXPLICACIÓN FEYNMAN: DE EDO CONTINUA A MATRIZ TRIDIAGONAL (A * y = b)
# -----------------------------------------------------------------------------
"""
¿CÓMO CONVERTIMOS UNA ECUACIÓN DIFERENCIAL EN UNA MATRIZ?

En un Problema de Valor Inicial (PVI), caminamos hacia adelante en el tiempo.
En un Problema de Valores en la Frontera (BVP), conocemos ambos extremos del dominio
y necesitamos descubrir la forma de TODO el perfil interior de un solo golpe.

1. DISCRETIZACIÓN ESPACIAL:
   Dividimos la barra de longitud L en N nodos separados por un paso dx.

2. APROXIMACIÓN DE SEGUNDA DERIVADA (Diferencias Finitas Centradas):
   La curvatura en un nodo i depende de sus dos vecinos (izquierdo i-1 y derecho i+1):
   
        d²T/dx² ≈ (T_{i-1} - 2*T_i + T_{i+1}) / (dx²)

3. ENSAMBLAJE DEL SISTEMA LINEAL:
   Sustituyendo en la EDO (d²T/dx² = -S):
   
        T_{i-1} - 2*T_i + T_{i+1} = -S * dx²
   
   ¡Esto es una ecuación lineal para cada nodo interior! Al juntar todos los nodos,
   obtenemos un sistema A * T = b donde A es TRIDIAGONAL:
   - Diagonal Principal:  -2
   - Diagonales Superior e Inferior: +1

4. ACOPLAMIENTO DE FRONTERAS:
   Los nodos extremos (0 y N) ya se conocen (T_0 = T_izq, T_N = T_der). 
   Sus valores pasan al vector b del lado derecho, "empujando" el calor desde los bordes.
"""


# -----------------------------------------------------------------------------
# 2. Solver BVP por Diferencias Finitas
# -----------------------------------------------------------------------------
def resolver_bvp_calor(L, T_izq, T_der, S, N):
    """
    Resuelve d²T/dx² = -S con T(0) = T_izq y T(L) = T_der.
    N: Número de subdivisiones de la barra.
    """
    dx = L / N
    x = np.linspace(0, L, N + 1)

    # Matriz para los nodos INTERIORES: 1 a N-1 (Dimensión: (N-1) x (N-1))
    num_interiores = N - 1
    A = np.zeros((num_interiores, num_interiores))
    b = np.full(num_interiores, -S * (dx**2))

    # Llenado de la matriz Tridiagonal
    np.fill_diagonal(A, -2.0)
    np.fill_diagonal(A[:-1, 1:], 1.0)
    np.fill_diagonal(A[1:, :-1], 1.0)

    # Aplicación de Condiciones de Frontera (Modificación del vector b)
    b[0] -= T_izq      # Acoplamiento del borde izquierdo
    b[-1] -= T_der     # Acoplamiento del borde derecho

    # Resolver el sistema lineal A * T_int = b
    T_interiores = np.linalg.solve(A, b)

    # Reconstruir el vector completo T incluyendo las fronteras conocidas
    T = np.zeros(N + 1)
    T[0] = T_izq
    T[-1] = T_der
    T[1:-1] = T_interiores

    return x, T, A, b, dx


# -----------------------------------------------------------------------------
# 3. Ejecución y Muestra en Consola
# -----------------------------------------------------------------------------
def ejecutar_simulacion():
    # Parámetros físicos
    L = 1.0          # Longitud de la barra [m]
    T_izq = 100.0    # Temperatura borde izquierdo [°C]
    T_der = 400.0    # Temperatura borde derecho [°C]
    S = 200.0        # Término fuente de generación de calor [°C/m²]

    # Número pequeño de nodos para visualización clara de la matriz A en consola
    N_consola = 5
    x_c, T_c, A_c, b_c, dx_c = resolver_bvp_calor(L, T_izq, T_der, S, N_consola)

    print("=" * 65)
    print(" SISTEMA MATRICIAL ENSAMBLADO (N = 5, Nodos Interiores = 4)")
    print("=" * 65)
    print(f"Paso espacial dx = {dx_c:.4f} m\n")
    print("Matriz A (Coeficientes Tridiagonales):")
    print(A_c)
    print("\nVector del lado derecho b (Fuente + Condiciones de Frontera):")
    print(b_c)
    print("\nTemperaturas calculadas T(x) [°C]:")
    for xi, Ti in zip(x_c, T_c):
        print(f"  x = {xi:.2f} m  -->  T = {Ti:.2f} °C")
    print("=" * 65)

    # Solución fina para gráfica suave
    N_fino = 100
    x_fino, T_fino, _, _, _ = resolver_bvp_calor(L, T_izq, T_der, S, N_fino)

    # Gráfica del perfil térmico
    plt.figure(figsize=(9, 5))
    plt.plot(x_fino, T_fino, 'r-', linewidth=2.5, label='Perfil T(x) - Malla fina ($N=100$)')
    plt.plot(x_c, T_c, 'bo--', markersize=7, label='Nodos discretos ($N=5$)')

    # Destacar fronteras
    plt.plot(0, T_izq, 'go', markersize=10, label=f'Frontera Izq: {T_izq}°C')
    plt.plot(L, T_der, 'mo', markersize=10, label=f'Frontera Der: {T_der}°C')

    plt.title('Distribución de Temperatura Estacionaria en una Barra 1D (BVP)', fontsize=13)
    plt.xlabel('Posición en la barra $x$ [m]', fontsize=11)
    plt.ylabel('Temperatura $T$ [°C]', fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10, loc='upper left')
    plt.tight_layout()

    print("\nGenerando gráfica del perfil de temperatura...")
    plt.show()


if __name__ == "__main__":
    ejecutar_simulacion()