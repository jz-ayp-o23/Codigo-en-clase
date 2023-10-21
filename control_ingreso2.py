
# Declaraciones
alumnos = {
    752069: "Sarah", 750722: "Pris", 750786: "Dani",
    751097: "Clara", 731756: "Giovanni", 752830: "David",
}

en_campus = []

while True:
    expediente = int(input("Expediente (0 para salir): "))
    if expediente != 0:
        if expediente in alumnos:
            if expediente in en_campus:
                # Salida
                en_campus.remove(expediente)
            else:
                # Entrada
                en_campus.append(expediente)
        else:
            # Expediente desconocido, dar de alta
            print("Expediente desconocido")
            nombre = input("Nombre del alumno (ENTER para cancelar): ")
            if nombre != "":
                alumnos[expediente] = nombre
                print("Alumnos:", alumnos)
                en_campus.append(expediente)
        for i in en_campus:
            print(alumnos[i], end=", ")
        print()
    else:
        break
