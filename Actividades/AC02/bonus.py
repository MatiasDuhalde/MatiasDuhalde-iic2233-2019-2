"""
Aquí debes completar las funciones del Bonus
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""
import os

TECH_KEYS = {
    'Piso -1': ['red', 'yellow', 'blue', 'purple', 'blue', 'purple', 'green', 'red', 'orange'],
    'Piso -2': ['black', 'pink', 'blue', 'green', 'green', 'orange', 'grey', 'red', 'yellow'],
    'Piso -3': ['purple', 'grey', 'orange', 'red', 'purple', 'pink', 'purple', 'grey',
                'orange', 'red', 'purple', 'pink'],
    'Piso -4': ['blue', 'red', 'white', 'green', 'blue', 'white', 'lightblue', 'white',
                'yellow', 'blue', 'red', 'yellow', 'purple', 'yellow', 'red', 'orange',
                'black', 'white', 'grey']
}


def cargar_llaves(ruta_archivo_llaves):
    print(f"Cargando datos de {ruta_archivo_llaves}...")
    keys = {}
    with open(ruta_archivo_llaves) as archivo_llaves:
        for linea in archivo_llaves:
            linea = linea.strip().split(";")
            keys[linea[0]] = linea[1].split(",")
    return keys

def desbloquear_pisos(llaves, piso):
    print(f"Desbloqueando {piso}...")
    if TECH_KEYS[piso] == llaves[piso]:
        print(f"{piso} desbloqueado!")
        return True
    print(f"No se ha podido desbloquear el {piso} :(")
    return False
