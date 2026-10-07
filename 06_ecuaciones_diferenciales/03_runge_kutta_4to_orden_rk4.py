"""
===============================================================================
CLASE 24 - PARTE 1: Runge-Kutta de 4° Orden (RK4) para Sistemas Vectoriales
===============================================================================
Propósito:
  Implementar RK4 vectorial para resolver el modelo ecológico Depredador-Presa
  (Lotka-Volterra) y demostrar por qué el orden O(h⁴) es el estándar industrial.

Modelo Matemático (Lotka-Volterra):
  dx/dt = alpha * x - beta * x * y   (Presas: Conejos)
  dy/dt = delta * x * y - gamma * y  (Depredadores: Lobos)
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# 1. Definición del Sistema Vectorial de EDOs
# -----------------------------------------------------------------------------
def sistema_lotka_volterra(t, u, alpha=1.1, beta=0.4, delta=0.1, gamma=0.4):
    """
    Sistema vectorial: du/dt = F(t, u)
    u[0] = x(t) : Población de presas
    u[1] = y(t) : Población de depredadores
    """
    x, y = u[0], u[1]
    dx_dt = alpha * x - beta * x * y
    dy_dt = delta * x * y - gamma * y
    return np.array([dx_dt, dy_dt])


# -----------------------------------------------------------------------------
# 2. Algoritmo Vectorial RK4
# -----------------------------------------------------------------------------
def rk4_sistema(f, t0, u0, tf, h):
    """
    EXPLICACIÓN FEYNMAN (RK4 Vectorial):
    ¿Por qué RK4 es el 'Santo Grial' de la simulación?

    Imagínate navegando en un mapa de corrientes de viento.
    - K1: Mides la velocidad del viento donde estás AHORA MISMO.
    - K2: Das medio paso (h/2) guiado por K1 y vuelves a medir el viento.
    - K3: Regresas al origen, pero usas K2 para volver a dar el medio paso.
          ¡Esta es la corrección del punto medio!
    - K4: Das un paso completo (h) usando la velocidad refinada de K3 para
          probar cómo viene el viento al final del tramo.

    Al final, haces un promediado ponderado (Regla de Simpson):
    u_{i+1} = u_i + (h/6) * (K1 + 2*K2 + 2*K3 + K4)

    ¿POR QUÉ EL ORDEN O(h^4) DOMINA LA INDUSTRIA?
    Porque los términos de error de la Serie de Taylor se cancelan hasta la
    3era derivada. Si reduces el paso h a la mitad (h/2), el error NO cae a la
    mitad (como en Euler) ni a la cuarta parte (como en Euler Modificado)...
    ¡El error se reduce 16 veces (2^4)!
    """
    n_pasos = int(np.round((tf - t0) / h))
    t = np.linspace(t0, tf, n_pasos + 1)

    # Matriz para almacenar las variables de estado (Filas: tiempo, Col: componentes)
    u = np.zeros((n_pasos + 1, len(u0)))
    u[0] = u0

    for i in range(n_pasos):
        t_i = t[i]
        u_i = u[i]

        # Muestreo de las 4 pendientes vectoriales
        k1 = f(t_i, u_i)
        k2 = f(t_i + 0.5 * h, u_i + 0.5 * h * k1)
        k3 = f(t_i + 0.5 * h, u_i + 0.5 * h * k2)
        k4 = f(t_i + h, u_i + h * k3)

        # Promedio ponderado Simpson
        u[i + 1] = u_i + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)

    return t, u


# -----------------------------------------------------------------------------
# 3. Ejecución y Visualización
# -----------------------------------------------------------------------------
def simular_y_graficar():
    # Parámetros de simulación
    t0, tf = 0.0, 50.0
    h = 0.05
    u0 = np.array([10.0, 5.0])  # 10 presas, 5 depredadores iniciales

    t, u = rk4_sistema(sistema_lotka_volterra, t0, u0, tf, h)

    print("=" * 65)
    print(" SIMULACIÓN RK4: MODELO DEP REDADOR-PRESA (LOTKA-VOLTERRA)")
    print("=" * 65)
    print(f" Condición Inicial : Presas = {u0[0]}, Depredadores = {u0[1]}")
    print(f" Tiempo total      : {tf} unidades | Paso (h): {h}")
    print(f" Estado Final (t={tf}): Presas = {u[-1, 0]:.3f}, Depredadores = {u[-1, 1]:.3f}")
    print("=" * 65)

    # Subplots: Serie de Tiempo + Plano de Fase
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # 1. Perfil Temporal
    ax1.plot(t, u[:, 0], 'b-', linewidth=2, label='Presas $x(t)$ (Conejos)')
    ax1.plot(t, u[:, 1], 'r--', linewidth=2, label='Depredadores $y(t)$ (Lobos)')
    ax1.set_title('Dinámica Temporal de Poblaciones', fontsize=12)
    ax1.set_xlabel('Tiempo', fontsize=11)
    ax1.set_ylabel('Población', fontsize=11)
    ax1.grid(True, linestyle='--', alpha=0.6)
    ax1.legend(loc='upper right')

    # 2. Plano de Fase (Trayectoria Orbital)
    ax2.plot(u[:, 0], u[:, 1], 'g-', linewidth=2)
    ax2.plot(u0[0], u0[1], 'ko', markersize=8, label='Inicio $(x_0, y_0)$')
    ax2.set_title('Plano de Fase: Ciclo de Vida Presa-Depredador', fontsize=12)
    ax2.set_xlabel('Presas $x(t)$', fontsize=11)
    ax2.set_ylabel('Depredadores $y(t)$', fontsize=11)
    ax2.grid(True, linestyle='--', alpha=0.6)
    ax2.legend()

    plt.tight_layout()
    print("\nGenerando gráficas (Serie Temporal y Plano de Fase)...")
    plt.show()


if __name__ == "__main__":
    simular_y_graficar()