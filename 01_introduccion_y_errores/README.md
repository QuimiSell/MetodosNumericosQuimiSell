# Módulo 1: Introducción, Conversión de Bases y Teoría de Errores

Este módulo aborda los fundamentos computacionales del cálculo numérico: representación de datos en sistemas de numeración digital, precisión finita de punto flotante, propagación de errores y aproximación de funciones continuas mediante series de potencias (Taylor y Maclaurin).

---

## 🎯 Objetivos de Aprendizaje

1. Comprender la representación interna de números en base decimal, binaria, octal y hexadecimal.
2. Analizar el impacto del redondeo y el truncamiento en la aritmética de punto flotante bajo el estándar IEEE 754.
3. Cuantificar el Error Absoluto ($E_A$), Error Relativo ($E_R$) y Error Porcentual ($E_P$).
4. Implementar aproximaciones analíticas y numéricas mediante Series de Taylor y Maclaurin con evaluación del residuo.

---

## 📐 Fundamento Teórico

### 1. Definición Formal de Errores

Dado un valor real exacto $V_{\text{real}}$ y un valor numérico aproximado $V_{\text{aprox}}$:

- **Error Absoluto ($E_A$):**
  $$E_A = |V_{\text{real}} - V_{\text{aprox}}|$$

- **Error Relativo ($E_R$):**
  $$E_R = \frac{|V_{\text{real}} - V_{\text{aprox}}|}{|V_{\text{real}}|} \quad (V_{\text{real}} \neq 0)$$

- **Error Relativo Porcentual ($E_P$):**
  $$E_P = E_R \times 100\%$$

### 2. Teorema de Taylor y Serie de Maclaurin

Cualquier función infinitamente diferenciable $f(x)$ alrededor de un punto $x_0$ se aproxima por:
$$f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(x_0)}{n!} (x - x_0)^n = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \dots$$

Cuando $x_0 = 0$, la serie se denomina **Serie de Maclaurin**.

---

## 📂 Contenido del Módulo

| Archivo | Archivo Original | Descripción / Tema |
| :--- | :--- | :--- |
| `01_convertidor_bases_entero.py` | `ConvertidorNum1.py` | Conversión interactiva de enteros entre bases 10, 2, 8 y 16 usando funciones nativas. |
| `02_convertidor_bases_cadenas.py` | `ConvertidorNum2.py` | Decodificación de cadenas binarias, octales y hexadecimales a números enteros. |
| `03_error_redondeo_precision.py` | `Error1.py` | Demostración de discrepancias por precisión finita en operaciones flotantes. |
| `04_teoria_errores_abs_rel.py` | `Error2.py` | Funciones para cálculo sistemático de error absoluto, relativo y porcentual. |
| `05_maclaurin_coseno.py` | `SerieMaclaurin4-1.py` | Aproximación polinómica de $\cos(x)$ alrededor de $x=0$ con SymPy y Matplotlib. |
| `06_taylor_logaritmo.py` | `Taylolnx4-2.py` | Serie de Taylor para la función logaritmo natural $\ln(x)$ y análisis de convergencia. |
| `07_maclaurin_exponencial.py` | `Maclaurine4-3.py` | Expansión en serie de Maclaurin para la función exponencial $e^x$. |
| `08_taylor_euler_complejo.py` | `Taylorei4-4.py` | Aproximación de la fórmula de Euler $e^{ix} = \cos(x) + i\sin(x)$ en el plano complejo. |

---

## 🚀 Instrucciones de Ejecución y Estudio

Cada script es independiente y se puede ejecutar directamente en consola o abrir en tu editor de código preferido (VS Code, Jupyter, Spyder) para inspeccionar los comentarios y el desarrollo matemático paso a paso:

```bash
python 05_maclaurin_coseno.py
```
