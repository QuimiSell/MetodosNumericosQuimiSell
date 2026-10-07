"""
======================================================================
CLASE 20: DIFERENCIACION NUMERICA
SCRIPT 3: GRADIENTE NUMERICO, RUIDO Y LA RAZON DE SER DEL BACKPROPAGATION
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Por que la diferenciacion numerica amplifica el ruido?
   La integracion es un operador 'promediador' o suavizador: suma areas y cancela ruido.
   La derivacion hace exactamente lo contrario: calcula pendientes locales.
   Si tienes un dato con una fluctuacion pequena de ruido epsilon (por ejemplo 0.001)
   y aplicas diferencias finitas dividiendo entre h = 0.001:
      Ruido amplificado ≈ epsilon / h = 0.001 / 0.001 = 1.0
   ¡El ruido se vuelve tan grande como la funcion misma! En datos reales de sensores
   o entrenamiento ruidoso, la derivada numerica directa produce basura.

2. ¿Por que las Redes Neuronales (Deep Learning) NO usan diferencias finitas?
   Imagina un modelo como ChatGPT o ResNet con 100 millones de parametros (pesos w_i).
   - Para calcular el gradiente con diferencias finitas: Necesitas evaluar la red completa
     100 millones de veces (f(w + h) para cada w). ¡Tomaria dias por cada paso de gradiente!
   - Solucion: Autograd / Backpropagation (Regla de la Cadena analitica).
     Con solo UN paso hacia adelante y UN paso hacia atras por el grafo computacional,
     obtenemos el gradiente exacto de todos los millones de pesos simultaneamente,
     sin dividir entre h y sin sufrir por amplificacion de ruido numerico.
"""

import numpy as np
import matplotlib.pyplot as plt

# ====================================================================
# SUPERFICIE 2D DE EJEMPLO
# f(x, y) = x^2 + 2*y^2 + sin(3*x)
# ====================================================================

def superficie_f(x, y):
    return x**2 + 2.0 * (y**2) + np.sin(3.0 * x)

def gradiente_analitico(x, y):
    """
    df/dx = 2x + 3*cos(3x)
    df/dy = 4y
    """
    df_dx = 2.0 * x + 3.0 * np.cos(3.0 * x)
    df_dy = 4.0 * y
    return np.array([df_dx, df_dy])


# ====================================================================
# CALCULO DE GRADIENTE NUMERICO
# ====================================================================

def gradiente_numerico(f_func, x, y, h=1e-5):
    """Calcula el vector gradiente usando diferencias centradas"""
    df_dx = (f_func(x + h, y) - f_func(x - h, y)) / (2.0 * h)
    df_dy = (f_func(x, y + h) - f_func(x, y - h)) / (2.0 * h)
    return np.array([df_dx, df_dy])


# ====================================================================
# SIMULACION DE RUIDO EXPERIMENTAL
# ====================================================================

def demo_gradiente_y_ruido():
    np.random.seed(42)  # Para reproducibilidad exacta en clase

    punto_x = 1.0
    punto_y = 1.0
    h_paso = 1e-4

    grad_real = gradiente_analitico(punto_x, punto_y)
    grad_num_limpio = gradiente_numerico(superficie_f, punto_x, punto_y, h=h_paso)

    # Introducimos un ruido minusculo de sensor (magnitud 1e-5)
    amplitud_ruido = 1e-4

    def superficie_con_ruido(x, y):
        ruido = np.random.normal(0, amplitud_ruido)
        return superficie_f(x, y) + ruido

    grad_num_ruidoso = gradiente_numerico(superficie_con_ruido, punto_x, punto_y, h=h_paso)

    print("=" * 72)
    print(" IMPACTO DEL RUIDO EN EL VECTOR GRADIENTE [df/dx, df/dy]")
    print(f" Evaluando en el punto: (x = {punto_x}, y = {punto_y}) con paso h = {h_paso}")
    print("=" * 72)
    print(f" Gradiente Exacto (Analitico):  [{grad_real[0]:10.5f}, {grad_real[1]:10.5f}]")
    print(f" Gradiente Numerico (Limpio):   [{grad_num_limpio[0]:10.5f}, {grad_num_limpio[1]:10.5f}]")
    print(f" Gradiente Numerico (RUIDOSO):  [{grad_num_ruidoso[0]:10.5f}, {grad_num_ruidoso[1]:10.5f}]")
    print("-" * 72)
    error_limpio = np.linalg.norm(grad_num_limpio - grad_real)
    error_ruidoso = np.linalg.norm(grad_num_ruidoso - grad_real)
    print(f" Error norma en senal limpia:   {error_limpio:.6e}")
    print(f" Error norma en senal ruidosa:  {error_ruidoso:.6f}  <-- ¡DESTRUIDO POR EL RUIDO!")
    print("=" * 72)

    # Visualizacion 1D de la amplificacion de ruido al derivar
    x_grid = np.linspace(0, 3, 200)
    y_fijo = 1.0
    senial_pura = superficie_f(x_grid, y_fijo)
    senial_ruido = senial_pura + np.random.normal(0, 0.05, size=x_grid.shape)

    # Derivada numerica a lo largo de x
    dx = x_grid[1] - x_grid[0]
    derivada_real = 2.0 * x_grid + 3.0 * np.cos(3.0 * x_grid)
    derivada_ruidosa = np.gradient(senial_ruido, dx)

    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    # Grafico 1: Senal con ruido casi imperceptible
    axs[0].plot(x_grid, senial_pura, label="Senal original limpia f(x, y=1)", color="blue", linewidth=2)
    axs[0].scatter(x_grid, senial_ruido, label="Datos observados con ruido (5%)", color="black", s=10, alpha=0.5)
    axs[0].set_title("Datos de Entrada: Ruido aparentemente moderado", fontsize=12)
    axs[0].set_ylabel("f(x, y=1)", fontsize=11)
    axs[0].grid(True, linestyle="--", alpha=0.5)
    axs[0].legend()

    # Grafico 2: Derivada totalmente corrompida
    axs[1].plot(x_grid, derivada_real, label="Derivada exacta df/dx", color="green", linewidth=2.5)
    axs[1].plot(x_grid, derivada_ruidosa, label="Derivada numerica sobre datos ruidosos", color="crimson", alpha=0.7)
    axs[1].set_title("Efecto de la Diferenciacion: El ruido se amplifica y ahoga el gradiente real", fontsize=12)
    axs[1].set_xlabel("x", fontsize=11)
    axs[1].set_ylabel("df/dx", fontsize=11)
    axs[1].grid(True, linestyle="--", alpha=0.5)
    axs[1].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    demo_gradiente_y_ruido()