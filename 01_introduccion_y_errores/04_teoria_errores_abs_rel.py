# Función para calcular teoría de errores según las fuentes [3-5]

def calcular_errores(valor_obtenido, valor_real):
    # Error Absoluto (EA): Diferencia en magnitud [3]
    ea = abs(valor_obtenido - valor_real)
    
    # Error Relativo (ER): Dimensiona el error según el contexto [3, 4]
    er = ea / valor_real
    
    # Error Relativo Porcentual (ERP): Expresa el error en porcentaje [4]
    erp = er * 100
    
    return ea, er, erp

# Ejemplo práctico basado en el libro (Saldo bancario) [3, 4]
v_real = 100.00
v_obtenido = 90.00

ea, er, erp = calcular_errores(v_obtenido, v_real)

print(f"--- Análisis de Errores ---")
print(f"Valor Real: {v_real} | Valor Obtenido: {v_obtenido}")
print(f"Error Absoluto (EA): {ea}")
print(f"Error Relativo (ER): {er}")
print(f"Error Relativo Porcentual (ERP): {erp}%")