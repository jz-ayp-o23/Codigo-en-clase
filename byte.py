# Dar formato a un byte

# Declaraciones
LONG_BYTE = 8

# Entradas
binario = input("Introduzca los dígitos binarios: ")

# Proceso
# ¿Cuántos bits tenemos?
long_binario = len(binario)
# ¿Cuántos necesitamos?
long_faltan = LONG_BYTE - long_binario
# Agregarlos
binario = "0" * long_faltan + binario
# Separar en dos cuartetos
cuarteto_1 = binario[:4]
cuarteto_2 = binario[4:]
# Y unirlos con un espacio en medio
byte = cuarteto_1 + " " + cuarteto_2

# Salidas
print("Byte:", byte)
