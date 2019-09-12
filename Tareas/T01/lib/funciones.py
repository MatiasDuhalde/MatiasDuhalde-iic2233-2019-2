import os

def clear():
    """Clears console lines."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# HEADERS MIGHT CHANGE POSITIONS, USE KWARGS

def get_vehiculos(name, tipos_vehiculo):
    """Returns a list containing vehicle objects, that belong to name."""

    lista_vehiculos = []
    with open(os.path.join('databases', 'vehículos.csv'), 'r', 
    encoding='utf-8') as vehiculos:
        
        # HEADERS/COLUMNS MIGHT CHANGE ORDER!
        headers = vehiculos.readline().rstrip().split(",")
        # headers = [Nombre, Dueño, Categoría, Chasis, Carrocería, Ruedas, 
        # Motor o Zapatillas, Peso] // ORDER MIGHT CHANGE
        for line in vehiculos:
            if name in line:
                line = line.rstrip().split(",")
                kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
                tipo = kwargs.pop("categoría")
                if tipo in ["troncomóvil", "bicicleta"]:
                    power = "zapatillas"
                elif tipo in ["automóvil", "motocicleta"]:
                    power = "motor"
                kwargs[power] = kwargs.pop("motor o zapatillas")
                lista_vehiculos.append(tipos_vehiculo[tipo](**kwargs))
    return lista_vehiculos


def get_piloto(name, lista_equipos, tipos_vehiculo):
    """
    Returns a pilot object from a name, given it exists in pilotos.csv.
    Returns None otherwise.
    """

    with open(os.path.join('databases', 'pilotos.csv'), 'r', 
    encoding='utf-8') as pilotos:
        
        # HEADERS/COLUMNS MIGHT CHANGE ORDER!
        headers = pilotos.readline().rstrip().split(",")
        # headers = [Nombre, Dinero, Personalidad, Contextura, Equilibrio, 
        # Experiencia, Equipo] // ORDER MIGHT CHANGE
        for line in pilotos:
            if name in line:
                line = line.rstrip().split(",")
                vehículos = get_vehiculos(name, tipos_vehiculo)
                kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
                kwargs.update({"vehículos" : vehículos})
                team = kwargs.pop("equipo")
                piloto = lista_equipos[team](**kwargs)
                if name == piloto.nombre:
                    return piloto
    return None