from abc import ABC, abstractmethod

import lib.gametext as gametext
import lib.funciones as f
from lib.entidades import Automovil, Motocicleta, Troncomovil, Bicicleta
from lib.entidades import PistaHelada, PistaRocosa, PistaSuprema

class Menu(ABC):
    """Abstract class. Inherited by more specific menu classes."""

    # strings based in original data from vehículos.csv and pistas.csv
    TIPOS_VEHICULO = {"automóvil" : Automovil, "motocicleta" : Motocicleta, 
    "troncomóvil" : Troncomovil, "bicicleta" : Bicicleta}
    TIPOS_PISTA = {"pista hielo" : PistaHelada, "pista rocosa" : PistaRocosa, 
    "pista suprema" : PistaSuprema}

    @abstractmethod
    def __init__(self):
        self.actions = {}
        self.active = True

    def recibir_input(self, msj="Ingrese una opción: ", actions={}, to_print=None):
        """Receives and returns a numeric input. Number must be in action list."""
        if not actions:
            actions = self.actions
        while True:
            number = input(msj)
            if number.isdecimal():
                number = int(number)
                if number in actions.keys():
                    return number
            f.clear()
            if not to_print:
                print(self)
            else:
                print(to_print)
            print(f"Debes entrar un número según las acciones disponibles.")

    @abstractmethod
    def go_to(self, option):
        self.active = False

    def get_str(self, actions={}):
        """Returns str. Contains actions items + decorative elements."""
        if not actions:
            actions = self.actions

        string = ""
        
        string += ">>>|  ┌───┐\n"
        for action in actions:
            string += ">>>|  │{:^3}│    {}\n".format(action, actions[action])
            if action != 0:
                string += ">>>|  ├───┤\n"
        string += ">>>|  └───┘\n"
        string += gametext.SEP2
        
        return string

    @abstractmethod
    def __str__(self):
        """Meant to be used with print(). Shows the menu."""
        string = str(self.get_str())
        return string