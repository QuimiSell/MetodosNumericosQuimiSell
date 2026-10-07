import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

# 1. FUNCION, PRIMERA Y SEGUNDA DERIVADA
def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3 * x**2 - 2

def d2f(x):
    return 6 * x

# 2. RESOLUCION MEDIANTE CONVERGENCIA CUBICA (HALLEY)
def resolver_halley():
    x0 = 3.0
    # Al pasar 'fprime2' (segunda derivada), SciPy ejecuta el algoritmo de Halley
    raiz = newton(func=f, x0=x0, fprime=df, fprime2=d2f, tol=1e-6)
    print(f"Raiz exacta por Metodo de Halley: x = {raiz:.8f}")
    return raiz

# 3. VISUALIZACION DEL PUNTO
if __name__ == "__main__":
    raiz = resolver_halley()

    x_vals = np.linspace(0, 3.5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x^3 - 2x - 5", color="darkorange", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    
    # Punto exacto donde la curva cruza el cero
    plt.plot(raiz, 0, "mo", markersize=9, label=f"Raiz Cúbica Exacta: x = {raiz:.6f}")

    plt.title("Programa 3.7: Metodo de Halley (Convergencia Cubica)")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.show()