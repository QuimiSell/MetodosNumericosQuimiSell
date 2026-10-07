import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# -----------------------------------------------------------------------------
# 1. OBJETOS DEL MUNDO EN 2D (Coordenadas originales)
# -----------------------------------------------------------------------------
# Un cuadrado unitario (Área original = 1)
cuadrado_base = np.array([
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
])

# Un objeto gráfico (Casa de prueba)
casa_base = np.array([
    [0, 2, 2, 1, 0, 0, 0.5, 0.5, 1.5, 1.5, 2], # X
    [0, 0, 2, 3, 2, 0, 0.0, 1.0, 1.0, 0.0, 0]  # Y
])

# -----------------------------------------------------------------------------
# 2. CONFIGURACIÓN DE LA FIGURA DE MATPLOTLIB
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.3)

# Dibujar la figura original en gris de fondo para comparar
ax.plot(casa_base[0, :], casa_base[1, :], '--', color='gray', alpha=0.5, label='Original')
ax.fill(cuadrado_base[0, :], cuadrado_base[1, :], color='gray', alpha=0.2, label='Área Base (1.0)')

# Elementos transformados dinámicos
linea_transformada, = ax.plot([], [], 'o-', color='crimson', lw=2.5, label='Mundo Transformado')
poligono_transformado = ax.fill([], [], color='red', alpha=0.3)[0]

# Estética del sistema cartesiano
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.axhline(0, color='black', linewidth=0.8)
ax.axvline(0, color='black', linewidth=0.8)
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_aspect('equal')
ax.set_title("EMULADOR 2D: Efecto del Determinante en la Pantalla", fontsize=12, fontweight='bold')

# Texto informativo en pantalla
texto_det = ax.text(-5.5, 5.0, "", fontsize=11, bbox=dict(boxstyle="round", facecolor="white", edgecolor="gray"))

# -----------------------------------------------------------------------------
# 3. CONTROLES INTERACTIVOS (SLIDERS PARA LA MATRIZ A)
# -----------------------------------------------------------------------------
ax_a = plt.axes([0.15, 0.18, 0.3, 0.03])
ax_b = plt.axes([0.60, 0.18, 0.3, 0.03])
ax_c = plt.axes([0.15, 0.10, 0.3, 0.03])
ax_d = plt.axes([0.60, 0.10, 0.3, 0.03])

slider_a = Slider(ax_a, 'a (m11)', -3.0, 3.0, valinit=1.0)
slider_b = Slider(ax_b, 'b (m12)', -3.0, 3.0, valinit=0.0)
slider_c = Slider(ax_c, 'c (m21)', -3.0, 3.0, valinit=0.0)
slider_d = Slider(ax_d, 'd (m22)', -3.0, 3.0, valinit=1.0)

# -----------------------------------------------------------------------------
# 4. LÓGICA DE TRANSFORMACIÓN
# -----------------------------------------------------------------------------
def actualizar(val):
    # Construir la matriz de transformación A
    A = np.array([
        [slider_a.val, slider_b.val],
        [slider_c.val, slider_d.val]
    ])
    
    # Aplicar la matriz A * X a los objetos del mundo
    casa_trans = np.dot(A, casa_base)
    cuadrado_trans = np.dot(A, cuadrado_base)
    
    # Calcular el determinante exacto
    det = np.linalg.det(A)
    
    # Actualizar gráficos
    linea_transformada.set_data(casa_trans[0, :], casa_trans[1, :])
    poligono_transformado.set_xy(cuadrado_trans.T)
    
    # Estado de la pantalla según el determinante
    if np.isclose(det, 0.0, atol=1e-2):
        estado = "COLAPSO (Área = 0.0)\n¡El mapa se aplastó a 1D!"
        color_box = "lightcoral"
    else:
        estado = f"Área resultante: {abs(det):.2f}"
        color_box = "lightgreen" if det > 0 else "khaki"
        
    texto_det.set_text(f"Matriz A:\n[{A[0,0]:.1f}  {A[0,1]:.1f}]\n[{A[1,0]:.1f}  {A[1,1]:.1f}]\n\nDeterminante = {det:.2f}\n{estado}")
    texto_det.set_backgroundcolor(color_box)
    
    fig.canvas.draw_idle()

# Conectar deslizadores a la función de actualización
slider_a.on_changed(actualizar)
slider_b.on_changed(actualizar)
slider_c.on_changed(actualizar)
slider_d.on_changed(actualizar)

# Ejecutar primera vista
actualizar(None)
ax.legend(loc='upper right')
plt.show()