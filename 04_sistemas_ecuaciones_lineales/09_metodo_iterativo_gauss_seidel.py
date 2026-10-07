import numpy as np

# =====================================================================
# PROFESOR DE MÉTODOS NUMÉRICOS: MÉTODO DE GAUSS-SEIDEL
# Explicación estilo Feynman:
# Imagina la misma coreografía, pero ahora el bailarin 2 no espera a la foto
# del segundo anterior: si el bailarín 1 ya se movió HACE UN SEGUNDO, el 2
# usa la posición ACTUAL de 1 de inmediato.
#
# ¿Por qué ahorra la mitad de memoria RAM?
# En Jacobi necesitas DOS arreglos en memoria RAM: uno para guardar la "foto vieja"
# y otro para escribir los "datos nuevos". En Gauss-Seidel solo usas UN arreglo:
# vas sobrescribiendo sobre la misma marcha ("en caliente"). Ahorras el 50% de RAM.
# =====================================================================

A = np.array([
    [ 4.0, -1.0,  0.0,  0.0,  0.0],
    [-1.0,  4.0, -1.0,  0.0,  0.0],
    [ 0.0, -1.0,  4.0, -1.0,  0.0],
    [ 0.0,  0.0, -1.0,  4.0, -1.0],
    [ 0.0,  0.0,  0.0, -1.0,  4.0]
], dtype=float)

b = np.array([100.0, 50.0, 50.0, 50.0, 100.0], dtype=float)

def gauss_seidel(A, b, tol=1e-8, max_iter=100):
    n = len(b)
    x = np.zeros(n)  # ¡Solo UN arreglo de memoria! Sobrescribimos en caliente.
    
    print("=" * 75)
    print("   MÉTODO DE GAUSS-SEIDEL - COLUMNA DE ABSORCIÓN (5 PLATOS)")
    print("=" * 75)
    print(f"{'Iteración':^10} | {'x1 (Plato 1)':^12} | {'x3 (Plato 3)':^12} | {'x5 (Plato 5)':^12} | {'Error Norma L2':^15}")
    print("-" * 75)
    
    for k in range(1, max_iter + 1):
        x_old = x.copy()  # Solo para medir el error de la iteración completa
        
        for i in range(n):
            # Usamos x[:i] que YA TIENE los valores actualizados en ESTA misma iteración
            suma = np.sum(A[i, :i] * x[:i]) + np.sum(A[i, i+1:] * x[i+1:])
            x[i] = (b[i] - suma) / A[i, i]  # Sobrescritura directa
            
        error = np.linalg.norm(x - x_old, ord=2)
        
        print(f"{k:^10} | {x[0]:^12.6f} | {x[2]:^12.6f} | {x[4]:^12.6f} | {error:^15.4e}")
        
        if error < tol:
            print("-" * 75)
            print(f"¡Convergencia alcanzada en la iteración {k}!")
            return x

    print("No se alcanzó la tolerancia en las iteraciones máximas.")
    return x

if __name__ == "__main__":
    solucion = gauss_seidel(A, b)
    print("\nSolución Final (Concentración/Masa por plato):")
    for idx, val in enumerate(solucion, 1):
        print(f"  Plato {idx}: {val:.6f}")