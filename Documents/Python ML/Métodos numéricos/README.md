# Métodos Numéricos - QuimiSell

Repositorio de **métodos numéricos** aplicados a problemas químicos y de ingeniería. Incluye implementaciones en Python de algoritmos numéricos fundamentales con ejemplos prácticos.

## Contenido del Proyecto

### 📁 Estructura

```
├── 01_Modulo_1/          # Métodos de Taylor y Maclaurin
│   ├── Error1.py
│   ├── Error2.py
│   ├── SerieMaclaurin4-1.py
│   ├── Taylolnx4-2.py
│   └── Taylorei4-4.py
│
├── 02_Modulo_2/          # Interpolación y Regresión Lineal
│   ├── lagrange1-2.py
│   ├── Naville1-3.py
│   ├── Naville31-4.py
│   ├── Newton1-1.py
│   ├── 8RegresiónLineal1.py
│   ├── 8RegresionLineal2.py
│   └── 8RegresionLineal3.py (Conexión con IA: Perceptrón)
│
├── utils/                # Funciones auxiliares
│   └── __init__.py
│
├── ConvertidorNum.py     # Convertidor de números
├── Trductor.py          # Traductor numérico
├── requirements.txt      # Dependencias
└── README.md           # Este archivo
```

## 🎯 Módulos Principales

### Módulo 1: Series de Taylor y Maclaurin
- Cálculo de aproximaciones usando series de potencias
- Análisis de errores
- Aplicaciones en funciones logarítmicas y exponenciales

### Módulo 2: Interpolación y Regresión
- Interpolación de Lagrange
- Método de Neville
- Newton - Diferencias divididas
- **Regresión Lineal**: conexión entre estadística clásica y redes neuronales (perceptrón)

## 📦 Requisitos

```bash
pip install -r requirements.txt
```

Las librerías necesarias son:
- `numpy` - Cálculos numéricos
- `matplotlib` - Visualización
- `scipy` - Análisis científico

## 🚀 Uso

### Ejecutar un ejemplo de regresión lineal

```bash
python 02_Modulo_2/8RegresionLineal3.py
```

Esto mostrará:
- La salida de un perceptrón lineal
- Gráfica comparativa: datos reales vs predicción de la neurona

### Ejecutar convertidor

```bash
python ConvertidorNum.py
```

## 🧠 Conexión con IA

El archivo `8RegresionLineal3.py` demuestra cómo los coeficientes de una regresión lineal se pueden interpretar como **peso** y **bias** en una neurona lineal:

```
y = x · w + b
```

Donde:
- `w` (peso) ≈ pendiente de la regresión
- `b` (bias) ≈ ordenada en el origen

Esto es fundamental para entender las redes neuronales simples.

## 📝 Autor

**QuimiSell** - Proyectos de Química e Ingeniería

## 📄 Licencia

Este proyecto es educativo y de código abierto.
