"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si no lo necesitas
"""
from collections import namedtuple, deque

"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    Alumno = namedtuple("Alumno", ["nombre", "habilidades"])
    alumnos = []
    with open(ruta_archivo_alumnos, "r", encoding="UTF-8") as file_alumnos:
        for linea in file_alumnos:
            linea = linea.rstrip()
            nom, habils = linea.split(";")
            alumnos.append(Alumno(nom, set(habils.split(","))))
    return alumnos



def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    Ayudante = namedtuple("Ayudante", ["nombre", "rango", "debilidades", "comiendo"])
    piso1 = deque()
    piso2 = deque()
    piso3 = deque()
    piso4 = deque()
    ayudantes = {"Piso -4": piso4, "Piso -3": piso3, "Piso -2": piso2, 
    "Piso -1": piso1}
    with open(ruta_archivo_ayudantes, "r", encoding="UTF-8") as file_ayudantes:
        for linea in file_ayudantes:
            linea = linea.rstrip()
            nom, r, debils = linea.split(";")
            ay = Ayudante(nom, r, set(debils.split(",")), [])
            ayudantes[DICT_PISOS[ay.rango]].append(ay)
    return ayudantes
