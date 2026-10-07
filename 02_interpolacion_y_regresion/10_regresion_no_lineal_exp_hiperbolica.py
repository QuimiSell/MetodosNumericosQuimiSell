import numpy as np
import matplotlib.pyplot as plt

def resolver_sistema_lineal(x_trans, y_trans):
    """
    Calcula la pendiente (b) e intersección (A) para datos linealizados
    usando las sumatorias clásicas de mínimos cuadrados.
    """
    n = len(x_trans)
    sum_x = np.sum(x_trans)
    sum_y = np.sum(y_trans)
    sum_x2 = np.sum(x_trans**2)
    sum_xy = np.sum(x_trans * y_trans)
    
    # Sistema de ecuaciones: 
    # n*A + sum_x*b = sum_y
    # sum_x*A + sum_x2*b = sum_xy
    # Resolviendo por fórmulas directas de mínimos cuadrados:
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    A = (sum_y - b * sum_x) / n
    
    return A, b, sum_x, sum_y, sum_x2, sum_xy

# =====================================================================
# DATOS DEL PROBLEMA Y PREDICCIÓN
# =====================================================================
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.5, 4.7, 8.8, 15.9, 30.1])

# ¿Qué valor te pide predecir el ejercicio? (Cambia este número)
x_futuro = 4.5 

n_puntos = len(x)

print("="*60)
print("         DESGLOSE DE PASOS PARA MÉTODOS NUMÉRICOS")
print("="*60)

# =====================================================================
# 1. EJECUCIÓN MODELO EXPONENCIAL (y = a * e^(bx))
#    Linealización: X = x, Y = ln(y) -> Y = A + bX, donde a = e^A
# =====================================================================
X_exp = x
Y_exp = np.log(y)
A_exp, b_exp, sx, sy, sx2, sxy = resolver_sistema_lineal(X_exp, Y_exp)
a_real_exp = np.exp(A_exp)
pred_exp = a_real_exp * np.exp(b_exp * x_futuro)

print("--- 1. MODELO EXPONENCIAL ---")
print(f"Tabla transformada: X = x, Y = ln(y)")
print(f"Sumatorias: ΣX = {sx:.4f}, ΣY = {sy:.4f}, ΣX² = {sx2:.4f}, ΣXY = {sxy:.4f}")
print(f"Coeficientes de la línea: Intersección (A) = {A_exp:.4f}, Pendiente (b) = {b_exp:.4f}")
print(f"Constante original despejada: a = e^A = {a_real_exp:.4f}")
print(f"Ecuación final: y = {a_real_exp:.4f} * e^({b_exp:.4f} * x)")
print(f"Predicción para x = {x_futuro}: y = {pred_exp:.4f}\n")

# =====================================================================
# 2. EJECUCIÓN MODELO POTENCIAL (y = a * x^b)
#    Linealización: X = log10(x), Y = log10(y) -> Y = A + bX, donde a = 10^A
# =====================================================================
X_pot = np.log10(x)
Y_pot = np.log10(y)
A_pot, b_pot, sx, sy, sx2, sxy = resolver_sistema_lineal(X_pot, Y_pot)
a_real_pot = 10**A_pot
pred_pot = a_real_pot * (x_futuro**b_pot)

print("--- 2. MODELO POTENCIAL ---")
print(f"Tabla transformada: X = log10(x), Y = log10(y)")
print(f"Sumatorias: ΣX = {sx:.4f}, ΣY = {sy:.4f}, ΣX² = {sx2:.4f}, ΣXY = {sxy:.4f}")
print(f"Coeficientes de la línea: Intersección (A) = {A_pot:.4f}, Pendiente (b) = {b_pot:.4f}")
print(f"Constante original despejada: a = 10^A = {a_real_pot:.4f}")
print(f"Ecuación final: y = {a_real_pot:.4f} * x^({b_pot:.4f})")
print(f"Predicción para x = {x_futuro}: y = {pred_pot:.4f}\n")

# =====================================================================
# 3. EJECUCIÓN MODELO HIPERBÓLICO (y = 1 / (a + bx))
#    Linealización: X = x, Y = 1/y -> Y = A + bX, donde a = A
# =====================================================================
X_hip = x
Y_hip = 1 / y
A_hip, b_hip, sx, sy, sx2, sxy = resolver_sistema_lineal(X_hip, Y_hip)
pred_hip = 1 / (A_hip + b_hip * x_futuro)

print("--- 3. MODELO HIPERBÓLICO ---")
print(f"Tabla transformada: X = x, Y = 1/y")
print(f"Sumatorias: ΣX = {sx:.4f}, ΣY = {sy:.4f}, ΣX² = {sx2:.4f}, ΣXY = {sxy:.4f}")
print(f"Coeficientes de la línea: Intersección (a) = {A_hip:.4f}, Pendiente (b) = {b_hip:.4f}")
print(f"Ecuación final: y = 1 / ({A_hip:.4f} + {b_hip:.4f} * x)")
print(f"Predicción para x = {x_futuro}: y = {pred_hip:.4f}")
print("="*60)




# =====================================================================
# 4. VISUALIZACIÓN GRÁFICA PROFESIONAL (Estilo Dashboard de Ingeniería)
# =====================================================================
# Vector de X suavizado para curvas continuas limpias
x_curva = np.linspace(min(x) * 0.9, max(x) * 1.1, 300)

# Re-calcular curvas continuas
y_curva_exp = a_real_exp * np.exp(b_exp * x_curva)
y_curva_pot = a_real_pot * (x_curva**b_pot)
y_curva_hip = 1 / (A_hip + b_hip * x_curva)

# Definir estilo limpio y moderno
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(12, 7.5))

# 1. Datos experimentales/ejercicio (Puntos grandes y claros)
ax.scatter(x, y, color='#2c3e50', edgecolor='#e74c3c', s=130, linewidth=2, zorder=5, label='Datos del Enunciado')

# 2. Curvas de los modelos con colores contrastantes y grosores claros
ax.plot(x_curva, y_curva_exp, color='#1abc9c', linestyle='-', linewidth=2.5, label='Ajuste Exponencial')
ax.plot(x_curva, y_curva_pot, color='#3498db', linestyle='--', linewidth=2.5, label='Ajuste Potencial')
ax.plot(x_curva, y_curva_hip, color='#9b59b6', linestyle='-.', linewidth=2.5, label='Ajuste Hiperbólico')

# 3. Puntos de predicción solicitados (Evaluados en x_futuro)
ax.scatter(x_futuro, pred_exp, color='#16a085', marker='s', s=100, zorder=6, label=f'Pred. Exponencial ({pred_exp:.2f})')
ax.scatter(x_futuro, pred_pot, color='#2980b9', marker='^', s=110, zorder=6, label=f'Pred. Potencial ({pred_pot:.2f})')
ax.scatter(x_futuro, pred_hip, color='#8e44ad', marker='D', s=90, zorder=6, label=f'Pred. Hiperbólica ({pred_hip:.2f})')

# Línea vertical punteada que cruza por la X calculada para guiar la vista
ax.axvline(x_futuro, color='#7f8c8d', linestyle=':', linewidth=1.2, alpha=0.7, label=f'X a Evaluar = {x_futuro}')

# 4. Cuadro de texto flotante con las ecuaciones calculadas (Para que el alumno no adivine)
texto_ecuaciones = (
    f"Ecuaciones Resultantes:\n"
    f"───────────────────\n"
    f"Exp: y = {a_real_exp:.3f} * e^({b_exp:.3f}*x)\n"
    f"Pot: y = {a_real_pot:.3f} * x^({b_pot:.3f})\n"
    f"Hip: y = 1 / ({A_hip:.3f} + {b_hip:.3f}*x)"
)
props_caja = dict(boxstyle='round,pad=0.6', facecolor='#f8f9fa', edgecolor='#bdc3c7', alpha=0.95)
ax.text(0.03, 0.05, texto_ecuaciones, transform=ax.transAxes, fontsize=10, fontfamily='monospace', verticalalignment='bottom', bbox=props_caja)

# Ajustes de etiquetas y títulos limpios
ax.set_title('Laboratorio de Métodos Numéricos: Regresiones No Lineales', fontsize=15, fontweight='bold', color='#2c3e50', pad=15)
ax.set_xlabel('Variable Independiente (X)', fontsize=12, fontweight='bold', color='#34495e', labelpad=10)
ax.set_ylabel('Variable Dependiente (Y)', fontsize=12, fontweight='bold', color='#34495e', labelpad=10)

# Refinar la cuadrícula
ax.grid(True, linestyle='--', alpha=0.5, color='#cccccc')
ax.tick_params(colors='#34495e', labelsize=10)

# Mover la leyenda afuera o en una esquina limpia para que no tape los datos
ax.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='#e2e8f0', shadow=True, fontsize=10)

plt.tight_layout()
plt.show()