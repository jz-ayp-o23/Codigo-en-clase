"""
Calcular el día siguiente
"""

def dia_siguiente(dia, mes, anho):
    "Suma 1 día a la fecha"
    dia += 1
    if dia > dia_del_mes(mes, anho):
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anho += 1
    return (dia, mes, anho)


def dia_del_mes(mes, anho=1):
    "Regresa la cantidad de días en el mes"
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias = 31
    elif mes in (4, 6, 9, 11):
        dias = 30
    else:
        if es_bisiesto(anho):
            dias = 29
        else:
            dias = 28
    return dias


def es_bisiesto(anho):
    "Determina si el año es bisiesto"
    if anho % 400 == 0 or anho % 4 == 0 and anho % 100 != 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto

casos_prueba = [
    (1, 1, 2023),
    (31, 1, 2023),
    (1, 2, 2023),
    (28, 2, 2023),
    (28, 2, 2024),
    (29, 2, 2024),
    (4, 4, 2023),
    (31, 12, 2023),
]
for dia, mes, anho in casos_prueba:
    print("Actual:   ", dia, mes, anho, end="  --->   ")
    print("Siguiente:",dia_siguiente(dia, mes, anho))
