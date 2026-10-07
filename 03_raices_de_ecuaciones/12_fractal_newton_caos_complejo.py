import numpy as np
import matplotlib.pyplot as plt

def fractal_newton():
    res = 500
    x = np.linspace(-2, 2, res)
    y = np.linspace(-2, 2, res)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Iteraciones de Newton
    for _ in range(25):
        Z -= (Z**3 - 1) / (3 * np.where(np.abs(Z) == 0, 1e-12, Z)**2)

    # 3 Raíces cúbicas de 1
    r1 = 1.0 + 0j
    r2 = -0.5 + (np.sqrt(3)/2)*1j
    r3 = -0.5 - (np.sqrt(3)/2)*1j

    img = np.zeros(Z.shape)
    img[np.abs(Z - r1) < 0.2] = 1
    img[np.abs(Z - r2) < 0.2] = 2
    img[np.abs(Z - r3) < 0.2] = 3

    plt.figure(figsize=(8, 8))
    plt.imshow(img, extent=[-2, 2, -2, 2], cmap="plasma", origin="lower")
    plt.title("Sensibilidad a Condiciones Iniciales: Fractal de Newton ($z^3 - 1 = 0$)")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

fractal_newton()