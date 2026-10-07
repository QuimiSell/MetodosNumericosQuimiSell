import numpy as np

def newton_con_pasos(coefs, x0=1.0, tol=1e-6, max_iter=30):
    """Encuentra una raíz imprimiendo el paso a paso de Newton."""
    n = len(coefs) - 1
    d_coefs = [coefs[i] * (n - i) for i in range(n)]
    x = complex(x0)
    
    for i in range(max_iter):
        # Evaluar polinomio y derivada con Horner
        fx = 0
        for c in coefs: fx = fx * x + c
        dfx = 0
        for c in d_coefs: dfx = dfx * x + c
        
        dx = fx / dfx
        x -= dx
        if abs(dx) < tol:
            return x
    return x

def ruffini_con_pasos(coefs, raiz):
    """Ejecuta y muestra la división sintética paso a paso."""
    nuevo_coefs = [coefs[0]]
    print(f"\n  [División Sintética por (x - {raiz.real:.4f})]")
    print(f"  Coeficientes iniciales: {coefs}")
    
    for i in range(1, len(coefs) - 1):
        valor = coefs[i] + nuevo_coefs[-1] * raiz
        nuevo_coefs.append(valor)
        
    print(f"  Nuevo polinomio deflactado: {[round(c.real, 4) for c in nuevo_coefs]}")
    return nuevo_coefs

def deflacion_completa(coefs):
    polinomio = list(coefs)
    grado_total = len(coefs) - 1
    raices = []

    print("=" * 60)
    print(f"RESOLVIENDO POLINOMIO DE GRADO {grado_total}")
    print("=" * 60)

    for paso in range(grado_total):
        print(f"\n>>> Paso {paso + 1}: Buscando Raíz {paso + 1}")
        r = newton_con_pasos(polinomio, x0=1.0 + 0.5j)
        raices.append(r)
        print(f"  Raíz encontrada: {r.real:+.4f} {r.imag:+.4f}j")
        
        if len(polinomio) > 2:
            polinomio = ruffini_con_pasos(polinomio, r)

    print("\n" + "=" * 60)
    print("RESUMEN FINAL DE RAÍCES")
    print("=" * 60)
    for idx, r in enumerate(raices, 1):
        print(f"Raíz {idx}: {r.real:+.6f} {r.imag:+.6f}j")

# Polinomio de prueba: x^3 - 4x^2 + x + 6 = 0 (Raíces exactas: -1, 2, 3)
coefs_ejemplo = [1.0, -4.0, 1.0, 6.0]
deflacion_completa(coefs_ejemplo)