import numpy as np

# =====================================================================
# PROFESOR DE MÉTODOS NUMÉRICOS: MÉTODO DE SOR (SOBRERRELAJACIÓN SUCESIVA)
# Explicación estilo Feynman (Con peras y manzanas):
# Imagina que estás buscando el volumen ideal de tu radio.
#
# - Si omega (w) = 1: Es Gauss-Seidel normal. Te mueves a paso normal.
# - Si 0 < w < 1 (Sub-relajación): Das pasitos de bebé. Le pones "freno de mano"
#   al algoritmo porque el sistema es tan inestable/salvaje que si das un paso completo,
#   se dispara al infinito (diverge). Amortigua la oscilación.
# - Si 1 < w < 2 (Sobre-relajación): ¡Es como pisar el acelerador! Ves hacia dónde
#   va la tendencia de la corrección y dices: "En lugar de avanzar 1 metro hacia allá,
#   extrapolo y me aviento 1.3 metros de un solo salto".
# =====================================================================

A = np.array([
    [ 4.0, -1.0,  0.0,  0.0,  0.0],
    [-1.0,  4.0, -1.0,  0.0,  0.0],
    [ 0.0, -1.0,  4.0, -1.0,  0.0],
    [ 0.0,  0.0, -1.0,  4.0, -1.0],
    [ 0.0,  0.0,  0.0, -1.0,  4.0]
], dtype=float)

b = np.array([100.0, 50.0, 50.0, 50.0, 100.0], dtype=float)

def sor(A, b, omega, tol=1e-8, max_iter=100, silent=False):
    n = len(b)
    x = np.zeros(n)
    
    if not silent:
        print("=" * 75)
        print(f"   MÉSTATIC DE SOR (omega = {omega}) - COLUMNA DE ABSORCIÓN")
        print("=" * 75)
        print(f"{'Iteración':^10} | {'x1 (Plato 1)':^12} | {'x3 (Plato 3)':^12} | {'x5 (Plato 5)':^12} | {'Error Norma L2':^15}")
        print("-" * 75)
        
    for k in range(1, max_iter + 1):
        x_old = x.copy()
        
        for i in range(n):
            suma = np.sum(A[i, :i] * x[:i]) + np.sum(A[i, i+1:] * x[i+1:])
            # Calculamos el valor de Gauss-Seidel (la propuesta de nuevo paso)
            x_gs = (b[i] - suma) / A[i, i]
            # Extrapolamos combinando el valor anterior con la nueva propuesta
            x[i] = (1.0 - omega) * x[i] + omega * x_gs
            
        error = np.linalg.norm(x - x_old, ord=2)
        
        if not silent:
            print(f"{k:^10} | {x[0]:^12.6f} | {x[2]:^12.6f} | {x[4]:^12.6f} | {error:^15.4e}")
            
        if error < tol:
            if not silent:
                print("-" * 75)
                print(f"¡Convergencia alcanzada en la iteración {k}!")
            return x, k

    return x, max_iter

if __name__ == "__main__":
    # 1. Ejecución detallada con un omega acelerador óptimo (~1.25 para este sistema)
    omega_optimo = 1.25
    solucion, iter_sor = sor(A, b, omega=omega_optimo)
    
    print("\nSolución Final:")
    for idx, val in enumerate(solucion, 1):
        print(f"  Plato {idx}: {val:.6f}")
        
    # 2. Demostración comparativa de aceleración
    _, iter_gs = sor(A, b, omega=1.0, silent=True)  # omega=1.0 es Gauss-Seidel
    
    print("\n" + "=" * 75)
    print("DEMOSTRACIÓN DE VELOCIDAD DE CONVERGENCIA:")
    print("=" * 75)
    print(f"  • Gauss-Seidel (omega = 1.00) : {iter_gs} iteraciones")
    print(f"  • SOR Acelerado (omega = {omega_optimo:.2f}) : {iter_sor} iteraciones")
    
    reduccion = ((iter_gs - iter_sor) / iter_gs) * 100
    print(f"  --> ¡SOR redujo las iteraciones en un {reduccion:.1f}%!")
    print("=" * 75)