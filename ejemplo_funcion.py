def suma(a, b):
    "Suma dos números"
    resultado = a + b
    return resultado

def sumar_varios(numeros):
    suma = 0
    for x in numeros:
        suma += x
    return suma

def saludar():
    print("Hola.")
    return 1


c = suma(2, 5)
print(c)

sumandos = [1, 2, 4, 7, 99]
print(sumar_varios(sumandos))

saludar()
print(saludar())
