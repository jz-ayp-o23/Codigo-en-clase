"""
Factores de un número
"""

# Entrada
numero = int(input("¿De qué número quiere sus factores: "))

# Proceso
# Probar cada número a ver si es divisor (exacto)
factores = []
for factor in range(1, numero+1):
    if numero % factor == 0:
        factores.append(factor)

salida = [str(i) for i in factores]
salida = "\n> ".join(salida)

# Salida
print("Los factores son:\n> ", salida)
