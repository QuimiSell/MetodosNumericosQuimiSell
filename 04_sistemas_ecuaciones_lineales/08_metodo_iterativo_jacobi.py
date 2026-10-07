import numpy as np

# =====================================================================
# PROFESOR DE MÉTODOS NUMÉRICOS: MÉTODO DE JACOBI
# Explicación estilo Feynman:
# Imagina que estás haciendo una coreografía grupal. En Jacobi, TODOS
# miran dónde estaban sus compañeros en el SEGUNDO ANTERIOR (la foto anterior)
# y calculan su nuevo paso. Nadie cambia de posición basándose en lo que
# sus compañeros están haciendo en el presente.
#
# ¿Por qué es perfecto para GPUs?
# Como cada elemento de x^(k+1) depende Exclusivamente de la foto anterior x^(k),
# un chip de GPU puede calcular las 10,000 posiciones de un sistema al
# mismo tiempo (en paralelo) sin tener que esperar a que otro núcleo termine.
# =====================================================================

# Sistema de 5 platos de una columna de absorción (Matriz A x = b)
# A representa los balances de materia por plato, b las entradas/salidas.
A = np.array([
    [ 4.0, -1.0,  0.0,  0.0,  0.0],
    [-1.0,  4.0, -1.0,  0.0,  0.0],
    [ 0.0, -1.0,  4.0, -1.0,  0.0],
    [ 0.0,  0.0, -1.0,  4.0, -1.0],
    [ 0.0,  0.0,  0.0, -1.0,  4.0]
], dtype=float)

b = np.array([100.0, 50.0, 50.0, 50.0, 100.0], dtype=float)

def jacobi(A, b, tol=1e-8, max_iter=100):
    n = len(b)
    x_old = np.zeros(n)  # Foto anterior del vector
    x_new = np.zeros(n)  # Espacio para los nuevos valores calculados
    
    print("=" * 75)
    print("   MÉTODO DE JACOBI - COLUMNA DE ABSORCIÓN (5 PLATOS)")
    print("=" * 75)
    print(f"{'Iteración':^10} | {'x1 (Plato 1)':^12} | {'x3 (Plato 3)':^12} | {'x5 (Plato 5)':^12} | {'Error Norma L2':^15}")
    print("-" * 75)
    
    for k in range(1, max_iter + 1):
        # Despejamos cada x_i basándonos ÚNICAMENTE en la foto vieja (x_old)
        for i in range(n):
            suma = np.sum(A[i, :i] * x_old[:i]) + np.sum(A[i, i+1:] * x_old[i+1:])
            x_new[i] = (b[i] - suma) / A[i, i]
            
        # Evaluamos qué tanto cambió la solución (Norma del Error)
        error = np.linalg.norm(x_new - x_old, ord=2)
        
        print(f"{k:^10} | {x_new[0]:^12.6f} | {x_new[2]:^12.6f} | {x_new[4]:^12.6f} | {error:^15.4e}")
        
        if error < tol:
            print("-" * 75)
            print(f"¡Convergencia alcanzada en la iteración {k}!")
            return x_new
            
        # "Tomamos la foto" para la siguiente iteración
        x_old = x_new.copy()

    print("No se alcanzó la tolerancia en las iteraciones máximas.")
    return x_new

if __name__ == "__main__":
    solucion = jacobi(A, b)
    print("\nSolución Final (Concentración/Masa por plato):")
    for idx, val in enumerate(solucion, 1):
        print(f"  Plato {idx}: {val:.6f}")