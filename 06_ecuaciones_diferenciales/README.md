# Módulo 6: Ecuaciones Diferenciales Ordinarias (EDOs) y Parciales (EDPs)

Este módulo representa la cúspide del curso, conectando los métodos numéricos con problemas dinámicos y espaciales del mundo real en **física e ingeniería química**. Se estudian problemas de valor inicial (IVP), problemas de valor en la frontera (BVP), y ecuaciones en derivadas parciales (EDPs) elípticas y parabólicas.

---

## 🎯 Objetivos de Aprendizaje

1. Implementar integradores numéricos para EDOs: Euler estándar, Euler Modificado (Heun, Predictor-Corrector) y Runge-Kutta de 4to Orden (RK4).
2. Simular la dinámica transitoria real de un sistema de **reactores agitados continuos (CSTR) en cascada** con reacción química de primer orden.
3. Resolver problemas de valor en la frontera (BVP 1D) mediante Diferencias Finitas (conducción térmica en aletas y varillas).
4. Discretizar y resolver la **Ecuación de Laplace 2D** en estado estacionario térmico con condiciones Dirichlet y aceleración SOR.
5. Modelar la difusión transitoria del calor en 1D comparando los métodos FTCS (explícito), BTCS (implícito) y **Crank-Nicolson** (incondicionalmente estable, $O(\Delta t^2, \Delta x^2)$).
6. Explorar visualmente el condicionamiento geométrico de determinantes con sliders interactivos de Matplotlib.

---

## 🔬 Caso de Estudio: Reactores CSTR en Serie

El script `02_reactores_cstr_cascada_euler_modificado.py` modela el balance de masa no estacionario para dos tanques CSTR con reacción $A \rightarrow B$:

$$\begin{aligned}
\frac{dC_1}{dt} &= \frac{F}{V_1}(C_{\text{in}} - C_1) - k C_1 \\
\frac{dC_2}{dt} &= \frac{F}{V_2}(C_1 - C_2) - k C_2
\end{aligned}$$

Donde:
- $F$: Flujo volumétrico ($10 \text{ L/min}$)
- $V_1, V_2$: Volúmenes de los reactores ($100 \text{ L}$)
- $C_{\text{in}}$: Concentración de alimentación ($2.0 \text{ mol/L}$)
- $k$: Constante cinética de primer orden ($0.05 \text{ min}^{-1}$)

El método de **Euler Modificado (Predictor-Corrector)** resuelve vectorialmente este sistema mostrando el retardo en la respuesta y la aproximación al estado estacionario final.

---

## 📐 Ecuaciones en Derivadas Parciales (EDPs)

### 1. Ecuación de Laplace 2D ($\nabla^2 T = 0$)
Discretizada en una placa metálica con condiciones de frontera Dirichlet:
$$T_{i, j}^{(k+1)} = (1 - \omega) T_{i,j}^{(k)} + \frac{\omega}{4} \left( T_{i+1, j}^{(k)} + T_{i-1, j}^{(k+1)} + T_{i, j+1}^{(k)} + T_{i, j-1}^{(k+1)} \right)$$
La analogía Feynman demuestra que cada punto en equilibrio térmico adopta exactamente el promedio de sus cuatro vecinos ortogonales.

### 2. Ecuación de Difusión 1D y Esquema de Crank-Nicolson
$$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2}$$
El esquema de Crank-Nicolson promedia las diferencias espaciales en los instantes $n$ y $n+1$, generando un sistema tridiagonal incondicionalmente estable:
$$-\frac{r}{2} T_{i-1}^{n+1} + (1 + r) T_i^{n+1} - \frac{r}{2} T_{i+1}^{n+1} = \frac{r}{2} T_{i-1}^n + (1 - r) T_i^n + \frac{r}{2} T_{i+1}^n \quad \left(r = \alpha \frac{\Delta t}{\Delta x^2}\right)$$

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Modelo Físico |
| :--- | :--- | :--- |
| `01_metodo_euler_estandar_vs_modificado.py` | `24Euler.py` | Comparación de convergencia y estabilidad: Euler hacia adelante vs Heun (Predictor-Corrector). |
| `02_reactores_cstr_cascada_euler_modificado.py` | `25EDOReactores.py` | **Ingeniería Química:** Modelado de 2 CSTRs en serie con reacción cinética de 1er orden. |
| `03_runge_kutta_4to_orden_rk4.py` | `26R4.py` | Integrador RK4 para sistemas vectoriales de ecuaciones diferenciales. |
| `04_diferencias_finitas_bvp_1d.py` | `27DifFinintas.py` | Problemas con valores en la frontera (BVPs) resueltos mediante matrices tridiagonales. |
| `05_discretizacion_edp_conceptos.py` | `28EDP.py` | Introducción conceptual y computacional a la discretización de EDPs. |
| `06_laplace_2d_sor_placa_termica.py` | `29Laplace2d.py` | Distribución de temperaturas 2D en estado estacionario con aceleración SOR. |
| `07_difusion_1d_crank_nicolson_ftcs_btcs.py` | `30Nicholson.py` | Comparativa completa de difusión térmica: FTCS (explícito), BTCS (implícito) y Crank-Nicolson. |
| `08_determinante_interactivo_sliders.py` | `Determinante.py` | Visualización interactiva con sliders en tiempo real del determinante y condicionamiento matricial. |

---

## 🚀 Instrucciones de Ejecución y Estudio

Cada script es independiente y se puede abrir y ejecutar directamente para estudiar los modelos dinámicos, la analogía Feynman de Laplace y las simulaciones de ingeniería química:

```bash
python 02_reactores_cstr_cascada_euler_modificado.py
python 06_laplace_2d_sor_placa_termica.py
```
