"""
Suma de los primeros n enteros
"""

# Entradas
# n: Cuántos enteros sumar
n = int(input("¿Cuántos enteros quieres sumar? n = "))

# Proceso
# Sumar empezando con 1 e incrementando hasta llegar a "n"
entero = 1
suma = 0
while entero <= n:
    suma += entero
    entero += 1

# Salidas
# suma
print("La suma es", suma)
