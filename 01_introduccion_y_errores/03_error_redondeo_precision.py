# Programa 1.2: Error de redondeo en Python
# Este código demuestra que la precisión finita genera discrepancias

a = 4.1
b = 0.2
resultado = a - b

print(f"Operación: {a} - {b}")
print(f"Resultado en Python: {resultado}")

# Salida esperada: 3.8999999999999995
# Explicación: Se observa un error de redondeo al no ser capaz de 
# almacenar el valor exacto de la resta en la memoria [2].