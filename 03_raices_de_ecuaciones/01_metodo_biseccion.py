# ====================================================
# CLASE 12: MÉTODO DE BISECCIÓN (MÓDULO 3)
# Autor / Canal: QuimiSell
# Descripción: Código independiente y gráfico para cálculo de raíces
# ====================================================

import numpy as np
import matplotlib.pyplot as plt

# 1. Definición de la función de ejemplo
def f(x):
    return x**3 - x - 2

def biseccion(f, a, b, tol=1e-6, max_iter=100):
    # Verificación del Teorema de Bolzano
    if f(a) * f(b) >= 0:
        raise ValueError("El intervalo inicial no cumple con el cambio de signo (f(a) * f(b) >= 0).")
    
    print(f"--- INICIO MÉTODO DE BISECCIÓN ---")
    print(f"Intervalo inicial: [{a}, {b}]")
    
    historial_c = []
    
    for i in range(max_iter):
        c = (a + b) / 2.0
        fc = f(c)
        historial_c.append(c)
        
        print(f"Iter {i+1:2d}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {fc:.6f}")
        
        # Criterio de parada por tolerancia o tamaño del intervalo
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            print(f"\n¡Éxito! Raíz encontrada en {i+1} iteraciones.")
            print(f"Raíz aproximada (x): {c:.8f}\n")
            return c, historial_c
        
        # Selección de la subregión que contiene el cambio de signo
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    raise RuntimeError("Se alcanzó el número máximo de iteraciones.")

# Ejecución principal
if __name__ == "__main__":
    a_ini, b_ini = 1.0, 2.0
    raiz, historial = biseccion(f, a_ini, b_ini)
    
    # ----------------------------------------------------
    # REPRESENTACIÓN GRÁFICA PARA EL VIDEO
    # ----------------------------------------------------
    x_vals = np.linspace(0.5, 2.5, 400)
    y_vals = f(x_vals)
    
    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x³ - x - 2", color="blue", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    
    # Graficar la convergencia de los puntos medios calculados
    plt.scatter(historial, [f(val) for val in historial], color="red", zorder=5, 
                label=f"Aproximaciones (Bisección): {len(historial)} iteraciones")
    
    plt.title("Método Cerrado: Bisección (Clase 12)", fontsize=14, fontweight='bold')
    plt.xlabel("Eje X", fontsize=12)
    plt.ylabel("Eje Y", fontsize=12)
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend()
    plt.show()