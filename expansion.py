print("Introduzca los números que quiere sumar, separados por un espacio:")
numeros = input()

numeros = numeros.split()

numeros_verdaderos = []
for perro in numeros:
    gato = float(perro)
    numeros_verdaderos.append(gato)

suma = sum(numeros_verdaderos)

print(perro, gato)
print(numeros)
print(numeros_verdaderos)
print(suma)