# 🧪 Métodos Numéricos en Python | QuimiSell

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Scientific%20Computing-8CAAE6.svg?logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Visualization-11557C.svg)](https://matplotlib.org/)
[![SymPy](https://img.shields.io/badge/SymPy-Symbolic%20Math-3B5526.svg)](https://www.sympy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![QuimiSell](https://img.shields.io/badge/Canal-QuimiSell-red.svg?logo=youtube&logoColor=white)](https://github.com/QuimiSell)

Repositorio oficial del curso **Métodos Numéricos en Python** de **QuimiSell**. Este proyecto reúne 60 algoritmos numéricos implementados de forma independiente, transparente y pedagógica, con aplicaciones directas a **física, termodinámica e ingeniería química**.

---

## 🎯 Filosofía Didáctica: "El Código es la Explicación"

El propósito central de este repositorio es que **estudiantes, docentes e investigadores puedan abrir cualquier archivo `.py` y comprender inmediatamente el *porqué* matemático y físico de cada línea**:

- **Autocontenidos:** Cada script se puede ejecutar de forma individual sin depender de librerías internas ocultas ni menús que aíslen al usuario del código.
- **Comentarios línea por línea:** Explicaciones detalladas dentro del propio código sobre la justificación de cada paso (criterios de parada, tolerancias, pivoteos, condiciones de frontera).
- **Analogías pedagógicas (estilo Feynman):** Explicaciones conceptuales intuitivas en docstrings (como el porqué del pivoteo parcial o por qué cada nodo en la ecuación de Laplace es el promedio de sus 4 vecinos).
- **Inspección de datos paso a paso:** Impresión formateada de iteraciones en consola y generación de gráficas en Matplotlib para visualizar la convergencia.

---

## 👥 ¿A quién está dirigido este repositorio?

- **🎓 Estudiantes:** Para leer el código fuente, entender cómo se traduce la teoría matemática a estructuras de datos en Python y reproducir ejercicios de clase.
- **👨‍🏫 Docentes:** Como material didáctico modular para proyectar y analizar directamente en el aula, con ejemplos de balances de materia, cinética química, reactores y transferencia de calor.
- **🔬 Investigadores e Ingenieros:** Como referencia transparente de algoritmos numéricos (Wegstein para reciclos, SOR para Laplace 2D, Crank-Nicolson para difusión, Heun/RK4 para reactores CSTR en serie).

---

## 📚 Mapa Curricular de Módulos

| Módulo | Directorio | Temas Principales | Aplicaciones y Casos de Estudio |
| :---: | :--- | :--- | :--- |
| **01** | [`01_introduccion_y_errores`](01_introduccion_y_errores/) | Conversión de bases, precisión de punto flotante, teoría de errores, Series de Taylor y Maclaurin. | Pérdida de significancia flotante, fórmula de Euler compleja. |
| **02** | [`02_interpolacion_y_regresion`](02_interpolacion_y_regresion/) | Polinomios de Newton, Lagrange, Neville, vecino más cercano, regresión MCO lineal y no lineal. | Interpolación 2D de superficies, cinética química hiperbólica y exponencial. |
| **03** | [`03_raices_de_ecuaciones`](03_raices_de_ecuaciones/) | Bisección, Regla Falsa, Newton-Raphson, Halley, Secante, Wegstein, Müller, Deflación de Horner. | Aceleración de reciclaje de procesos (Wegstein), **Fractal de Newton** ($z^3 - 1 = 0$). |
| **04** | [`04_sistemas_ecuaciones_lineales`](04_sistemas_ecuaciones_lineales/) | Eliminación Gaussiana, Gauss-Jordan, Factorización LU, Cramer, Jacobi, Gauss-Seidel, SOR. | **Balance de 5 reactores CSTR interconectados**, destilación de hidrocarburos, balanceo estequiométrico con SymPy. |
| **05** | [`05_sistemas_no_lineales_y_calculo`](05_sistemas_no_lineales_y_calculo/) | Newton multivariable con Jacobiano, derivadas centradas, Richardson, Riemann, Simpson, Romberg, Gauss. | Flujo de calor acumulado, integración de datos ruidosos de laboratorio, integrales impropias. |
| **06** | [`06_ecuaciones_diferenciales`](06_ecuaciones_diferenciales/) | Euler y Euler Modificado, RK4 vectorial, Diferencias Finitas (BVPs), EDP Laplace 2D, Crank-Nicolson. | **Dinámica transitoria de CSTRs en serie**, conducción de calor 2D con SOR, difusión 1D transitoria. |

---

## 🛠️ Instalación y Requisitos

### 1. Clonar el repositorio
```bash
git clone https://github.com/QuimiSell/MetodosNumericosQuimiSell.git
cd MetodosNumericosQuimiSell
```

### 2. Crear y activar un entorno virtual (recomendado)
En Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

En Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar las dependencias científicas
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución de los Scripts

Para estudiar cualquier método, navega a la carpeta correspondiente y ejecuta el archivo `.py` directamente:

```bash
# Ejemplo: Método de Bisección
python 03_raices_de_ecuaciones/01_metodo_biseccion.py

# Ejemplo: Balance de 5 reactores CSTR con Gauss
python 04_sistemas_ecuaciones_lineales/01_eliminacion_gauss_pivoteo_5tanques.py

# Ejemplo: Modelado de Reactores Químicos en Serie
python 06_ecuaciones_diferenciales/02_reactores_cstr_cascada_euler_modificado.py
```

Cada script mostrará la evolución numérica en la consola y desplegará la ventana gráfica de Matplotlib.

---

## 🔬 Casos de Estudio Destacados

### 🧪 1. Reactores Químicos CSTR en Cascada (Módulo 6)
Modelado de dos tanques de mezcla completa en serie con reacción de primer orden mediante el método de **Euler Modificado (Predictor-Corrector)**:
$$\frac{dC_1}{dt} = \frac{F}{V_1}(C_{\text{in}} - C_1) - k C_1, \qquad \frac{dC_2}{dt} = \frac{F}{V_2}(C_1 - C_2) - k C_2$$

### 🔥 2. Conducción de Calor Bidimensional con SOR (Módulo 6)
Resolución de la ecuación elíptica de Laplace $\nabla^2 T = 0$ sobre una placa con condiciones de Dirichlet, implementando la **Analogía Feynman** (cada nodo en equilibrio es el promedio de sus 4 vecinos) y aceleración por Sobre-Relajación Sucesiva (SOR):
$$T_{i,j}^{(k+1)} = (1 - \omega) T_{i,j}^{(k)} + \frac{\omega}{4} \left( T_{i+1, j}^{(k)} + T_{i-1, j}^{(k+1)} + T_{i, j+1}^{(k)} + T_{i, j-1}^{(k+1)} \right)$$

### 🌀 3. Caos y Fractal de Newton en el Plano Complejo (Módulo 3)
Estudio de la sensibilidad extrema a las condiciones iniciales del método de Newton-Raphson aplicado a raíces cúbicas complejas ($z^3 - 1 = 0$), graficando las cuencas fractales de atracción.

---

## 📁 Estructura del Proyecto

```text
MetodosNumericosQuimiSell/
├── .gitignore                                      # Exclusión de entornos virtuales y cachés
├── LICENSE                                         # Licencia MIT de código abierto
├── README.md                                       # Documentación principal del repositorio
├── requirements.txt                                # Dependencias de Python (NumPy, SciPy, Matplotlib, SymPy)
│
├── 01_introduccion_y_errores/                     # Módulo 1: Bases, errores y Taylor (8 scripts + README)
├── 02_interpolacion_y_regresion/                  # Módulo 2: Interpolación y regresión (10 scripts + README)
├── 03_raices_de_ecuaciones/                       # Módulo 3: Raíces no lineales 1D (12 scripts + README)
├── 04_sistemas_ecuaciones_lineales/               # Módulo 4: Matrices y sistemas lineales (10 scripts + README)
├── 05_sistemas_no_lineales_y_calculo/             # Módulo 5: Multivariable, derivadas e integrales (12 scripts + README)
├── 06_ecuaciones_diferenciales/                   # Módulo 6: EDOs, EDPs y reactores (8 scripts + README)
└── utils/                                         # Módulo de funciones auxiliares
```

---

## 🤝 Contribuciones y Comunidad

Las contribuciones, sugerencias y mejoras son bienvenidas:
1. Haz un Fork del repositorio.
2. Crea una rama para tu función (`git checkout -b feature/NuevoMetodo`).
3. Realiza un commit con tus cambios (`git commit -m "Añadido nuevo caso de estudio"`).
4. Envía un Pull Request.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT** - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<p align="center">
  Desarrollado con ❤️ para la comunidad de ciencia e ingeniería por <b>QuimiSell</b>.
</p>
