
"""
Contar vocales en una frase (versión con función).
"""

def contar_vocales(frase):
    "Cuenta las vocales en frase"
    # Definiciones
    VOCALES = "aeiouáéíóúü"
    # Proceso
    #   Revisar cada letra de la frase
    #     Si es una vocal
    #        Llevo una vocal más
    cantidad_vocales = 0
    for letra in frase:
        if letra.lower() in VOCALES:
            cantidad_vocales += 1
    return cantidad_vocales



perro = input("Frase: ")
gato = contar_vocales(perro)
print("La frase tiene", gato, "vocales")
