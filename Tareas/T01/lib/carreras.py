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
    def __init__(self, chasis, carroceria, ruedas):
        self.chasis = chasis
        self.carroceria = carroceria
        self.ruedas = ruedas


class Automovil(Vehiculo):
    
    def __init__(self, chasis, carroceria, ruedas, motor):
        super().__init__(chasis, carroceria, ruedas)
        self.motor = motor


class Motocicleta(Vehiculo):
    
    def __init__(self, chasis, carroceria, ruedas, motor):
        super().__init__(chasis, carroceria, ruedas)
        self.motor = motor


class Troncomovil(Vehiculo):
    
    def __init__(self, chasis, carroceria, ruedas, zapatillas):
        super().__init__(chasis, carroceria, ruedas)
        self.zapatillas = zapatillas


class Bicicleta(Vehiculo):
    
    def __init__(self, chasis, carroceria, ruedas, zapatillas):
        super().__init__(chasis, carroceria, ruedas)
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
    def __init__(self, nombre, dinero=0, n_exp=0, ):
        self.nombre = nombre
        self.dinero = dinero
        self.nivel_de_experiencia = n_exp


class Tareo(Piloto):
    """Tareos team. Inherits from Piloto."""
    
    def __init__(self):
        super().__init__()
        self.contextura = randint(26, 45)
        self.equilibrio = randint(36, 55)
        self.personalidad = 'precavido'


class Hibrido(Piloto):
    """Híbridos team. Inherits from Piloto"""
    
    def __init__(self):
        super().__init__()
        self.contextura = randint(35, 54)
        self.equilibrio = randint(20, 34)
        self.personalidad = choice(['precavido', 'osado'])


class Docencio(Piloto):
    """Docencios team. Inherits from Piloto"""

    def __init__(self):
        super().__init__()
        self.contextura = randint(44, 60)
        self.equilibrio = randint(4, 10)
        self.personalidad = 'osado'
        
