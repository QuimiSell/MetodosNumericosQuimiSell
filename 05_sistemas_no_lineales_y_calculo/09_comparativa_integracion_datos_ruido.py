"""
Clase 21 - Script 3: Datos de Laboratorio con Ruido y Uso de Scipy
Metodos: scipy.integrate.trapezoid y scipy.integrate.simpson
Grafica comparativa con areas sombreadas usando Matplotlib.

EXPLICACION DIDACTICA (ESTILO FEYNMAN):
1. Por que la integracion es un suavizador de ruido?
   El ruido de alta frecuencia en sensores oscila rapidamente alrededor de cero
   (a veces positivo, a veces negativo).
   - Derivada: calcula pendientes [y(i+1) - y(i)] / h. Cuando h es chico, dos puntos
     con ruido producen pendientes gigantescas. La derivada amplifica el ruido.
   - Integral: suma areas. Al sumar, los picos positivos cancelan a los valles negativos.
     La integral es un filtro pasa-bajas natural que promedia y amortigua el error aleatorio.

2. Conexion directa con la Inteligencia Artificial:
   - Esperanza matematica: E[X] = Integral(x * p(x) dx). En aprendizaje probabilistico,
     calcular momentos o medias exige integrar distribuciones continuas.
   - Curvas ROC y Precision-Recall: La metrica estandar AUC (Area Under Curve) se evalua
     directamente aplicando la regla del trapecio sobre los falsos positivos y verdaderos positivos.
   - Normalizacion en modelos generativos: En modelos de energia y VAEs continuos, la constante
     de particion Z = Integral(exp(-E(x)) dx) se aproxima usando integracion numerica o Monte Carlo.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson, trapezoid

# Semilla fija para reproducibilidad de la leccion
np.random.seed(42)

# Simulacion de adquisicion de senal en 15 muestras (n = 14 intervalos, numero PAR)
n_puntos = 15
t = np.linspace(0.0, 6.0, n_puntos)

# Senal base pura y senal ruidosa de sensor
senal_pura = lambda x: 5.0 * np.exp(-0.3 * x) * np.sin(1.2 * x) + 2.0
ruido_gaussiano = np.random.normal(loc=0.0, scale=0.35, size=n_puntos)
lecturas_sensor = senal_pura(t) + ruido_gaussiano

# 1. Calculo con scipy.integrate
integral_trapecio = trapezoid(y=lecturas_sensor, x=t)
integral_simpson = simpson(y=lecturas_sensor, x=t)

# 2. Integracion de alta resolucion de la senal limpia para comparar
t_fino = np.linspace(0.0, 6.0, 1000)
integral_referencia = trapezoid(y=senal_pura(t_fino), x=t_fino)

# Salida en consola formateada
print("=====================================================================")
print("RESULTADOS DE INTEGRACION SOBRE DATOS DISCRETOS DE SENSOR")
print("=====================================================================")
print(f"Puntos de muestreo : {n_puntos} (14 subintervalos)")
print(f"Referencia limpia  : {integral_referencia:12.6f}")
print(f"scipy.trapezoid    : {integral_trapecio:12.6f} | Error: {abs(integral_referencia - integral_trapecio):.4e}")
print(f"scipy.simpson      : {integral_simpson:12.6f} | Error: {abs(integral_referencia - integral_simpson):.4e}")
print("=====================================================================")

# 3. Grafica didactica con Matplotlib
fig, ax = plt.subplots(figsize=(10, 5.5))

# Curva teorica continua
ax.plot(t_fino, senal_pura(t_fino), "b-", linewidth=2.0, label="Senal real continua (sin ruido)")

# Puntos discretos medidos por el sensor
ax.scatter(t, lecturas_sensor, color="red", s=45, zorder=5, label="Lecturas discretas de sensor")

# Area sombreada aproximada por trapecios
ax.fill_between(t, 0, lecturas_sensor, color="orange", alpha=0.30, step=None, label="Area aproximada (Trapecios)")

# Visualizacion de los trapecios individuales con lineas verticales
for ti, yi in zip(t, lecturas_sensor):
    ax.vlines(x=ti, ymin=0, ymax=yi, color="gray", linestyle="--", alpha=0.6)

ax.set_title("Integracion Numerica de Senal con Ruido (Clase 21)", fontsize=13, fontweight="bold")
ax.set_xlabel("Tiempo t [s]", fontsize=11)
ax.set_ylabel("Amplitud del sensor [V]", fontsize=11)
ax.set_xlim(0.0, 6.0)
ax.set_ylim(bottom=0.0)
ax.grid(True, linestyle=":", alpha=0.6)
ax.legend(loc="upper right", frameon=True)

plt.tight_layout()
plt.show()