import numpy as np
import matplotlib.pyplot as plt

# 1. DEFINICION DE LA FUNCION Y SU DERIVADA
def f(x):
    """
    Funcion objetivo: f(x) = x^2 - 2
    Buscamos el punto donde x^2 - 2 = 0 (Raiz cuadrada de 2).
    """
    return x**2 - 2

def df(x):
    """
    Primera derivada: f'(x) = 2x
    Nos da la pendiente de la recta tangente en cualquier punto x.
    """
    return 2 * x

# 2. ALGORITMO MANUAL DE NEWTON-RAPHSON
def newton_raphson_manual(x0, tol=1e-6, max_iter=100):
    x = x0
    historial_x = [x]  # Guardamos los puntos para graficar la convergencia
    
    print(f"Punto de inicio: x0 = {x0}")
    
    for i in range(max_iter):
        eval_f = f(x)
        eval_df = df(x)
        
        # Evitar division por cero (si la pendiente es horizontal)
        if eval_df == 0:
            print("Error: Derivada igual a cero. La tangente no cruza el eje X.")
            return None, historial_x
            
        # Formula de Newton-Raphson: x_nuevo = x - f(x)/f'(x)
        x_nuevo = x - (eval_f / eval_df)
        historial_x.append(x_nuevo)
        
        error = abs(x_nuevo - x)
        print(f"Iteracion {i+1:02d} | x = {x_nuevo:.8f} | Error = {error:.8e}")
        
        # Criterio de parada
        if error < tol:
            print(f"Raiz encontrada en x = {x_nuevo:.8f}")
            return x_nuevo, historial_x
            
        x = x_nuevo
        
    return x, historial_x

# 3. EJECUCION Y GRAFICADO
if __name__ == "__main__":
    x0 = 0.5  # Estimacion inicial
    raiz, historial = newton_raphson_manual(x0)

    # Generamos el rango de datos para la grafica
    x_vals = np.linspace(0, 2.5, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(9, 5))
    plt.plot(x_vals, y_vals, label="f(x) = x^2 - 2", color="blue", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1, label="Eje X (y = 0)")
    
    # Graficar el punto exacto de la raiz
    plt.plot(raiz, f(raiz), "ro", markersize=8, label=f"Raiz Exacta: x = {raiz:.6f}")
    
    # Graficar la trayectoria del francotirador (puntos evaluados)
    plt.plot(historial, [f(h) for h in historial], "g^--", alpha=0.6, label="Pasos del algoritmo")

    plt.title("Programa 3.4: Newton-Raphson Manual (Francotirador Matematico)")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()
    plt.show()