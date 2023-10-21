# Declaraciones
MULTA_BAJA = 1_000
MULTA_ALTA = 50_000
LIMITE_BAJO = 80
LIMITE_ALTO = 120

# Entradas
velocidad = float(input("Velocidad: "))

# Proceso
# Si la velocidad excede al límite, aplicar la multa
if velocidad > LIMITE_ALTO:
    multa = MULTA_ALTA
elif velocidad > LIMITE_BAJO:
    multa = MULTA_BAJA
else:
    multa = 0

# Salidas
print("La multa es de:", multa)