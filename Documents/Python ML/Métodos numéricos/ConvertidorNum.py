# Definimos el número decimal que queremos convertir
numero = 30

# Python utiliza funciones integradas para las conversiones:
# bin() para binario, oct() para octal y hex() para hexadecimal.

print(numero, 'en base 10 es', numero)
print(numero, 'en base 2 es', bin(numero))   # Resultado empieza con '0b'
print(numero, 'en base 8 es', oct(numero))   # Resultado empieza con '0o'
print(numero, 'en base 16 es', hex(numero))  # Resultado empieza con '0x'