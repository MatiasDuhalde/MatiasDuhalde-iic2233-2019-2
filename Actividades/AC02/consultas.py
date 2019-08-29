from cargar_datos import DICT_PISOS
"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    print("-"*79)

    print(f"Alumnos restantes: {len(alumnos)}")
    total = 0
    for i in DICT_PISOS.values():
        total += len(ayudantes[i])
        print(f"Ayudantes {i}: {len(ayudantes[i])}")
    print(f"Ayudantes restantes: {total}")
    
    print("-"*79)


def stock_comida(alumnos):
    dict_comidas = {}
    for alumno in alumnos:
        for comida in alumno.habilidades:
            if not comida in dict_comidas.keys():
                dict_comidas[comida] = 1
            else:
                dict_comidas[comida] += 1
    comidas_totales = [(comida, dict_comidas[comida]) for comida in dict_comidas.keys()]
    return comidas_totales