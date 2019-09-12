import os
from lib.carreras import Automovil, Motocicleta, Troncomovil, Bicicleta
from lib.carreras import Tareo, Hibrido, Docencio


def clear():
    """Clears console lines."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_vehiculos(name):
    """Returns a list containing vehicle objects, that belong to name."""
    tipos_vehiculo = {"automóvil" : Automovil,
    "motocicleta" : Motocicleta,
    "troncomóvil" : Troncomovil,
    "bicicleta" : Bicicleta}

    lista_vehiculos = []
    with open(os.path.join('databases', 'vehículos.csv'), 'r', 
    encoding='utf-8') as vehiculos:
        vehiculos.readline()
        for line in vehiculos:
            if name in line:
                line = line.rstrip().split(",")
                # Line looks like: [Nombre, Dueño, Categoría, Chasis, 
                # Carrocería, Ruedas, Motor o Zapatillas, Peso]
                tipo = line.pop(2)
                lista_vehiculos.append(tipos_vehiculo[tipo](*line))
    return vehiculos


def get_piloto(name):
    """
    Returns a pilot object from a name, given it exists in pilotos.csv.
    Returns None otherwise.
    """
    teams_pilotos = {"Tareos" : Tareo, 
    "Hibrido" : Hibrido, 
    "Docencios" : Docencio}

    with open(os.path.join('databases', 'pilotos.csv'), 'r', 
    encoding='utf-8') as pilotos:
        pilotos.readline()
        for line in pilotos:
            if name in line:
                line = line.rstrip().split(",")
                # Line looks like: [Nombre, Dinero, Personalidad, 
                # Contextura, Equilibrio, Experiencia, Equipo]
                vehiculos = get_vehiculos(name)

                team = line.pop()
                piloto = teams_pilotos[team](*line, vehiculos)
                if name == piloto.nombre:
                    return piloto
    return None