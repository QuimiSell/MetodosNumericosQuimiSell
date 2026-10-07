import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton

# 1. DEFINICION MATEMATICA
def f(x):
    return x**2 - 2

def df(x):
    return 2 * x

# 2. RESOLUCION CON LIBRERIA PROFESIONAL (SCIPY)
def resolver_con_scipy():
    x0 = 0.5
    # SciPy ejecuta el algoritmo optimizado en C/Fortran
    raiz = newton(func=f, x0=x0, fprime=df, tol=1e-6)
    print(f"Raiz calculada por SciPy: x = {raiz:.8f}")
    return raiz

# 3. VISUALIZACION DE LA SOLUCION
if __name__ == "__main__":
    raiz = resolver_con_scipy()

    x_vals = np.linspace(-0.5, 2.5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x^2 - 2", color="darkcyan", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    
    # Marcador en el punto exacto de la raiz
    plt.plot(raiz, 0, "go", markersize=9, label=f"Punto Exacto Raiz (x={raiz:.6f}, y=0)")

    plt.title("Programa 3.5: Newton-Raphson con SciPy.Optimize")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.show()