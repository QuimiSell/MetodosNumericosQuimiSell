import numpy as np
import matplotlib.pyplot as plt

# 1. FUNCION CON RAIZ MULTIPLE (DOBLE) EN x = 2
def f(x):
    # f(x) = (x - 2)^2 * (x - 4)
    return ((x - 2)**2) * (x - 4)

def df(x):
    # Primera derivada: f'(x) = 3x^2 - 16x + 20
    return 3 * x**2 - 16 * x + 20

def d2f(x):
    # Segunda derivada: f''(x) = 6x - 16
    return 6 * x - 16

# 2. ALGORITMO MODIFICADO (INCORPORA SEGUNDA DERIVADA)
def newton_modificado(x0, tol=1e-6, max_iter=100):
    x = x0
    print(f"Inicio desde x0 = {x0}")
    
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        d2fx = d2f(x)
        
        # Denominador ajustado con f''(x) para no perder velocidad en raices multiples
        denominador = (dfx**2) - (fx * d2fx)
        
        if denominador == 0:
            print("Error: Denominador cero.")
            return None
            
        # Formula de Newton Modificado
        x_nuevo = x - (fx * dfx) / denominador
        error = abs(x_nuevo - x)
        
        print(f"Iteracion {i+1:02d} | x = {x_nuevo:.8f} | Error = {error:.8e}")
        
        if error < tol:
            print(f"Raiz multiple encontrada en x = {x_nuevo:.8f}")
            return x_nuevo
            
        x = x_nuevo
        
    return x

# 3. GRAFICADO Y DEMOSTRACION
if __name__ == "__main__":
    x0 = 1.0  # Punto inicial cercano a la raiz doble x=2
    raiz = newton_modificado(x0)

    x_vals = np.linspace(0.5, 4.5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x) = (x-2)^2 * (x-4)", color="purple", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    
    # Resaltar la raiz multiple encontrada (donde la curva toca tangencialmente el eje X)
    plt.plot(raiz, 0, "ro", markersize=10, label=f"Raiz Doble Exacta: x = {raiz:.6f}")
    plt.plot(4.0, 0, "bo", markersize=7, label="Otra Raiz Simple: x = 4.000000")

    plt.title("Programa 3.6: Newton Modificado (Correccion para Raices Multiples)")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.show()