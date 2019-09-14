import os
import lib.parametros as pm
from math import floor, ceil
import lib.parametros as pm

# -----------------------------------------------------------------------------
#                                AUX FUNCTIONS 
# -----------------------------------------------------------------------------

def clear():
    """Clears console lines."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_vehiculos(name, tipos_vehiculo):
    """Returns a list containing vehicle objects, that belong to name."""

    lista_vehiculos = []
    headers, vehiculos = read_csv(pm.PATHS["VEHICULOS"])
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
            vehiculo = tipos_vehiculo[tipo](**kwargs)
            if vehiculo.dueño == name:
                lista_vehiculos.append(vehiculo)
    return lista_vehiculos


def get_piloto(name, tipos_vehiculo, objeto, player=True):
    """
    Returns a pilot object from a name, given it exists in pilotos.csv.
    Returns None otherwise.
    """
    if player:
        headers , pilotos = read_csv(pm.PATHS["PILOTOS"])
    else:
        headers , pilotos = read_csv(pm.PATHS["CONTRINCANTES"])
    # headers = [Nombre, Dinero, Personalidad, Contextura, Equilibrio, 
    # Experiencia, Equipo] // ORDER MIGHT CHANGE
    for line in pilotos:
        if name in line:
            line = line.rstrip().split(",")
            
            vehículos = get_vehiculos(name, tipos_vehiculo)
            kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
            kwargs.update({"vehículos" : vehículos})
            
            piloto = objeto(**kwargs)
            if name == piloto.nombre:
                return piloto
    return None

def get_contrincantes(names, tipos_vehiculo, Contrincante):
    """
    Receives a list containing names of contrincantes (obtained from pistas).
    Returns a list of Contrincantes objects.
    """
    lista_contrincantes = []
    for name in names:
        lista_contrincantes.append(get_piloto(name, tipos_vehiculo, 
        Contrincante, player=False))
    return lista_contrincantes

def get_pistas(tipos_pista, tipos_vehiculo, Contrincante):
    """Returns a list of the track objects stored in pilotos.csv."""
    lista_pistas = []
    headers, pistas = read_csv(pm.PATHS["PISTAS"])
    for line in pistas:
        line = line.rstrip().split(",")
        
        kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
        kwargs["número_vueltas"] = kwargs.pop("númerovueltas")
        kwargs["largo_pista"] = kwargs.pop("largopista")

        tipo_pista = kwargs.pop("tipo")
        if tipo_pista == "pista hielo":
            kwargs.pop("rocas")
        if tipo_pista == "pista rocosa":
            kwargs.pop("hielo")
        contrincantes = kwargs.pop("contrincantes").split(";")
        kwargs["contrincantes"] = get_contrincantes(contrincantes, 
        tipos_vehiculo, Contrincante)
        lista_pistas.append(tipos_pista[tipo_pista](**kwargs))
    return lista_pistas

def read_csv(path):
    """
    Returns headers (list) and a list containing every line (without '\n')
    """
    lineas = []
    with open(os.path.join(*path), 'r', encoding='utf-8') as archivo:
        headers = archivo.readline().rstrip().split(",")
        for line in archivo:
            lineas.append(line.rstrip())
    return headers, lineas


def guardar_partida(piloto, tipos_vehiculo):
        """
        Overwrites pilotos.csv, vehículos.csv
        A same pilot with the same name can't have 2 entries in pilotos.csv
        Previous lines describing the pilot are deleted and replaced with new
        ones based on the pilot's attributes.
        """
        # Delete old line(s) in pilotos.csv
        lines = []
        headers, pilotos = read_csv(pm.PATHS["PILOTOS"])
        lines.append(",".join(headers) + '\n')
        for line in pilotos:
            lines.append(line + '\n')
            line = line.rstrip().split(",")
            kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
            if kwargs["nombre"] == piloto.nombre:
                lines.pop()
        
        # Rewrite pilotos.csv
        save_data = {"Nombre" : piloto.nombre, 
        "Dinero" : piloto.dinero, "Personalidad" : piloto.personalidad, 
        "Contextura" : piloto.contextura, "Equilibrio" : piloto.equilibrio, 
        "Experiencia" : piloto.experiencia, "Equipo" : piloto.equipo}
        order = {headers[index] : index for index in range(len(headers))}
        save_data = [str(save_data[key]) for key in sorted(save_data, key=order.get)]
        save_data = ",".join(save_data) + '\n'
        lines.append(save_data)

        with open(os.path.join(*pm.PATHS["PILOTOS"]), 'w', 
        encoding='utf-8') as pilotos:
            for line in lines:
                pilotos.write(line)
        
        # Delete old line(s) in vehículos.csv
        lines = []
        headers, vehiculos = read_csv(pm.PATHS["VEHICULOS"])
        lines.append(",".join(headers) + '\n')
        for line in vehiculos:
            lines.append(line + '\n')
            line = line.rstrip().split(",")
            kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
            if kwargs["dueño"] == piloto.nombre:
                lines.pop()
        
        # Rewrite vehículos.csv
        for vehiculo in piloto.vehículos:
            save_data = {"Nombre" : vehiculo.nombre, "Dueño" : vehiculo.dueño, 
            "Categoría" : list(tipos_vehiculo.keys())[list(
                tipos_vehiculo.values()).index(type(vehiculo))], 
            "Chasis" : vehiculo.chasis, "Carrocería" : vehiculo.carrocería, 
            "Ruedas" : vehiculo.ruedas, "Motor o Zapatillas" : vehiculo.motor 
            if type(vehiculo) in list(tipos_vehiculo.values())[:2] else vehiculo.zapatillas, 
            "Peso" : vehiculo.peso}
            
            order = {headers[index] : index for index in range(len(headers))}
            save_data = [str(save_data[key]) for key in sorted(save_data, key=order.get)]
            save_data = ",".join(save_data) + '\n'
            lines.append(save_data)
        with open(os.path.join(*pm.PATHS["VEHICULOS"]), 'w', 
        encoding='utf-8') as vehiculos:
            for line in lines:
                vehiculos.write(line)


# -----------------------------------------------------------------------------
#                                FORMULAS
# -----------------------------------------------------------------------------

# Cálculo de velocidad

def hipotermia(piloto, vehiculo, pista, numero_vuelta):
    # DE DONDE SALE numero_vuelta ?
    if not hasattr(pista, 'hielo'):
        return 0
    return min(0, numero_vuelta * (piloto.contextura - pista.hielo))

def dificultad_control(piloto, vehiculo):
    # Se asume que troncomóvil tiene 2 ruedas, aún cuando en los picapiedras 
    # tiene claramente 2 :thinking:
    if type(vehiculo).__name__ in ["Automovil", "Troncomovil"]:
        return 0
    efecto = 1 if piloto.personalidad == 'osado' else pm.EQUILIBRIO_PRECAVIDO
    return min(0, piloto.equilibrio * efecto - floor(pm.PESO_MEDIO/vehiculo.peso))

def velocidad_recomendada(piloto, vehiculo, pista):
    velocidad_base = vehiculo.motor if hasattr(vehiculo, 'motor') else vehiculo.zapatillas
    hielo_pista = pista.hielo if hasattr(pista, 'hielo') else 0
    rocas_pista = pista.hielo if hasattr(pista, 'hielo') else 0
    return velocidad_base + (vehiculo.ruedas - hielo_pista) + \
        (vehiculo.carrocería - rocas_pista) + \
        (piloto.experiencia - pista.dificultad)

def velocidad_intencional(piloto, vehiculo, pista):
    if piloto.personalidad == 'osado':
        efecto = pm.EFECTO_OSADO 
    elif piloto.personalidad == 'precavido':
        efecto = pm.EFECTO_PRECAVIDO
    return efecto * velocidad_recomendada(piloto, vehiculo, pista)

def velocidad_real(piloto, vehiculo, pista, numero_vuelta):
    return max(pm.VELOCIDAD_MINIMA, velocidad_intencional(piloto, vehiculo, pista) + \
        dificultad_control(piloto, vehiculo) + \
        hipotermia(piloto, vehiculo, pista, numero_vuelta))
    
# Sucesos durante la carrera

def calcular_daño(vehiculo, pista):
    # Esta fórmula no tiene mucho sentido
    if not hasattr(pista, 'rocas'):
        return max(0, vehiculo.carrocería - pista.rocas)
    return 0

def tiempo_pits(vehiculo):
    return pm.TIEMPO_MINIMO_PITS + (vehiculo.chasis - vehiculo.chasis_actual) \
    * pm.VELOCIDAD_PITS

def dinero_vuelta(pista, numero_vuelta):
    return numero_vuelta * pista.dificultad

def probabilidad_accidentes(piloto, vehiculo, pista, numero_vuelta):
    vel_real = velocidad_real(piloto, vehiculo, pista, numero_vuelta)
    vel_recomendada = velocidad_recomendada(piloto, vehiculo, pista)
    return (vel_real - vel_recomendada)/vel_recomendada + \
    floor((vehiculo.chasis - vehiculo.chasis_actual)/vehiculo.chasis)

def tiempo_vuelta(piloto, vehiculo, pista, numero_vuelta):
    return ceil(pista.largo_pista/velocidad_real(piloto, vehiculo, pista, \
    numero_vuelta))

# Ganador carrera

def dinero_ganador(pista):
    rocas = pista.rocas if hasattr(pista, 'rocas') else 0
    hielo = pista.hielo if hasattr(pista, 'hielo') else 0
    return pista.número_vueltas * (pista.dificultad + hielo + rocas)

def ventaja_con_ultimo(primero, ultimo):
    return primero - ultimo

def experiencia_recibida(piloto, pista, primero, ultimo):
    if piloto.personalidad == 'precavido':
        bonus = pm.BONIFICACION_PRECAVIDO 
    elif piloto.personalidad == 'osado':
        bonus = pm.BONIFICACION_OSADO
    return (ventaja_con_ultimo(primero, ultimo) + pista.dificultad) * bonus