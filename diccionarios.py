from pprint import pprint

alumnos = {751097: "Clara", 731756: "Giovanni", 752830: "David"}

# Acceder a los datos de la lista
alguien = alumnos[731756]
print(alguien)

alumnos2 = {
    751097: {"Nombre": "Clara", "calificacion": 97},
    731756: {"Nombre": "Giovanni", "calificacion": 98},
    752830: {"Nombre": "David", "calificacion": 99},
}
print()
pprint(alumnos2)

alguien = alumnos2[752830]
print()
print(alguien)

print()
print(alumnos)
print("Clara" in alumnos)
print(751097 in alumnos)