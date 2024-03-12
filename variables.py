# Definición de variables primitivas
numero_entero = 10
numero_flotante = 3.14159
cadena = "Hola Mundo!"
booleano = True

# Concatenación de variables
resultado_concatenacion = str(numero_entero) + " " + str(numero_flotante) + " " + cadena + " " + str(booleano)

# Límites de tipos de datos
# Enteros: [-9223372036854775808, 9223372036854775807]
# Flotantes: [±1.7976931348623157e+308, ±2.2250738585072014e-308]

# Suma de los primeros n números pares
numero_pares = 0
for i in range(1, numero_entero + 1):
  if i % 2 == 0:
    numero_pares += i

# Impresión de resultados
print("Variable tipo entero:", numero_entero)
print("Variable tipo flotante:", numero_flotante)
print("Variable tipo cadena:", cadena)
print("Variable tipo booleano:", booleano)
print("Resultado concatenación:", resultado_concatenacion)
print("Suma de los primeros", numero_entero, "números pares:", numero_pares)
