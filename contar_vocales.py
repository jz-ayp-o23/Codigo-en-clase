"""
Contar vocales en una frase.
"""

# Definiciones
VOCALES = "aeiouáéíóúü"

# Entradas
#   La frase
frase = input("Introduzca una frase: ")

# Proceso
#   Revisar cada letra de la frase
#     Si es una vocal
#        Llevo una vocal más
cantidad_vocales = 0
for letra in frase:
    if letra.lower() in VOCALES:
        cantidad_vocales += 1

# Salidas
#   Cantidad de vocales
print("La frase tiene", cantidad_vocales, "vocales.")
