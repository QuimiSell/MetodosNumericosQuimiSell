"""
===============================================================================
CLASE 23: Balance de Materia en Reactores Agitados (CSTR) en Cascada
===============================================================================
Propósito:
  Modelar un sistema real de ingeniería química (2 tanques CSTR en serie)
  utilizando el Método de Euler Modificado.

Modelo Físico:
  Tanque 1: dC1/dt = (F/V1) * C_in - (F/V1) * C1 - k * C1
  Tanque 2: dC2/dt = (F/V2) * C1   - (F/V2) * C2 - k * C2
===============================================================================
"""

import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# 1. Parámetros del Sistema de Reactores
# -----------------------------------------------------------------------------
F = 10.0      # Flujo volumétrico [L/min]
V1 = 100.0    # Volumen Tanque 1 [L]
V2 = 100.0    # Volumen Tanque 2 [L]
C_in = 2.0    # Concentración de entrada al Tanque 1 [mol/L]
k = 0.05      # Constante cinética de reacción de 1er orden [1/min]


def sistema_reactores(t, C):
    """
    Sistema de Ecuaciones Diferenciales Ordinarias (EDOs).
    C[0]: Concentración Tanque 1 (C1)
    C[1]: Concentración Tanque 2 (C2)
    """
    c1, c2 = C[0], C[1]
    dc1_dt = (F / V1) * C_in - (F / V1) * c1 - k * c1
    dc2_dt = (F / V2) * c1 - (F / V2) * c2 - k * c2
    return np.array([dc1_dt, dc2_dt])


# -----------------------------------------------------------------------------
# 2. Integrador Euler Modificado para Sistemas de EDOs
# -----------------------------------------------------------------------------
def euler_modificado_sistema(sistema, t0, C0, tf, h):
    """
    Aplica el algoritmo Predictor-Corrector a vectores de estado C(t).
    """
    n_pasos = int(np.round((tf - t0) / h))
    t = np.linspace(t0, tf, n_pasos + 1)
    C = np.zeros((n_pasos + 1, len(C0)))
    C[0] = C0

    for i in range(n_pasos):
        # Predictor
        k1 = sistema(t[i], C[i])
        C_pred = C[i] + h * k1

        # Corrector
        k2 = sistema(t[i + 1], C_pred)

        # Promedio vectorial
        C[i + 1] = C[i] + (h / 2.0) * (k1 + k2)

    return t, C


# -----------------------------------------------------------------------------
# 3. EXPLICACIÓN FEYNMAN: RIGIDEZ (STIFFNESS) Y SIMULADORES INDUSTRIALES
# -----------------------------------------------------------------------------
"""
¿QUÉ ES LA RIGIDEZ (STIFFNESS) EN SIMULACIÓN DE PROCESOS?

Imagina un sistema con dos procesos ocurriendo al mismo tiempo:
1. Una mezcla hidráulica lenta que tarda 50 minutos en estabilizarse.
2. Una reacción química ultrarrápida que ocurre en 0.001 segundos.

Si intentas resolver esto con Euler Modificado o Runge-Kutta explícito, el paso de 
tiempo 'h' queda "secuestrado" por la velocidad de la reacción rápida. Si usas un 
paso grande (ej. h = 0.5 min) para simular los 50 minutos del tanque, la parte rápida 
generará oscilaciones salvajes que harán explotar el cálculo numérico a infinito.

¿Por qué los simuladores industriales (ASPEN, HYSYS) usan métodos implícitos o RK45?
- Métodos Explícitos (Euler, RK4): Calculan el futuro usando solo datos del presente. 
  Son frágiles ante la rigidez.
- Métodos Implicitos (Backward Euler, BDF) o Adaptativos (RK45):
  * Los métodos adaptativos como RK45 reducen 'h' automáticamente en las zonas 
    bruscas y lo aumentan en el régimen estacionario.
  * Los métodos implícitos evalúan la pendiente en el tiempo futuro *y_{i+1}*, 
    garantizando estabilidad incondicional incluso con pasos grandes.
"""


# -----------------------------------------------------------------------------
# 4. Simulación y Visualización
# -----------------------------------------------------------------------------
def simular_y_graficar():
    # Parámetros temporales
    t0, tf = 0.0, 60.0  # Tiempo en minutos
    h = 0.5             # Paso de integración
    C0 = [0.0, 0.0]     # Concentraciones iniciales (tanques limpios)

    t, C = euler_modificado_sistema(sistema_reactores, t0, C0, tf, h)

    # Cálculo analítico del estado estacionario (dC/dt = 0)
    c1_ss = (F * C_in) / (F + k * V1)
    c2_ss = (F * c1_ss) / (F + k * V2)

    print("=" * 60)
    print(" RESULTADOS DEL ESTADO ESTACIONARIO (t -> ∞)")
    print("=" * 60)
    print(f"Tanque 1 - Numérico: {C[-1, 0]:.4f} mol/L | Teórico: {c1_ss:.4f} mol/L")
    print(f"Tanque 2 - Numérico: {C[-1, 1]:.4f} mol/L | Teórico: {c2_ss:.4f} mol/L")
    print("=" * 60)

    # Configuración de gráfica estilo profesional/académico
    plt.figure(figsize=(10, 6))
    plt.plot(t, C[:, 0], 'b-', linewidth=2, label='Tanque 1 ($C_1$)')
    plt.plot(t, C[:, 1], 'r--', linewidth=2, label='Tanque 2 ($C_2$)')

    # Líneas de estado estacionario
    plt.axhline(y=c1_ss, color='b', linestyle=':', alpha=0.6, label='Estacionario $C_1$')
    plt.axhline(y=c2_ss, color='r', linestyle=':', alpha=0.6, label='Estacionario $C_2$')

    plt.title('Dinámica de Concentración en Reactores CSTR en Serie', fontsize=14, pad=12)
    plt.xlabel('Tiempo [minutos]', fontsize=12)
    plt.ylabel('Concentración [mol/L]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=11, loc='lower right')
    plt.tight_layout()

    print("\nGenerando gráfica del perfil de concentración...")
    plt.show()


if __name__ == "__main__":
    simular_y_graficar()