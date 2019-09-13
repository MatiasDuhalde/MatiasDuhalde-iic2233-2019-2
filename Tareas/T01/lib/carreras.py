from abc import ABC, abstractmethod
from random import randint, choice

import lib.parametros as pm
# CHECK PARAMETERS IN PARAMETROS.PY
# THEY MUST BE USED IN HERE (CHECK randints)


class Vehiculo(ABC):
    """
    Vehicle modeling class. 
    
    Inherited by more specific subclasses (type of vehicle):
     - Automovil
     - Troncomovil
     - Bicicleta
     - Motocicleta 
    
    Attributes:
     - Base:
        * chasis
        * carrocería
        * ruedas
     - Specific
        * motor (Automovil, Motocicleta)
        * zapatillas (Troncomovil, Bicicleta)

    """
    @abstractmethod
    def __init__(self, nombre, dueño, chasis, carrocería, ruedas, peso):
        """Arguments are ordered according to pilotos.csv original data."""
        self.nombre = nombre
        self.dueño = dueño
        self.chasis = chasis
        self.carrocería = carrocería
        self.ruedas = ruedas
        self.peso = peso


class Automovil(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis, carrocería, ruedas, motor, peso):
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso)
        self.motor = motor


class Motocicleta(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis, carrocería, ruedas, motor, peso):
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso)
        self.motor = motor


class Troncomovil(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis, carrocería, ruedas, zapatillas, peso):
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso)
        self.zapatillas = zapatillas


class Bicicleta(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis, carrocería, ruedas, zapatillas, peso):
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso)
        self.zapatillas = zapatillas



class Pista(ABC):
    """
    Track modeling class.
    
    Inherited by more specific subclasses (type of track):
     - PistaHelada
     - PistaRocosa
     - PistaSuprema

    """
    @abstractmethod
    def __init__(self):
        pass


class PistaHelada(Pista):

    def __init__(self):
        super().__init__()


class PistaRocosa(Pista):

    def __init__(self):
        super().__init__()
        

class PistaSuprema(Pista):

    def __init__(self):
        super().__init__()


class Piloto:
    """
    Pilot class.
    Possible teams:
     - Tareo
     - Hibrido
     - Docencio
    
    Pilots must have one team (and only one).
    """

    def __init__(self, nombre, equipo, dinero=None, personalidad=None, contextura=None, 
    equilibrio=None, experiencia=None, vehículos=[], new_pilot=False):
        """
        Pilot characteristics:
         - Nombre: nombre (saved in pilotos.csv)
         - Equipo: equipo (saved in pilotos.csv)
         - Dinero: dinero (saved in pilotos.csv) ****
         - Personalidad: personalidad (saved in pilotos.csv, bound to team except Hibrido)
         - Contextura: contextura (saved in pilotos.csv, range bound to team)
         - Equilibrio: equilibrio (saved in pilotos.csv, range bound to team)
         - Experiencia: experiencia (saved in pilotos.csv) ****
         - Vehicle list: vehicles (saved in vehículos.csv) ****
         . new_pilot: defines if pilot was just created of loaded
        Note: **** means this should be a property

        If a new pilot is created it should only receive a name and a team.
        New pilots start with dinero = 0, experiencia = 0, vehículos = []
        """
        self.nombre = nombre
        self.equipo = equipo

        if new_pilot: 
            DEF_ARGS = pm.EQUIPOS[self.equipo.upper()]
            self.dinero = 0
            self.personalidad = choice(DEF_ARGS['PERSONALIDAD'])
            self.contextura = randint(DEF_ARGS['CONTEXTURA']['MIN'], DEF_ARGS['CONTEXTURA']['MAX']) 
            self.equilibrio = randint(DEF_ARGS['EQUILIBRIO']['MIN'], DEF_ARGS['EQUILIBRIO']['MAX'])
            self.experiencia = 0
            self.vehículos = []
        else: 
            self.dinero = dinero
            self.personalidad = personalidad
            self.contextura = contextura
            self.equilibrio = equilibrio
            self.experiencia = experiencia
            self.vehículos = vehículos