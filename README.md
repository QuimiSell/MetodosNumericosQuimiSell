# 🧪 Métodos Numéricos en Python | QuimiSell

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Array%20Computing-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-Scientific%20Computing-8CAAE6.svg?logo=scipy&logoColor=white)](https://scipy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Data%20Visualization-11557C.svg)](https://matplotlib.org/)
[![SymPy](https://img.shields.io/badge/SymPy-Symbolic%20Math-3B5526.svg)](https://www.sympy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![QuimiSell](https://img.shields.io/badge/Canal-QuimiSell-red.svg?logo=youtube&logoColor=white)](https://github.com/QuimiSell)

Bienvenido al repositorio oficial del curso **Métodos Numéricos en Python** desarrollado por **QuimiSell**. Este proyecto reúne más de 60 algoritmos numéricos implementados desde cero y con librerías científicas de vanguardia, acompañados de analogías pedagógicas (estilo Feynman), análisis de convergencia y aplicaciones directas a problemas reales de **física, termodinámica e ingeniería química**.

---

## 👥 ¿A quién está dirigido este repositorio?

- **🎓 Estudiantes:** Para comprender la derivación matemática paso a paso, visualizar geométricamente cómo convergen los algoritmos y aprender a traducir modelos matemáticos a código limpio en Python.
- **👨‍🏫 Docentes:** Como material didáctico estructurado y listo para usar en clase, con ejemplos de balances de materia, cinética química, difusión de calor y visualizaciones en Matplotlib.
- **🔬 Investigadores e Ingenieros:** Como caja de herramientas de algoritmos robustos (Wegstein para bucles de reciclo, SOR para EDPs elípticas, Crank-Nicolson para difusión, RK4 para reactores continuos CSTR en cascada).

---

## 🌟 Lanzador Interactivo QuimiSell (`quimisell_runner.py`)

Para facilitar el estudio y la enseñanza, el repositorio incluye un **lanzador interactivo en terminal** que permite explorar y ejecutar cualquiera de los 60 programas sin necesidad de escribir rutas largas:

```bash
python quimisell_runner.py
```

```text
================================================================================
  ██████╗ ██╗   ██╗██╗███╗   ███╗██╗███████╗███████╗██╗     ██╗     
 ██╔═══██╗██║   ██║██║████╗ ████║██║██╔════╝██╔════╝██║     ██║     
 ██║   ██║██║   ██║██║██╔████╔██║██║███████╗█████╗  ██║     ██║     
 ██║▄▄ ██║██║   ██║██║██║╚██╔╝██║██║╚════██║██╔══╝  ██║     ██║     
 ╚██████╔╝╚██████╔╝██║██║ ╚═╝ ██║██║███████║███████╗███████╗███████╗
  ╚══▀▀═╝  ╚═════╝ ╚═╝╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚══════╝
     --- MÉTODOS NUMÉRICOS APLICADOS A LA CIENCIA E INGENIERÍA ---
================================================================================
```

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

## 🔬 Casos de Estudio Destacados

### 🧪 1. Reactores Químicos CSTR en Cascada (Módulo 6)
Modelado de dos tanques de mezcla completa en serie con reacción de primer orden mediante el método de **Euler Modificado (Predictor-Corrector)**:
$$\frac{dC_1}{dt} = \frac{F}{V_1}(C_{\text{in}} - C_1) - k C_1, \qquad \frac{dC_2}{dt} = \frac{F}{V_2}(C_1 - C_2) - k C_2$$

### 🔥 2. Conducción de Calor Bidimensional con SOR (Módulo 6)
Resolución de la ecuación elíptica de Laplace $\nabla^2 T = 0$ sobre una placa con condiciones de Dirichlet, implementando la **Analogía Feynman** (cada nodo en equilibrio es el promedio de sus 4 vecinos) y aceleración por Sobre-Relajación Sucesiva (SOR):
$$T_{i,j}^{(k+1)} = (1 - \omega) T_{i,j}^{(k)} + \frac{\omega}{4} \left( T_{i+1, j}^{(k)} + T_{i-1, j}^{(k+1)} + T_{i, j+1}^{(k)} + T_{i, j-1}^{(k+1)} \right)$$

### 🌀 3. Caos y Fractal de Newton en el Plano Complejo (Módulo 3)
Estudio de la sensibilidad extrema a las condiciones iniciales del método de Newton-Raphson aplicado a raíces cúbicas complejas ($z^3 - 1 = 0$), graficando las fronteras fractales de atracción.

---

## 📁 Estructura del Proyecto

```text
MetodosNumericosQuimiSell/
├── .gitignore                                      # Exclusión de entornos virtuales y cachés
├── LICENSE                                         # Licencia MIT de código abierto
├── README.md                                       # Documentación principal del repositorio
├── requirements.txt                                # Dependencias de Python (NumPy, SciPy, Matplotlib, SymPy)
├── quimisell_runner.py                             # Menú interactivo CLI para ejecutar cualquier método
│
├── 01_introduccion_y_errores/                     # Módulo 1 (8 scripts + README)
├── 02_interpolacion_y_regresion/                  # Módulo 2 (10 scripts + README)
├── 03_raices_de_ecuaciones/                       # Módulo 3 (12 scripts + README)
├── 04_sistemas_ecuaciones_lineales/               # Módulo 4 (10 scripts + README)
├── 05_sistemas_no_lineales_y_calculo/             # Módulo 5 (12 scripts + README)
├── 06_ecuaciones_diferenciales/                   # Módulo 6 (8 scripts + README)
└── utils/                                         # Módulo de funciones auxiliares
```

---

## 🤝 Contribuciones y Comunidad

Las contribuciones, sugerencias y mejoras son bienvenidas. Si encuentras un error o deseas proponer un nuevo caso práctico de ingeniería:
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
