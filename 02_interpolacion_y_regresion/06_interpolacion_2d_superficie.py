import numpy as np
from scipy import interpolate  # Seguimos usando el módulo de interpolación
import matplotlib.pyplot as plt
from matplotlib import cm

# 1. DEFINICIÓN DE COORDENADAS (Datos tabulados)
x = np.array([300.0, 350.0, 400.0, 450.0, 500.0])  # Temperatura (5 elementos)
y = np.array([100.0, 150.0, 200.0, 250.0])         # Presión (4 elementos)

# 2. MATRIZ DE PROPIEDADES (Z)
# Importante: RegularGridInterpolator requiere que las dimensiones de Z 
# coincidan exactamente con el orden de los ejes pasados (Presión, Temperatura).
z = np.array([[3073.3, 3174.7, 3277.5, 3381.7, 3487.6],
              [3072.1, 3173.8, 3276.7, 3381.1, 3487.0],
              [3070.9, 3172.8, 3275.9, 3380.4, 3486.5],
              [3069.7, 3171.9, 3275.2, 3379.8, 3486.0]])

# 3. INTERPOLACIÓN CON EL MÉTODO MODERNO
# Pasamos los ejes en una tupla (y, x) para que coincida con la estructura de filas/columnas de 'z'.
# 'method='cubic'' reemplaza al antiguo 'kind='cubic''.
# bounds_error=False permite evaluar puntos en los límites sin que el programa colapse.
f = interpolate.RegularGridInterpolator((y, x), z, method='cubic', bounds_error=False)

# 4. EVALUACIÓN DE UN PUNTO FUERA DE LA TABLA
# El nuevo interpolador no recibe argumentos separados f(x, y).
# Recibe una lista o arreglo de coordenadas en el orden de los ejes declarados: [Presión, Temperatura]
punto_objetivo = np.array([[190.0, 420.0]])  
zi = f(punto_objetivo)

print(f"Entalpía interpolada en (420K, 190kPa): {zi[0]} kJ/Kg")

# 5. PREPARACIÓN DE LA MALLA VISUAL 3D
X, Y = np.meshgrid(x, y)

# 6. CONFIGURACIÓN Y RENDERIZADO DEL ESPACIO TRIDIMENSIONAL
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.view_init(10, 35)

# Dibujamos la superficie con los datos base
surf = ax.plot_surface(X, Y, z, cmap=cm.coolwarm, antialiased=True)

# Configuraciones visuales e ingeniería
ax.set_xlabel('Temperatura (K)')
ax.set_ylabel('Presión (kPa)')
ax.set_zlabel('Entalpía (kJ/Kg)')
plt.title('Superficie de Entalpía (SciPy Moderno)')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()