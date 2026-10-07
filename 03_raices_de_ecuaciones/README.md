# Módulo 3: Raíces de Ecuaciones No Lineales (1D)

Este módulo cubre los algoritmos numéricos para encontrar las soluciones $x^*$ tales que $f(x^*) = 0$. Se clasifican en **métodos cerrados** (que garantizan convergencia acotando el intervalo donde hay cambio de signo) y **métodos abiertos** (más veloces, de orden cuadrático o cúbico, aunque sujetos a divergencia o ciclos).

---

## 🎯 Objetivos de Aprendizaje

1. Aplicar el Teorema del Valor Intermedio (Bolzano) para garantizar la existencia de raíces.
2. Comparar la velocidad y robustez de los métodos cerrados (Bisección y Regla Falsa).
3. Implementar métodos abiertos: Newton-Raphson estándar, optimizado con SciPy, y modificaciones para raíces de multiplicidad $m > 1$.
4. Comprender métodos acelerados y de orden superior: Halley (orden 3), Punto Fijo, Secante y el Algoritmo de Wegstein (clave en simuladores de procesos químicos como ASPEN y HYSYS).
5. Encontrar raíces complejas y polinomios mediante el Método de Müller y la Deflación de Horner.
6. Visualizar el comportamiento caótico y la sensibilidad a condiciones iniciales mediante el **Fractal de Newton**.

---

## 📐 Tabla Comparativa de Métodos

| Método | Tipo | Orden de Convergencia | Requiere Derivadas | Garantía de Convergencia |
| :--- | :--- | :--- | :--- | :--- |
| **Bisección** | Cerrado | Lineal ($r = 1$) | No | **Sí** (si $f(a)f(b) < 0$) |
| **Regla Falsa (Regula Falsi)** | Cerrado | Superlineal / Lineal | No | **Sí** (si $f(a)f(b) < 0$) |
| **Punto Fijo** | Abierto | Lineal ($r = 1$) | No | Condicional ($|g'(x)| < 1$) |
| **Secante** | Abierto | Superlineal ($r \approx 1.618$) | No | No garantizada |
| **Wegstein** | Abierto | Acelerado | No | Alta en bucles de reciclaje |
| **Newton-Raphson** | Abierto | Cuadrático ($r = 2$) | Sí ($f'(x)$) | Local (si $x_0 \approx x^*$) |
| **Halley** | Abierto | Cúbico ($r = 3$) | Sí ($f'(x), f''(x)$) | Local |
| **Müller** | Abierto | Cuadrático ($r \approx 1.84$) | No (parábolas) | Local (encuentra complejas) |

---

## 🔬 El Algoritmo de Wegstein en Ingeniería Química
El método de Wegstein es el algoritmo por excelencia empleado para converger bucles de reciclo en balances de materia y energía de plantas químicas:
$$x_{k+1} = q x_k + (1 - q) g(x_k), \quad q = \frac{s}{s - 1}, \quad s = \frac{g(x_k) - g(x_{k-1})}{x_k - x_{k-1}}$$
Acelera drásticamente la convergencia de iteraciones de punto fijo donde la pendiente $|g'(x)|$ está cerca de 1.

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Tema |
| :--- | :--- | :--- |
| `01_metodo_biseccion.py` | `1biseccion,py` | Bisección pura paso a paso con gráfica de convergencia y verificación de Bolzano. |
| `02_regla_falsa_regula_falsi.py` | `2Reglafalsa.py` | Método de la Regla Falsa (interpolación lineal entre extremos). |
| `03_newton_raphson_clasico.py` | `3NewtonRapson.py` | Implementación estándar de Newton-Raphson con trazado de tangentes. |
| `04_newton_raphson_scipy_opt.py` | `4NewRapopt.py` | Uso de `scipy.optimize.newton` para cálculos de producción de alta precisión. |
| `05_newton_raphson_raices_multiples.py` | `5NewRapsonMod.py` | Algoritmo modificado para raíces múltiples ($f(x)/f'(x)$). |
| `06_metodo_halley_convergencia_cubica.py` | `6halley.py` | Método de Halley con aproximación hiperbólica y convergencia cúbica. |
| `07_iteracion_punto_fijo.py` | `7puntofijo.py` | Iteración funcional $x = g(x)$ y verificación de $|g'(x)| < 1$. |
| `08_metodo_secante.py` | `8Secante.py` | Aproximación de la derivada mediante diferencias finitas sin cálculo analítico. |
| `09_aceleracion_wegstein.py` | `9Weigner.py` | Algoritmo de Wegstein para aceleración de convergencia en ingeniería de procesos. |
| `10_metodo_muller_raices_complejas.py` | `10Muller.py` | Ajuste parabólico a tres puntos para obtener raíces reales y números complejos. |
| `11_deflacion_polinomial_horner.py` | `11deflaPol.py` | Extracción iterativa de raíces polinómicas y división sintética (Horner). |
| `12_fractal_newton_caos_complejo.py` | `12FractalNew.py` | Renderizado del fractal de cuencas de atracción de Newton en el plano complejo para $z^3 - 1 = 0$. |

---

## 🚀 Instrucciones de Ejecución y Estudio

Cada script es independiente y se puede abrir y ejecutar directamente en Python para analizar los comentarios pedagógicos, los criterios de parada y las gráficas:

```bash
python 01_metodo_biseccion.py
python 12_fractal_newton_caos_complejo.py
```
