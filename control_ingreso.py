presentes = []

while True:
    operacion = input("¿(E)ntrada o (S)alida o (T)erminar?: ")
    operacion = operacion[0].upper()
    
    if operacion in ["E", "S"]:
        persona = input("Nombre: ")
        if operacion == "E":
            presentes.append(persona)
        else:
            if persona in presentes:
                presentes.remove(persona)
            else:
                print(persona, "no está en el Campus")
    elif operacion == "T":
        break
    else:
        print("Opción inválida")
    print(presentes)
