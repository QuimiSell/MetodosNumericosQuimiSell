# Módulo 2: Interpolación Polinomial y Modelos de Regresión

Este módulo profundiza en el ajuste de curvas y la estimación de valores intermedios a partir de conjuntos discretos de datos experimentales. Se estudian tanto métodos de **interpolación exacta** (donde la curva pasa estrictamente por los puntos muestra) como técnicas de **regresión por mínimos cuadrados** (para modelar tendencias con ruido experimental).

---

## 🎯 Objetivos de Aprendizaje

1. Dominar los métodos clásicos de interpolación polinomial: Diferencias Divididas de Newton, Polinomios de Lagrange y el Algoritmo Recursivo de Neville.
2. Explorar interpolación en dos dimensiones (2D) para superficies térmicas o de concentración.
3. Evaluar el fenómeno de Runge y comparar el desempeño de diferentes esquemas de interpolación.
4. Ajustar datos de laboratorio mediante Regresión Lineal Múltiple (Mínimos Cuadrados Ordinarios - MCO) y Regresiones No Lineales (modelos polinomiales, exponenciales e hiperbólicos).

---

## 📐 Fundamento Teórico

### 1. Polinomio de Interpolación de Newton
Construido mediante diferencias divididas recursivas:
$$P_n(x) = f[x_0] + \sum_{k=1}^{n} f[x_0, x_1, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j)$$
donde las diferencias divididas se calculan como:
$$f[x_i, x_{i+1}, \dots, x_{i+k}] = \frac{f[x_{i+1}, \dots, x_{i+k}] - f[x_i, \dots, x_{i+k-1}]}{x_{i+k} - x_i}$$

### 2. Forma de Lagrange
$$P_n(x) = \sum_{i=0}^{n} y_i L_i(x), \quad L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

### 3. Algoritmo de Neville
Estructura en tabla triangular recursiva que permite calcular el valor interpolado $P(x)$ de manera eficiente sin expandir explícitamente los coeficientes del polinomio:
$$P_{i, j}(x) = \frac{(x - x_j) P_{i, j-1}(x) - (x - x_i) P_{i+1, j}(x)}{x_i - x_j}$$

### 4. Regresión por Mínimos Cuadrados (MCO)
Para un sistema $Y \approx X \beta$, los estimadores de los parámetros óptimos que minimizan la suma de errores cuadráticos $\sum (y_i - \hat{y}_i)^2$ se obtienen resolviendo las ecuaciones normales:
$$\beta = (X^T X)^{-1} X^T Y$$

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Tema |
| :--- | :--- | :--- |
| `01_interpolacion_vecino_cercano.py` | `Nearest_1.py` | Interpolación por el vecino más cercano (Nearest Neighbor) con SciPy y Matplotlib. |
| `02_interpolacion_newton_dif_divididas.py` | `Newton1-1.py` | Tabla de diferencias divididas y evaluación polinómica de Newton. |
| `03_interpolacion_lagrange.py` | `lagrange1-2.py` | Construcción de polinomios base de Lagrange y graficación continua. |
| `04_algoritmo_neville.py` | `Naville1-3.py` | Implementación pura paso a paso del algoritmo recursivo de Neville. |
| `05_neville_vs_scipy.py` | `Naville31-4.py` | Comparativa de precisión entre Neville manual y módulos optimizados de SciPy. |
| `06_interpolacion_2d_superficie.py` | `2dinterpolacio.py` | Interpolación bidimensional en mallas regulares con mapas de contorno 3D (`scipy.interpolate`). |
| `07_comparativa_6_metodos_interpolacion.py` | `6metodos.py` | Análisis comparativo de 6 esquemas (lineal, cuadrático, cúbico, spline, baricéntrico, etc.). |
| `08_regresion_lineal_multiple_mco.py` | `RegresMulLineal.py` | Regresión lineal múltiple multivariable mediante solución matricial directa de MCO. |
| `09_regresion_no_lineal_multiple.py` | `RegresMultNoLineal.py` | Ajuste de modelos no lineales multivariables con superficies de regresión. |
| `10_regresion_no_lineal_exp_hiperbolica.py` | `RegresionNoLinealExpHip.py` | Linealización y ajuste de modelos exponenciales e hiperbólicos en cinética química. |

---

## 🚀 Instrucciones de Ejecución

```bash
python 07_comparativa_6_metodos_interpolacion.py
```
O usando el menú general:
```bash
python quimisell_runner.py
```
