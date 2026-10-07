import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

"""
GUION DE VOZ / PRODUCTOS TENSORIALES:
Cuando extendemos la cuadratura a 2D y 3D, aplicamos el concepto de producto tensorial.
Si en 1D tenemos n nodos y n pesos, en 2D tomamos una malla de n x n nodos (x_i, y_j) 
y el peso combinado es simplemente w_ij = w_i * w_j.
Es el análogo matemático de calcular el volumen sumando prismas ponderados.

Problema físico:
Distribución de temperatura en una placa rectangular [0, 2] x [0, 1]:
T(x, y) = 100 * sin(pi * x / 2) * exp(-y)
Calcularemos la energía térmica total (integral de T sobre el área).
"""

def gauss_legendre_2d(f, ax, bx, ay, by, n_puntos=3):
    if n_puntos == 2:
        t = np.array([-1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)])
        w = np.array([1.0, 1.0])
    elif n_puntos == 3:
        t = np.array([-np.sqrt(3.0 / 5.0), 0.0, np.sqrt(3.0 / 5.0)])
        w = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])
    else:
        raise ValueError("Implementado para 2 o 3 puntos.")

    cx1 = (bx - ax) / 2.0
    cx2 = (ax + bx) / 2.0
    cy1 = (by - ay) / 2.0
    cy2 = (ay + by) / 2.0

    x = cx1 * t + cx2
    y = cy1 * t + cy2

    integral = 0.0
    for i in range(n_puntos):
        for j in range(n_puntos):
            integral += w[i] * w[j] * f(x[i], y[j])

    return cx1 * cy1 * integral, x, y

def trapecio_iterado_2d(f, ax, bx, ay, by, nx=100, ny=100):
    x = np.linspace(ax, bx, nx + 1)
    y = np.linspace(ay, by, ny + 1)
    hx = (bx - ax) / nx
    hy = (by - ay) / ny

    wx = np.full(nx + 1, 2.0)
    wx[0] = 1.0
    wx[-1] = 1.0

    wy = np.full(ny + 1, 2.0)
    wy[0] = 1.0
    wy[-1] = 1.0

    W = np.outer(wx, wy)
    X, Y = np.meshgrid(x, y, indexing='ij')
    F = f(X, Y)

    integral = (hx * hy / 4.0) * np.sum(W * F)
    return integral

def graficar_superficie_y_malla(f, ax_lim, bx_lim, ay_lim, by_lim, gx, gy):
    x_grid = np.linspace(ax_lim, bx_lim, 60)
    y_grid = np.linspace(ay_lim, by_lim, 60)
    X, Y = np.meshgrid(x_grid, y_grid)
    Z = f(X, Y)

    # Nodos de Gauss 2D
    GX, GY = np.meshgrid(gx, gy)
    GZ = f(GX, GY)

    fig = plt.figure(figsize=(12, 5))

    # Panel 1: Superficie 3D
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    surf = ax1.plot_surface(X, Y, Z, cmap='inferno', alpha=0.8, edgecolor='none')
    ax1.scatter(GX, GY, GZ, color='cyan', s=60, edgecolors='black', label='Nodos Gauss (3x3)')
    ax1.set_title("Superficie Térmica T(x, y)")
    ax1.set_xlabel("X (m)")
    ax1.set_ylabel("Y (m)")
    ax1.set_zlabel("T (°C)")
    ax1.legend()

    # Panel 2: Mapa 2D con malla tensorial
    ax2 = fig.add_subplot(1, 2, 2)
    cp = ax2.contourf(X, Y, Z, levels=20, cmap='inferno')
    cbar = fig.colorbar(cp, ax=ax2)
    cbar.set_label('Temperatura (°C)')
    ax2.scatter(GX, GY, color='cyan', edgecolors='black', s=90, zorder=5, label='Nodos de Gauss (3x3)')
    
    # Líneas de la grilla tensorial
    for x_val in gx:
        ax2.axvline(x_val, color='white', linestyle=':', alpha=0.6)
    for y_val in gy:
        ax2.axhline(y_val, color='white', linestyle=':', alpha=0.6)

    ax2.set_title("Placa 2D y Producto Tensorial de Nodos")
    ax2.set_xlabel("X (m)")
    ax2.set_ylabel("Y (m)")
    ax2.legend(loc='upper right')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ax, bx = 0.0, 2.0
    ay, by = 0.0, 1.0
    
    def campo_temperatura(x, y):
        return 100.0 * np.sin(np.pi * x / 2.0) * np.exp(-y)

    # 1. Referencia con SciPy dblquad (recibe (y, x))
    scipy_res, _ = dblquad(lambda y, x: campo_temperatura(x, y), ax, bx, ay, by)

    # 2. Cuadratura Gauss-Legendre (Producto tensorial 3x3)
    gl_res, gx, gy = gauss_legendre_2d(campo_temperatura, ax, bx, ay, by, n_puntos=3)

    # 3. Trapecio Iterado (Malla 101x101)
    trap_res = trapecio_iterado_2d(campo_temperatura, ax, bx, ay, by, nx=100, ny=100)

    print("=" * 72)
    print("CLASE 22: INTEGRALES MÚLTIPLES - TEMPERATURA EN PLACA 2D")
    print("=" * 72)
    print(f"Dominio: x en [{ax}, {bx}], y en [{ay}, {by}]")
    print(f"Función: T(x, y) = 100 * sin(pi*x/2) * e^(-y)\n")
    
    print(f"{'Método':<32} | {'Aproximación':<16} | {'Diferencia vs SciPy':<18}")
    print("-" * 72)
    print(f"{'SciPy (dblquad)':<32} | {scipy_res:<16.8f} | {'Referencia':<18}")
    print(f"{'Gauss-Legendre (3x3 nodos)':<32} | {gl_res:<16.8f} | {abs(gl_res - scipy_res):<18.4e}")
    print(f"{'Trapecio Iterado (101x101 nodos)':<32} | {trap_res:<16.8f} | {abs(trap_res - scipy_res):<18.4e}")
    print("=" * 72)

    graficar_superficie_y_malla(campo_temperatura, ax, bx, ay, by, gx, gy)