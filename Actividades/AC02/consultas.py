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
    # Completar
    pass
