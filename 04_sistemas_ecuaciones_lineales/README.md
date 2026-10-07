# Módulo 4: Sistemas de Ecuaciones Lineales y Álgebra Matricial

Este módulo se enfoca en la resolución de sistemas de ecuaciones algebraicas lineales del tipo $A x = b$, fundamentales para modelar balances de materia y energía en estado estacionario, redes de flujo, columnas de destilación fraccionada y circuitos. Se exploran tanto **métodos directos** (exactos salvo error de redondeo) como **métodos iterativos** (para matrices grandes y dispersas).

---

## 🎯 Objetivos de Aprendizaje

1. Implementar la Eliminación Gaussiana con pivoteo parcial para evitar inestabilidades numéricas.
2. Resolver balances de masa multivariables: sistema de 5 reactores CSTR interconectados y columnas de fraccionamiento de hidrocarburos.
3. Descomponer matrices en factores $L$ (triangular inferior) y $U$ (triangular superior) para sistemas con múltiples vectores de carga $b$.
4. Balancear reacciones químicas homogéneas utilizando álgebra simbólica y forma escalonada reducida por filas (RREF).
5. Dominar los métodos iterativos: Jacobi, Gauss-Seidel y Sobre-Relajación Sucesiva (SOR).

---

## 📐 Fundamento Teórico

### 1. Eliminación Gaussiana y Pivoteo Parcial
Para evitar división por números cercanos a cero o acumulación de errores de redondeo, en cada paso $k$ se busca la fila con el coeficiente pivote de mayor magnitud absoluta:
$$\text{fila\_max} = \arg\max_{i \geq k} |a_{ik}|$$
y se intercambia con la fila actual antes de proceder a la eliminación hacia adelante:
$$m_{ik} = \frac{a_{ik}}{a_{kk}}, \quad F_i \leftarrow F_i - m_{ik} F_k$$

### 2. Descomposición LU ($A = LU$)
Permite resolver $A x = b$ en dos pasos rápidos de sustitución:
1. $L y = b$ (Sustitución hacia adelante)
2. $U x = y$ (Sustitución hacia atrás)

### 3. Métodos Iterativos (Jacobi vs Gauss-Seidel vs SOR)
Dado $a_{ii} x_i^{(k+1)} = b_i - \sum_{j < i} a_{ij} x_j - \sum_{j > i} a_{ij} x_j$:

- **Jacobi:** Utiliza únicamente los valores del paso anterior $x^{(k)}$.
- **Gauss-Seidel:** Utiliza de inmediato los valores recién calculados en la misma iteración $x^{(k+1)}$.
- **SOR (Successive Over-Relaxation):** Pondera la solución con un parámetro de aceleración $\omega \in (1, 2)$:
  $$x_i^{(k+1)} = (1 - \omega) x_i^{(k)} + \omega x_i^{\text{GS}}$$

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Caso Práctico |
| :--- | :--- | :--- |
| `01_eliminacion_gauss_pivoteo_5tanques.py` | `1Gaus.py` | **Caso real:** Balance de masa de soluto en 5 tanques continuos (CSTR) acoplados. Eliminación Gaussiana con pivoteo parcial y analogía Feynman. |
| `02_gauss_jordan_destilacion_4hidrocarburos.py` | `2GausJordan.py` | **Caso real:** Balance de materia en columna de destilación fraccionada de 4 hidrocarburos. Matriz identidad completa. |
| `03_sistemas_homogeneos_balanceo_quimico_sympy.py` | `3RectyHomo.py` | **Caso real:** Balanceo estequiométrico exacto de reacciones químicas usando álgebra simbólica SymPy y RREF. |
| `04_descomposicion_lu_doolittle.py` | `5DesLU.py` | Factorización matricial $A = LU$ y resolución con `scipy.linalg`. |
| `05_matriz_inversa_multiplicacion.py` | `6Invemultiplicacion.py` | Cálculo de matriz inversa e impacto del número de condición. |
| `06_inversa_sistemas_multiples.py` | `7InversaMultimultiplicacion.py` | Solución eficiente de sistemas simultáneos con matrices de entrada múltiples. |
| `07_regla_de_cramer.py` | `8Crammer.py` | Solución analítica mediante determinantes de Cramer (evaluación de costo computacional $O(n!)$ vs $O(n^3)$). |
| `08_metodo_iterativo_jacobi.py` | `9Jacobi.py` | Algoritmo iterativo de Jacobi con verificación de diagonal dominante. |
| `09_metodo_iterativo_gauss_seidel.py` | `10GausSeidiel.py` | Algoritmo iterativo de Gauss-Seidel con actualización inmediata in-situ. |
| `10_sobre_relajacion_sucesiva_sor.py` | `11Sor.py` | Aceleración de convergencia con factor de relajación óptimo $\omega$. |

---

## 🚀 Instrucciones de Ejecución

```bash
python 01_eliminacion_gauss_pivoteo_5tanques.py
```
O usando el menú interactivo:
```bash
python quimisell_runner.py
```
