"""
======================================================================
CLASE 20: DIFERENCIACION NUMERICA
SCRIPT 1: EL DILEMA DEL PASO 'h' Y LA CANCELACION SUSTRACTIVA
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Que nos dice el analisis matematico puro?
   Segun el calculo diferencial, la derivada es el limite cuando h tiende a 0.
   En papel, mientras mas pequeno sea h, mejor es la aproximacion.
   El error de truncamiento (lo que dejamos fuera en Taylor) decrece como O(h)
   o O(h^2).

2. ¿Que dice la computadora real (IEEE-754 de 64 bits)?
   La computadora no tiene infinitos decimales, tiene ~16 digitos de precision.
   Cuando eliges un h ridículamente pequeno (como 10^-14), f(x + h) y f(x)
   son casi identicos en sus primeros 15 decimales.
   
3. El monstruo de la CANCELACION SUSTRACTIVA:
   Al restar f(x + h) - f(x), se cancelan los digitos mas significativos y
   nos quedamos unicamente con basura numerica (ruido de redondeo).
   Luego, divides esa basura entre un numero minusculo (h), ¡lo cual amplifica
   el error hasta 10^14 veces!
   
   Por eso la curva tiene forma de 'V':
   - A la derecha: Domina el error de truncamiento matematico.
   - A la izquierda: Domina el error de redondeo computacional.
   - El punto optimo para diferencias centradas suele rondar h ≈ 10^-5 o 10^-6.
"""

import numpy as np
import matplotlib.pyplot as plt

# ====================================================================
# SECCION EDUCATIVA: DEFINICION DE FUNCIONES Y DERIVADA ANALITICA
# Funcion de prueba: f(x) = sin(x)
# Derivada exacta:   f'(x) = cos(x)
# ====================================================================

def f(x):
    return np.sin(x)

def df_exacta(x):
    return np.cos(x)


# ====================================================================
# FORMULAS DE DIFERENCIAS FINITAS
# ====================================================================

def dif_adelante(x, h):
    """Orden O(h)"""
    return (f(x + h) - f(x)) / h

def dif_atras(x, h):
    """Orden O(h)"""
    return (f(x) - f(x - h)) / h

def dif_centrada(x, h):
    """Orden O(h^2)"""
    return (f(x + h) - f(x - h)) / (2.0 * h)


# ====================================================================
# EXPERIMENTO NUMERICO
# ====================================================================

def ejecutar_experimento_paso_h():
    x0 = 1.0  # Evaluamos en x = 1 radián
    valor_real = df_exacta(x0)

    # Generamos pasos h desde 10^0 hasta 10^-16
    h_valores = np.logspace(0, -16, num=100)

    errores_adelante = []
    errores_atras = []
    errores_centrada = []

    for h in h_valores:
        aprox_fwd = dif_adelante(x0, h)
        aprox_bwd = dif_atras(x0, h)
        aprox_cen = dif_centrada(x0, h)

        errores_adelante.append(abs(aprox_fwd - valor_real))
        errores_atras.append(abs(aprox_bwd - valor_real))
        errores_centrada.append(abs(aprox_cen - valor_real))

    # Convertimos a arreglos para busqueda de minimos
    errores_centrada = np.array(errores_centrada)
    idx_optimo = np.argmin(errores_centrada)
    h_optimo = h_valores[idx_optimo]
    error_minimo = errores_centrada[idx_optimo]

    # Reporte en consola
    print("=" * 70)
    print(" ANALISIS DEL DILEMA DEL PASO 'h' (f(x) = sin(x), x = 1.0)")
    print("=" * 70)
    print(f" Valor exacto de f'(1.0): {valor_real:.16f}")
    print(f" Paso optimo detectado (Centrada): h = {h_optimo:.2e}")
    print(f" Error minimo alcanzado:          {error_minimo:.2e}")
    print("-" * 70)
    print(" Observa como para h < 10^-8 el error se dispara por cancelacion.")
    print("=" * 70)

    # Generacion del grafico explicativo
    plt.figure(figsize=(10, 6))
    plt.loglog(h_valores, errores_adelante, label="Hacia adelante O(h)", linestyle="--", color="blue")
    plt.loglog(h_valores, errores_atras, label="Hacia atras O(h)", linestyle=":", color="green")
    plt.loglog(h_valores, errores_centrada, label="Centrada O(h²)", linewidth=2, color="crimson")

    plt.axvline(h_optimo, color="black", linestyle="-.", alpha=0.6, label=f"h optimo ≈ {h_optimo:.1e}")
    
    plt.title("El Dilema del Paso $h$: Truncamiento vs Cancelacion Sustractiva", fontsize=13)
    plt.xlabel("Tamano del paso $h$ (Escala logaritmica)", fontsize=11)
    plt.ylabel("Error absoluto |Aproximacion - Exacto|", fontsize=11)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ejecutar_experimento_paso_h()