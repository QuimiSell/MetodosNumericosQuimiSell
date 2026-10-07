import cmath
import numpy as np
import matplotlib.pyplot as plt

def metodo_muller_con_tabla(f, x0, x1, x2, tol=1e-5, max_iter=20):
    # Encabezado de la tabla para el cuaderno
    print("=" * 95)
    print(f"{'Iter':<5} | {'x0':<10} | {'x1':<10} | {'x2':<10} | {'a':<10} | {'b':<10} | {'c':<10} | {'x3 (Nueva)':<12} | {'Error':<10}")
    print("=" * 95)

    historial_x3 = []

    for i in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f1 - f0) / h0
        d1 = (f2 - f1) / h1
        
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = f2
        
        rad = cmath.sqrt(b**2 - 4 * a * c)
        den1 = b + rad
        den2 = b - rad
        den = den1 if abs(den1) > abs(den2) else den2
        
        dx = -2 * c / den
        x3 = x2 + dx
        historial_x3.append(x3)
        
        error = abs(dx)
        
        # Imprimir fila de la iteración actual (formato a 4 decimales)
        print(f"{i+1:<5} | {x0.real:<10.4f} | {x1.real:<10.4f} | {x2.real:<10.4f} | {a.real:<10.4f} | {b.real:<10.4f} | {c.real:<10.4f} | {x3.real:<12.4f} | {error.real:<10.4e}")

        if error < tol:
            print("=" * 95)
            print(f"Convergencia alcanzada en la iteración {i+1}. Raíz = {x3.real:.6f}")
            break
            
        x0, x1, x2 = x1, x2, x3

    # Gráfica de soporte
    x_vals = np.linspace(-1, 3, 300)
    y_vals = [f(x).real for x in x_vals]
    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x)", color="black")
    plt.axhline(0, color="gray", linestyle="--")
    plt.scatter([x.real for x in historial_x3], [f(x).real for x in historial_x3], color="red", zorder=5, label="Iteraciones x3")
    plt.title("Método de Müller: Convergencia paso a paso")
    plt.grid(True)
    plt.legend()
    plt.show()

# Probar f(x) = x^3 - x - 2
f = lambda x: x**3 - x - 2
metodo_muller_con_tabla(f, x0=0.0, x1=1.0, x2=2.0)