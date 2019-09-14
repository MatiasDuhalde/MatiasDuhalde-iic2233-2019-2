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
    def __init__(self, nombre, dueño, chasis=None, carrocería=None, 
    ruedas=None, peso=None, DEF_ARGS=None):
        """Arguments are ordered according to pilotos.csv original data."""
        self.nombre = nombre
        self.dueño = dueño
        if DEF_ARGS:
            self.chasis = randint(DEF_ARGS["CHASIS"]["MIN"], DEF_ARGS["CHASIS"]["MAX"])
            self.carrocería = randint(DEF_ARGS["CARROCERIA"]["MIN"], 
            DEF_ARGS["CARROCERIA"]["MAX"])
            self.ruedas = randint(DEF_ARGS["RUEDAS"]["MIN"], DEF_ARGS["RUEDAS"]["MAX"])
            self.peso = randint(DEF_ARGS["PESO"]["MIN"], DEF_ARGS["PESO"]["MAX"])
        else:
            self.chasis = int(chasis)
            self.carrocería = int(carrocería)
            self.ruedas = int(ruedas)
            self.peso = int(peso)

        self.chasis_actual = self.chasis
        self.tiempo_acumulado = 0

    def reset_parameters(self):
        self.chasis_actual = self.chasis
        self.tiempo_acumulado = 0

    def reparar(self):
        self.chasis_actual = self.chasis

    def __str__(self, clase):
        # 15 chars to the left, limit 79
        string = "{:49.44}{:15}".format(self.nombre, clase)
        return string



class Automovil(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis=None, carrocería=None, 
    ruedas=None, motor=None, peso=None, new_car=False):
        if new_car:
            DEF_ARGS = pm.AUTOMOVIL
            self.motor = randint(DEF_ARGS["MOTOR"]["MIN"], DEF_ARGS["MOTOR"]["MAX"])
        else:
            DEF_ARGS = None
            self.motor = int(motor)
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso, DEF_ARGS)
    

    def __str__(self):
        return super().__str__("Automóvil")


class Motocicleta(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis=False, carrocería=False, 
    ruedas=False, motor=False, peso=False, new_car=False):
        if new_car:
            DEF_ARGS = pm.MOTOCICLETA
            self.motor = randint(DEF_ARGS["MOTOR"]["MIN"], DEF_ARGS["MOTOR"]["MAX"])
        else:
            DEF_ARGS = None
            self.motor = int(motor)
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso, DEF_ARGS)

    def __str__(self):
        return super().__str__("Motocicleta")


class Troncomovil(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis=False, carrocería=False, 
    ruedas=False, zapatillas=False, peso=False, new_car=False):
        if new_car:
            DEF_ARGS = pm.TRONCOMOVIL
            self.zapatillas = randint(DEF_ARGS["ZAPATILLAS"]["MIN"], 
            DEF_ARGS["ZAPATILLAS"]["MAX"])
        else:
            DEF_ARGS = None
            self.zapatillas = int(zapatillas)
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso, DEF_ARGS)

    def __str__(self):
        return super().__str__("Troncomóvil")


class Bicicleta(Vehiculo):
    
    def __init__(self, nombre, dueño, chasis=False, carrocería=False, 
    ruedas=False, zapatillas=False, peso=False, new_car=False):
        if new_car:
            DEF_ARGS = pm.BICICLETA
            self.zapatillas = randint(DEF_ARGS["ZAPATILLAS"]["MIN"], 
            DEF_ARGS["ZAPATILLAS"]["MAX"])
        else:
            DEF_ARGS = None
            self.zapatillas = int(zapatillas)
        super().__init__(nombre, dueño, chasis, carrocería, ruedas, peso, DEF_ARGS)

    def __str__(self):
        return super().__str__("Bicicleta")


class Pista(ABC):
    """
    Track modeling class.
    
    Inherited by more specific subclasses (type of track):
     - PistaHelada
     - PistaRocosa
     - PistaSuprema

    """
    @abstractmethod
    def __init__(self, nombre, dificultad, número_vueltas, contrincantes, largo_pista):
        self.nombre = nombre
        self.dificultad = int(dificultad)
        self.número_vueltas = int(número_vueltas)
        self.contrincantes = contrincantes
        self.largo_pista = int(largo_pista)

    @abstractmethod
    def __str__(self, tipo):
        # 15 chars to the left, limit 79
        string = "{:38.33} {:13.10} {}".format(self.nombre, 
        tipo, self.número_vueltas)
        return string


class PistaHelada(Pista):

    def __init__(self, hielo, nombre, dificultad, número_vueltas, 
    contrincantes, largo_pista):
        super().__init__(nombre, dificultad, número_vueltas, contrincantes, largo_pista)
        self.hielo = int(hielo)

    def __str__(self):
        return super().__str__("Helada")


class PistaRocosa(Pista):

    def __init__(self, rocas, nombre, dificultad, número_vueltas, 
    contrincantes, largo_pista):
        super().__init__(nombre, dificultad, número_vueltas, contrincantes, largo_pista)
        self.rocas = int(rocas)
    
    def __str__(self):
        return super().__str__("Rocosa")

class PistaSuprema(Pista):

    def __init__(self, hielo, rocas, nombre, dificultad, número_vueltas, 
    contrincantes, largo_pista):
        super().__init__(nombre, dificultad, número_vueltas, contrincantes, largo_pista)
        self.hielo = int(hielo)
        self.rocas = int(rocas)
    
    def __str__(self):
        return super().__str__("Suprema")

class Piloto:
    """
    Pilot class.
    Possible teams:
     - Tareo
     - Hibrido
     - Docencio
    
    Pilots must have one team (and only one).
    """

    def __init__(self, nombre, equipo, dinero=0, personalidad=None, contextura=None, 
    equilibrio=None, experiencia=0, vehículos=[], new_pilot=False):
        """
        Pilot characteristics:
         - Nombre: nombre (saved in pilotos.csv)
         - Equipo: equipo (saved in pilotos.csv)
         - Dinero: dinero (saved in pilotos.csv) ****
         - Personalidad: personalidad (saved in pilotos.csv, bound to team except Hibrido)
         - Contextura: contextura (saved in pilotos.csv, range bound to team)
         - Equilibrio: equilibrio (saved in pilotos.csv, range bound to team)
         - Experiencia: experiencia (saved in pilotos.csv) ****
         - Vehicle list: vehículos (saved in vehículos.csv) ****
         - new_pilot: defines if pilot was just created of loaded
        Note: **** means this should be a property

        If a new pilot is created it should only receive a name and a team.
        New pilots start with dinero = 0, experiencia = 0, vehículos = []
        """
        self.nombre = nombre
        self.equipo = equipo
        self.__dinero = int(dinero)

        if new_pilot: 
            DEF_ARGS = pm.EQUIPOS[self.equipo.upper()]
            self.personalidad = choice(DEF_ARGS['PERSONALIDAD'])
            self.contextura = randint(DEF_ARGS['CONTEXTURA']['MIN'], DEF_ARGS['CONTEXTURA']['MAX']) 
            self.equilibrio = randint(DEF_ARGS['EQUILIBRIO']['MIN'], DEF_ARGS['EQUILIBRIO']['MAX'])
            self.experiencia = 0
            self.vehículos = []
        else: 
            self.personalidad = personalidad
            self.contextura = int(contextura)
            self.equilibrio = int(equilibrio)
            self.experiencia = int(experiencia)
            self.vehículos = vehículos
    
    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, value):
        if value < 0:
            self.__dinero = 0
        else: 
            self.__dinero = self.__dinero - value


class Contrincante:

    def __init__(self, nombre, nivel, personalidad, contextura, equilibrio, 
    experiencia, equipo, vehículos):
        """
        Pilot characteristics:
         - Nombre: nombre (saved in contrincantes.csv)
         - Nivel: nivel (saved in contrincantes.csv)
         - Personalidad: personalidad (saved in contrincantes.csv)
         - Contextura: contextura (saved in contrincantes.csv)
         - Equilibrio: equilibrio (saved in contrincantes.csv)
         - Experiencia: experiencia (saved in contrincantes.csv)
         - Equipo: equipo (saved in contrincantes.csv)
         - Vehicle list: vehículos (saved in vehículos.csv)

        Contrincantes are always loaded from contrincantes.csv
        For this reason there are no default arguments.
        """
        self.nombre = nombre
        self.nivel = nivel
        self.personalidad = personalidad
        self.contextura = int(contextura)
        self.equilibrio = int(equilibrio)
        self.experiencia = int(experiencia)
        self.equipo = equipo
        self.vehículos = vehículos
        self.vehiculo = None
