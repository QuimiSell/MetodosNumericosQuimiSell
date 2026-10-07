# Definimos el número decimal que queremos convertir
numero = 30

# Python utiliza funciones integradas para las conversiones:
# bin() para binario, oct() para octal y hex() para hexadecimal.

print(numero, 'en base 10 es', numero)
print(numero, 'en base 2 es', bin(numero))   # Resultado empieza con '0b'
print(numero, 'en base 8 es', oct(numero))   # Resultado empieza con '0o'
print(numero, 'en base 16 es', hex(numero))  # Resultado empieza con '0x'

# Cadenas representativas en distintas bases
binario = "0b11110"  # o simplemente "11110"
octal = "0o36"       # o simplemente "36"
hexadecimal = "0x1e" # o simplemente "1e"

# Conversión a base 10 indicando la base de origen
dec_desde_bin = int(binario, 2)
dec_desde_oct = int(octal, 8)
dec_desde_hex = int(hexadecimal, 16)

print(binario, 'en base 10 es', dec_desde_bin)
print(octal, 'en base 10 es', dec_desde_oct)
print(hexadecimal, 'en base 10 es', dec_desde_hex)