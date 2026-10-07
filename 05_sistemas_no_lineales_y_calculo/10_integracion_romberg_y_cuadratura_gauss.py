import numpy as np
import matplotlib.pyplot as plt

"""
GUION DE VOZ / ESTILO FEYNMAN:
¿Por qué Gauss-Legendre no usa nodos equiespaciados como la regla del Trapecio o Simpson?
Imagina que te doy permiso de elegir dónde colocar n puntos de muestreo en una curva.
En Simpson estás obligado a ponerlos a distancias idénticas; estás 'atado de manos'.
Gauss dijo: 'Si tengo 2n grados de libertad (n posiciones x_i y n pesos w_i),
¿por qué desperdiciarlos en puntos fijos?' Al dejar flotar las posiciones,
podemos integrar con exactitud polinomios de grado hasta 2n - 1.

¿Por qué necesita la función continua f(x) y no datos tabulados?
Porque las raíces de los polinomios de Legendre casi nunca caen en enteros o divisiones
cómodas. Son números irracionales como +/- 1/sqrt(3). Si tus datos provienen de sensores
que miden cada 1 segundo exacto, Gauss-Legendre no te sirve directamente: necesitas
evaluar f(x) en el punto exacto donde la matemática lo exige.
"""

def integracion_romberg(f, a, b, max_iter=5, tol=1e-8):
    R = np.zeros((max_iter, max_iter))
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))
    
    for i in range(1, max_iter):
        h /= 2.0
        puntos = a + (2 * np.arange(1, 2**(i - 1)) - 1) * h
        suma_impares = np.sum(f(puntos))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * suma_impares
        
        for k in range(1, i + 1):
            factor = 4**k
            R[i, k] = (factor * R[i, k - 1] - R[i - 1, k - 1]) / (factor - 1)
            
        if abs(R[i, i] - R[i - 1, i - 1]) < tol:
            return R[:i + 1, :i + 1], R[i, i]
            
    return R, R[max_iter - 1, max_iter - 1]

def gauss_legendre(f, a, b, n_puntos=2):
    # Cambio de variable: x = ((b - a)*t + (a + b)) / 2  =>  dx = (b - a)/2 * dt
    c1 = (b - a) / 2.0
    c2 = (a + b) / 2.0
    
    if n_puntos == 2:
        t = np.array([-1.0 / np.sqrt(3.0), 1.0 / np.sqrt(3.0)])
        w = np.array([1.0, 1.0])
    elif n_puntos == 3:
        t = np.array([-np.sqrt(3.0 / 5.0), 0.0, np.sqrt(3.0 / 5.0)])
        w = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])
    else:
        raise ValueError("Implementado para n_puntos = 2 o 3.")
        
    x = c1 * t + c2
    integral = c1 * np.sum(w * f(x))
    return integral, x, w

def graficar_comparacion(f, a, b, nodos_gl2, nodos_gl3):
    x_curva = np.linspace(a, b, 200)
    y_curva = f(x_curva)
    
    # Nodos equiespaciados de Simpson 1/3 (3 puntos)
    nodos_simp = np.linspace(a, b, 3)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    
    # Panel 1: Función y evaluación en los nodos
    ax1.plot(x_curva, y_curva, 'black', lw=1.8, label='$f(x) = x e^{2x}$')
    ax1.fill_between(x_curva, y_curva, color='gray', alpha=0.15, label='Área bajo la curva')
    ax1.scatter(nodos_gl3, f(nodos_gl3), color='tab:blue', s=70, zorder=5, label='Muestreo Gauss-Legendre (3 pts)')
    ax1.scatter(nodos_simp, f(nodos_simp), color='tab:red', marker='s', s=60, zorder=5, label='Muestreo Simpson (3 pts)')
    ax1.set_ylabel('$f(x)$')
    ax1.set_title('Función Continua vs Puntos de Muestreo')
    ax1.legend(loc='upper left', frameon=True)
    ax1.grid(True, linestyle=':', alpha=0.6)
    
    # Panel 2: Comparativa de posiciones de nodos
    ax2.axhline(1.0, color='gray', linestyle='--', linewidth=0.8)
    ax2.axhline(2.0, color='gray', linestyle='--', linewidth=0.8)
    ax2.axhline(3.0, color='gray', linestyle='--', linewidth=0.8)
    
    ax2.plot(nodos_simp, [3.0]*len(nodos_simp), 's', color='tab:red', markersize=8, label='Newton-Cotes / Simpson (3 pts)')
    ax2.plot(nodos_gl3, [2.0]*len(nodos_gl3), 'o', color='tab:blue', markersize=8, label='Gauss-Legendre (3 pts)')
    ax2.plot(nodos_gl2, [1.0]*len(nodos_gl2), '^', color='tab:green', markersize=8, label='Gauss-Legendre (2 pts)')
    
    ax2.set_yticks([1.0, 2.0, 3.0])
    ax2.set_yticklabels(['Gauss (2 pts)', 'Gauss (3 pts)', 'Simpson (3 pts)'])
    ax2.set_xlabel('$x$')
    ax2.set_title('Distribución Espacial de los Nodos en el Intervalo')
    ax2.set_ylim(0.5, 3.5)
    ax2.grid(axis='x', linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    f = lambda x: x * np.exp(2 * x)
    a, b = 0.0, 1.0
    val_exacto = 0.25 * (np.exp(2) + 1.0)
    
    # 1. Romberg
    tabla_r, val_romberg = integracion_romberg(f, a, b, max_iter=4)
    
    # 2. Gauss-Legendre
    val_gl2, x_gl2, _ = gauss_legendre(f, a, b, n_puntos=2)
    val_gl3, x_gl3, _ = gauss_legendre(f, a, b, n_puntos=3)
    
    print("=" * 70)
    print("CLASE 22: INTEGRACIÓN AVANZADA - ROMBERG Y GAUSS-LEGENDRE")
    print("=" * 70)
    print(f"Integral de f(x) = x*e^(2x) en [{a}, {b}] | Valor Exacto: {val_exacto:.10f}\n")
    
    print("--- PIRÁMIDE DE ROMBERG ---")
    for i in range(tabla_r.shape[0]):
        fila = [f"{tabla_r[i, j]:12.8f}" for j in range(i + 1)]
        print(f"k={i} | " + " ".join(fila))
    print()
    
    print("--- TABLA COMPARATIVA DE PRECISIÓN ---")
    print(f"{'Método':<25} | {'Aproximación':<16} | {'Error Absoluto':<16}")
    print("-" * 63)
    metodos = [
        ("Romberg (Orden 6, R[3,3])", val_romberg),
        ("Gauss-Legendre (2 pts)", val_gl2),
        ("Gauss-Legendre (3 pts)", val_gl3)
    ]
    for nombre, aprox in metodos:
        error = abs(val_exacto - aprox)
        print(f"{nombre:<25} | {aprox:<16.10f} | {error:<16.4e}")
    print("=" * 70)
    
    graficar_comparacion(f, a, b, x_gl2, x_gl3)