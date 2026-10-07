# Módulo 5: Sistemas No Lineales, Diferenciación e Integración Numérica

Este módulo aborda dos áreas cruciales del análisis numérico avanzado:
1. **Sistemas de Ecuaciones No Lineales Multivariables:** Métodos iterativos (Jacobi, Gauss-Seidel) y el método multidimensional de Newton-Raphson basado en la matriz Jacobiana $J(x)$.
2. **Cálculo Numérico Diferencial e Integral:** Esquemas de diferencias finitas hacia adelante, atrás y centradas, extrapolación de Richardson, sumas de Riemann, regla del trapecio, reglas de Simpson (1/3 y 3/8), Cuadratura de Gauss, Integración de Romberg, e integración de funciones impropias o con singularidades.

---

## 🎯 Objetivos de Aprendizaje

1. Resolver sistemas no lineales $F(X) = 0$ utilizando Newton-Raphson Multivariable con inversión analítica o numérica del Jacobiano.
2. Calcular derivadas numéricas de primer y segundo orden evaluando el error de truncamiento $O(h)$ vs $O(h^2)$.
3. Acelerar la precisión del cálculo diferencial mediante la Extrapolación de Richardson.
4. Integrar numéricamente funciones continuas y datos discretos de laboratorio contaminados con ruido experimental.
5. Aplicar cuadraturas avanzadas (Gauss-Legendre) y métodos de orden alto (Romberg).
6. Evaluar integrales múltiples (volúmenes) e integrales impropias con límites al infinito o asíntotas.

---

## 📐 Fundamento Teórico

### 1. Newton-Raphson Multivariable
Para un sistema vectorial $F(X) = [f_1(x_1, \dots, x_n), \dots, f_n(x_1, \dots, x_n)]^T = 0$:
$$X_{k+1} = X_k - [J(X_k)]^{-1} F(X_k)$$
donde la matriz Jacobiana está definida por:
$$J_{ij} = \frac{\partial f_i}{\partial x_j}$$

### 2. Diferenciación Numérica Centrada y Richardson
- **Diferencia Centrada ($O(h^2)$):**
  $$f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}$$
- **Extrapolación de Richardson ($O(h^4)$):**
  $$D \approx \frac{4 D(h/2) - D(h)}{3}$$

### 3. Integración Numérica: Reglas de Simpson
- **Simpson 1/3 Compuesto ($n$ par):**
  $$\int_a^b f(x)dx \approx \frac{h}{3} \left[ f(x_0) + 4\sum_{i=1,3,\dots}^{n-1} f(x_i) + 2\sum_{i=2,4,\dots}^{n-2} f(x_i) + f(x_n) \right]$$
- **Simpson 3/8 Compuesto ($n$ múltiplo de 3):**
  $$\int_a^b f(x)dx \approx \frac{3h}{8} \left[ f(x_0) + 3 f(x_1) + 3 f(x_2) + 2 f(x_3) + \dots + f(x_n) \right]$$

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Caso de Estudio |
| :--- | :--- | :--- |
| `01_jacobi_no_lineal_multivariable.py` | `12Jacobi.py` | Extensión del método de Jacobi para sistemas acoplados no lineales. |
| `02_gauss_seidel_multivariable.py` | `13GausSeidielmulti.py` | Gauss-Seidel no lineal con actualización secuencial de variables. |
| `03_newton_raphson_multivariable_jacobiano.py` | `14NewRapsonMultivariables.py` | Algoritmo clásico de Newton-Raphson con cálculo del Jacobiano analítico y numérico. |
| `04_diferenciacion_adelante_atras_centrada.py` | `15Derivada.py` | Fórmulas de diferenciación progresiva, regresiva y centrada con análisis de error $O(h)$ vs $O(h^2)$. |
| `05_extrapolacion_richardson.py` | `16DeriRichard.py` | Aceleración de convergencia en derivadas numéricas mediante Richardson. |
| `06_gradiente_y_derivadas_parciales.py` | `17DerivadaGrad.py` | Cálculo numérico de vectores gradiente $\nabla f$ y superficies multidimensionales. |
| `07_riemann_y_trapecio_flujo_calor.py` | `18RiemTrapecio.py` | **Caso práctico:** Cálculo del flujo de calor acumulado mediante sumas de Riemann y Trapecio compuesto. |
| `08_reglas_simpson_1_3_y_3_8.py` | `19Simpson.py` | Implementación y comparación de las reglas de Simpson 1/3 y Simpson 3/8. |
| `09_comparativa_integracion_datos_ruido.py` | `20Comparativa.py` | Integración de datos experimentales con ruido comparando algoritmos propios vs SciPy. |
| `10_integracion_romberg_y_cuadratura_gauss.py` | `21RombergGaus.py` | Métodos de alta precisión: tabla de Romberg y polinomios de Legendre (Cuadratura de Gauss). |
| `11_integrales_multiples_volumen.py` | `22IntegMult.py` | Integrales dobles y triples para cálculo de áreas, volúmenes y masa total (`scipy.integrate.dblquad`). |
| `12_integrales_impropias_singularidades.py` | `23Impropias.py` | Tratamiento numérico de límites infinitos y singularidades con transformaciones de variable. |

---

## 🚀 Instrucciones de Ejecución

```bash
python 03_newton_raphson_multivariable_jacobiano.py
```
O usando el menú interactivo:
```bash
python quimisell_runner.py
```
