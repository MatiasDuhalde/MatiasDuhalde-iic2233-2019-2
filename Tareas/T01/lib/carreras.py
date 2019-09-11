from abc import ABC, abstractmethod
from random import randint, choice

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
        * carroceria
        * ruedas
     - Specific
        * motor (Automovil, Motocicleta)
        * zapatillas (Troncomovil, Bicicleta)

    """
    @abstractmethod
    def __init__(self, nombre, owner, chasis, carroceria, ruedas, peso):
        """Arguments are ordered according to pilotos.csv original data."""
        self.nombre = nombre
        self.owner = owner
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas
        self.peso = peso


class Automovil(Vehiculo):
    
    def __init__(self, nombre, owner, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, owner, chasis, carroceria, ruedas, peso)
        self.motor = motor


class Motocicleta(Vehiculo):
    
    def __init__(self, nombre, owner, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, owner, chasis, carroceria, ruedas, peso)
        self.motor = motor


class Troncomovil(Vehiculo):
    
    def __init__(self, nombre, owner, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, owner, chasis, carroceria, ruedas, peso)
        self.zapatillas = zapatillas


class Bicicleta(Vehiculo):
    
    def __init__(self, nombre, owner, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, owner, chasis, carroceria, ruedas, peso)
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
        


class Piloto(ABC):
    """
    Pilot modeling class.
    
    Inherited by more specific subclasses (pilot team):
     - Tareo
     - Hibrido
     - Docencio
    
    Pilots can only have one team.

    """

    @abstractmethod
    def __init__(self, nombre, dinero=0, n_exp=0, vehiculos=[]):
        """
        Arguments are ordered according to pilotos.csv original data, i.e.:
        
        Pilot characteristics:
         - Nombre: nombre (saved in pilotos.csv)
         - Dinero: dinero (saved in pilotos.csv) ****
         - Personalidad: personalidad (saved in pilotos.csv, bound to team except Hibrido)
         - Contextura: contextura (saved in pilotos.csv, range bound to team)
         - Equilibrio: equilibrio (saved in pilotos.csv, range bound to team)
         - Experiencia: nivel_de_experiencia (saved in pilotos.csv) ****
         - Equipo: (saved in pilotos.csv, implicit in subclass)
         - Vehicle list: vehicles (saved in vehículos.csv) ****
        Note: **** means this should be a property

        If a new pilot is created it should only receive a name and a team.
        New pilots start with dinero = 0, nivel_de_experiencia = 0, vehiculos = []
        """
        self.nombre = nombre
        self.dinero = dinero
        self.nivel_de_experiencia = n_exp
        self.vehiculos = vehiculos


class Tareo(Piloto):
    """Tareos team. Inherits from Piloto."""
    
    def __init__(self, nombre, dinero=0, personalidad='precavido', 
    contextura=randint(26, 45), equilibrio=randint(36, 55), n_exp, vehiculos = []):
        """
        Arguments are ordered according to pilotos.csv original data. i.e.:
        Nombre, Dinero, Personalidad, Contextura, 
        Equilibrio, Experiencia, Equipo,
        Lista de Vehículos (obtained from vehículos.csv)
        """
        super().__init__(nombre, dinero, n_exp, vehiculos)
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.personalidad = personalidad



class Hibrido(Piloto):
    """Híbridos team. Inherits from Piloto"""

    def __init__(self, nombre, dinero=0, personalidad=choice(['precavido', 'osado']), 
    contextura=randint(35, 54), equilibrio=randint(20, 34), n_exp=0, vehiculos = []):
        """
        Arguments are ordered according to pilotos.csv original data. i.e.:
        Nombre, Dinero, Personalidad, Contextura, 
        Equilibrio, Experiencia, Equipo,
        Lista de Vehículos (obtained from vehículos.csv)
        """
        super().__init__(nombre, dinero, n_exp, vehiculos)
        self.contextura = contextura
        self.equilibrio = equilibrio
        self.personalidad = personalidad


class Docencio(Piloto):
    """Docencios team. Inherits from Piloto"""

    def __init__(self):
        super().__init__()
        self.contextura = randint(44, 60)
        self.equilibrio = randint(4, 10)
        self.personalidad = 'osado'
        
