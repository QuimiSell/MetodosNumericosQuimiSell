"""
======================================================================
CLASE 20: DIFERENCIACION NUMERICA
SCRIPT 2: EXTRAPOLACION DE RICHARDSON (CANCELACION ALGEBRAICA DE ERROR)
======================================================================

EXPLICACION SENCILLA (ESTILO FEYNMAN PARA EL VIDEO):
---------------------------------------------------
1. ¿Cual es la idea genial de Lewis Richardson?
   Sabemos por la serie de Taylor que la diferencia centrada D(h) tiene la forma:
      D(h) = f'(x) + C1 * h^2 + C2 * h^4 + ...
   Si calculamos la misma derivada usando un paso doble (2h):
      D(2h) = f'(x) + C1 * (2h)^2 + C2 * (2h)^4 + ...
            = f'(x) + 4 * C1 * h^2 + 16 * C2 * h^4 + ...

2. ¿Como eliminamos el error algebraicamente?
   Observa el termino C1 * h^2. Multiplicamos la primera ecuacion por 4 y le
   restamos la segunda:
      4 * D(h) - D(2h) = 3 * f'(x) + 0 * h^2 + Terminos de O(h^4)
   Despejando f'(x):
      f'(x) ≈ [ 4 * D(h) - D(2h) ] / 3
   
   ¡Magia pura! Sin calcular mas derivadas ni evaluar funciones extranas,
   matamos el error cuadratico O(h^2) y saltamos a precision de cuarto orden O(h^4).
"""

import numpy as np

# ====================================================================
# SECCION PARA LA TAREA: DEFINICION DE FUNCION
# f(x) = exp(x)
# f'(x) = exp(x), f''(x) = exp(x)
# ====================================================================

def f(x):
    return np.exp(x)

def df_exacta(x):
    return np.exp(x)

def d2f_exacta(x):
    return np.exp(x)


# ====================================================================
# PRIMERA DERIVADA: FORMULAS
# ====================================================================

def d1_centrada(x, h):
    """Primera derivada centrada O(h^2)"""
    return (f(x + h) - f(x - h)) / (2.0 * h)

def d1_richardson(x, h):
    """Extrapolacion de Richardson para primera derivada O(h^4)"""
    d_h = d1_centrada(x, h)
    d_2h = d1_centrada(x, 2.0 * h)
    return (4.0 * d_h - d_2h) / 3.0


# ====================================================================
# SEGUNDA DERIVADA: FORMULAS
# ====================================================================

def d2_centrada(x, h):
    """Segunda derivada centrada O(h^2)"""
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h**2)

def d2_richardson(x, h):
    """Extrapolacion de Richardson para segunda derivada O(h^4)"""
    d2_h = d2_centrada(x, h)
    d2_2h = d2_centrada(x, 2.0 * h)
    return (4.0 * d2_h - d2_2h) / 3.0


# ====================================================================
# DEMOSTRACION EN CONSOLA
# ====================================================================

def comparar_richardson():
    x0 = 1.0
    val_d1 = df_exacta(x0)
    val_d2 = d2f_exacta(x0)

    pasos = [0.4, 0.2, 0.1, 0.05, 0.025]

    print("=" * 82)
    print(" TABLA COMPARATIVA: PRIMERA DERIVADA (f(x) = exp(x), x = 1.0)")
    print("=" * 82)
    print(f"{'h':<8} | {'D1 Centrada O(h^2)':<20} | {'Error Centrada':<15} | {'D1 Richardson O(h^4)':<20} | {'Error Richardson':<15}")
    print("-" * 88)

    for h in pasos:
        cen = d1_centrada(x0, h)
        err_cen = abs(cen - val_d1)

        rich = d1_richardson(x0, h)
        err_rich = abs(rich - val_d1)

        print(f"{h:<8.3f} | {cen:<20.10f} | {err_cen:<15.4e} | {rich:<20.10f} | {err_rich:<15.4e}")

    print("\n" + "=" * 82)
    print(" TABLA COMPARATIVA: SEGUNDA DERIVADA (f(x) = exp(x), x = 1.0)")
    print("=" * 82)
    print(f"{'h':<8} | {'D2 Centrada O(h^2)':<20} | {'Error Centrada':<15} | {'D2 Richardson O(h^4)':<20} | {'Error Richardson':<15}")
    print("-" * 88)

    for h in pasos:
        cen2 = d2_centrada(x0, h)
        err_cen2 = abs(cen2 - val_d2)

        rich2 = d2_richardson(x0, h)
        err_rich2 = abs(rich2 - val_d2)

        print(f"{h:<8.3f} | {cen2:<20.10f} | {err_cen2:<15.4e} | {rich2:<20.10f} | {err_rich2:<15.4e}")
    print("=" * 88)

if __name__ == "__main__":
    comparar_richardson()