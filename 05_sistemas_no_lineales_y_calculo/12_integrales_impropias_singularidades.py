import numpy as np
import matplotlib.pyplot as plt

"""
GUION DE VOZ / ESTILO FEYNMAN:
¿Cómo metes el infinito en una computadora si solo tiene 64 bits de memoria?
Si intentas evaluar f(10^300), obtendrás ZeroDivisionError, Underflow o Overflow.
Peor aún: sumar números diminutos a una suma acumulada genera el fenómeno de
cancelación catastrófica y pérdida de precisión de punto flotante.

El truco de ingeniería no es hacer que la máquina corra hasta el infinito, sino
engañar al espacio. Hacemos una sustitución:
Sea x = 1/t. Cuando x tiende a infinito, t tiende a 0.
dx = -1/t^2 dt.
Hemos transformado un intervalo infinito [1, inf) en uno compacto y seguro (0, 1].
Ahora cualquier cuadratura numérica estándar puede resolverlo en milisegundos.
"""

def integrar_asintotica(f, eps=1e-12, b=1.0, n=1000):
    # Singularidad en x=0 (ej: 1/sqrt(x))
    h = (b - eps) / (n - 1)
    x = np.linspace(eps, b, n)
    puntos_medios = x[:-1] + h / 2.0
    return np.sum(f(puntos_medios)) * h

def integral_dominio_infinito(f, a=0.0, n_puntos=3):
    def gl_base(func, low, high):
        t = np.array([-np.sqrt(3.0 / 5.0), 0.0, np.sqrt(3.0 / 5.0)])
        w = np.array([5.0 / 9.0, 8.0 / 9.0, 5.0 / 9.0])
        c1 = (high - low) / 2.0
        c2 = (low + high) / 2.0
        return c1 * np.sum(w * func(c1 * t + c2))

    # Parte 1: [0, 1] directa
    i1 = gl_base(f, 0.0, 1.0)

    # Parte 2: [1, inf) mediante x = 1/t  =>  dx = 1/t^2 dt
    def f_transformada(t):
        return f(1.0 / t) * (1.0 / (t**2))

    i2 = gl_base(f_transformada, 0.0, 1.0)
    return i1 + i2

def graficar_casos_impropios():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    # Caso 1: Singularidad en x=0
    x_sing = np.linspace(0.01, 1.0, 300)
    y_sing = 1.0 / np.sqrt(x_sing)
    ax1.plot(x_sing, y_sing, color='tab:red', lw=2, label=r'$f(x) = \frac{1}{\sqrt{x}}$')
    ax1.fill_between(x_sing, y_sing, color='tab:red', alpha=0.2)
    ax1.axvline(0.0, color='black', linestyle='--', label=r'Asíntota vertical ($x=0$)')
    ax1.set_ylim(0, 10)
    ax1.set_title("1. Singularidad Asintótica en x=0")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.legend()
    ax1.grid(True, linestyle=':', alpha=0.6)

    # Caso 2: Dominio infinito vs Transformación
    t = np.linspace(0.02, 1.0, 200)
    # g(t) = f(1/t) * (1/t^2) con f(x) = 1/(1 + x^2)
    g_t = (1.0 / (1.0 + (1.0 / t)**2)) * (1.0 / (t**2))
    
    ax2.plot(t, g_t, color='tab:green', lw=2, label=r'$g(t) = \frac{1}{1 + t^2}$')
    ax2.fill_between(t, g_t, color='tab:green', alpha=0.2)
    ax2.set_xlim(0, 1.05)
    ax2.set_ylim(0, 1.1)
    ax2.set_title("2. Dominio Infinito Compactado en (0, 1]")
    ax2.set_xlabel(r"$t = 1/x$")
    ax2.set_ylabel(r"$g(t) = f(1/t) \cdot \frac{1}{t^2}$")
    ax2.legend()
    ax2.grid(True, linestyle=':', alpha=0.6)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("=" * 72)
    print("CLASE 22: TRATAMIENTO DE INTEGRALES IMPROPIAS Y SINGULARIDADES")
    print("=" * 72)

    # CASO 1: Singularidad en x=0
    f_sing = lambda x: 1.0 / np.sqrt(x)
    exacto_sing = 2.0
    aprox_sing = integrar_asintotica(f_sing, eps=1e-10, b=1.0, n=50000)

    print("1. INTEGRAL ASINTÓTICA: f(x) = 1/sqrt(x) en [0, 1]")
    print(f"   Valor Exacto:       {exacto_sing:<15.10f}")
    print(f"   Aproximación Num:   {aprox_sing:<15.10f}")
    print(f"   Error Absoluto:     {abs(exacto_sing - aprox_sing):<15.4e}\n")

    # CASO 2: Límite Infinito en [0, inf)
    f_inf = lambda x: 1.0 / (1.0 + x**2)
    exacto_inf = np.pi / 2.0
    aprox_inf = integral_dominio_infinito(f_inf, a=0.0, n_puntos=3)

    print("2. DOMINIO INFINITO: f(x) = 1/(1 + x^2) en [0, inf)")
    print("   Transformación aplicada en [1, inf): x = 1/t  =>  dx = (1/t^2) dt")
    print(f"   Valor Exacto (pi/2): {exacto_inf:<15.10f}")
    print(f"   Aproximación Num:    {aprox_inf:<15.10f}")
    print(f"   Error Absoluto:      {abs(exacto_inf - aprox_inf):<15.4e}")
    print("=" * 72)

    graficar_casos_impropios()