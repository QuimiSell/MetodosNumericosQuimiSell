"""
===============================================================================
CLASE 23: Método de Euler Estándar vs. Euler Modificado (Predictor-Corrector)
===============================================================================
Propósito:
  Demostrar cómo la corrección de la pendiente en Euler Modificado reduce el
  error global de O(h) a O(h²) al resolver un Problema de Valor Inicial (PVI).

PVI de prueba:
  dy/dt = y - t^2 + 1,   y(0) = 0.5   en el intervalo t ∈ [0, 2]
  Solución analítica:    y(t) = (t + 1)^2 - 0.5 * exp(t)
===============================================================================
"""

import numpy as np


# -----------------------------------------------------------------------------
# 1. Definición del Problema de Valor Inicial (PVI)
# -----------------------------------------------------------------------------
def f(t, y):
    """Ecuación diferencial: dy/dt = f(t, y)"""
    return y - t**2 + 1


def y_exacta(t):
    """Solución analítica exacta para cálculo de errores."""
    return (t + 1) ** 2 - 0.5 * np.exp(t)


# -----------------------------------------------------------------------------
# 2. Algoritmos Numéricos
# -----------------------------------------------------------------------------
def euler_estandar(f, t0, y0, tf, h):
    """
    EXPLICACIÓN FEYNMAN (Euler Estándar):
    Imagina que vas conduciendo a ciegas con la mirada fija únicamente en la velocidad
    del instante actual. Si el camino se curva hacia arriba, tú sigues recto en la
    dirección inicial durante todo el tramo 'h'.
    Al final del paso, estás desviado porque ignoraste la curvatura.
    Por eso su error acumulado es de primer orden: O(h).
    """
    n_pasos = int(np.round((tf - t0) / h))
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0

    for i in range(n_pasos):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y


def euler_modificado(f, t0, y0, tf, h):
    """
    EXPLICACIÓN FEYNMAN (Euler Modificado / Predictor-Corrector):
    ¿Cómo corregimos la ceguera de Euler Estándar?
    1. PASO PREDICTOR: Damos un "salto provisional" con la pendiente inicial para
       adivinar dónde estaríamos al final del intervalo: y_pred = y_i + h * f(t_i, y_i).
    2. PASO CORRECTOR: Calculamos la pendiente en ese punto futuro adivinado: f(t_{i+1}, y_pred).
    3. PROMEDIO: Promediamos la pendiente inicial y la pendiente futura.
       Usar el promedio de ambas pendientes equivale a tomar la recta tangente en el centro
       del intervalo (Regla del Trapecio). Esto elimina el sesgo de la primera derivada y
       eleva la precisión a segundo orden: O(h²).
    """
    n_pasos = int(np.round((tf - t0) / h))
    t = np.linspace(t0, tf, n_pasos + 1)
    y = np.zeros(n_pasos + 1)
    y[0] = y0

    for i in range(n_pasos):
        # 1. Predictor (Euler Estándar)
        k1 = f(t[i], y[i])
        y_pred = y[i] + h * k1

        # 2. Corrector (Evaluación en el punto futuro)
        k2 = f(t[i + 1], y_pred)

        # 3. Actualización con la pendiente promedio
        y[i + 1] = y[i] + (h / 2.0) * (k1 + k2)

    return t, y


# -----------------------------------------------------------------------------
# 3. Análisis de Convergencia
# -----------------------------------------------------------------------------
def ejecutar_analisis_convergencia():
    t0, y0, tf = 0.0, 0.5, 2.0
    pasos_h = [0.5, 0.1, 0.01]
    val_exacto = y_exacta(tf)

    print("=" * 80)
    print(" ESTUDIO DE CONVERGENCIA EN t = 2.0 (Valor Exacto = {:.6f})".format(val_exacto))
    print("=" * 80)
    print(f"{'Paso (h)':<10} | {'Euler Est.':<12} | {'Error Abs.':<12} | {'Euler Mod.':<12} | {'Error Abs.':<12}")
    print("-" * 80)

    for h in pasos_h:
        _, y_e = euler_estandar(f, t0, y0, tf, h)
        _, y_m = euler_modificado(f, t0, y0, tf, h)

        err_e = abs(val_exacto - y_e[-1])
        err_m = abs(val_exacto - y_m[-1])

        print(f"{h:<10.2f} | {y_e[-1]:<12.6f} | {err_e:<12.6e} | {y_m[-1]:<12.6f} | {err_m:<12.6e}")

    print("=" * 80)
    print("\nOBSERVACIÓN PEDAGÓGICA PARA EL VIDEO:")
    print("• Al reducir h por un factor de 10 (de 0.1 a 0.01):")
    print("  - El error en Euler Estándar disminuye ~10 veces (Proporcional a h -> O(h)).")
    print("  - El error en Euler Modificado disminuye ~100 veces (Proporcional a h² -> O(h²)).\n")


if __name__ == "__main__":
    ejecutar_analisis_convergencia()