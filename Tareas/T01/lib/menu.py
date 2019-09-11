import os
from abc import ABC, abstractmethod

import lib.gametext as gametext
from lib.funciones import clear, get_piloto
from lib.carreras import Tareo, Docencio, Hibrido
from lib.carreras import Automovil, Motocicleta, Troncomovil, Bicicleta



class Menu(ABC):
    """Abstract class. Inherited by more specific menu classes."""

    @abstractmethod
    def __init__(self):
        self.actions = {}

    def recibir_input(self, msj="Ingrese una opción: "):
        """Receives and returns a numeric input. Number must be in action list."""
        while True:
            number = input(msj)
            if number.isdecimal():
                number = int(number)
                if number in self.actions.keys():
                    return number
            clear()
            print(self)
            print(f"Debes entrar un número según las acciones disponibles.")

    def get_str(self, actions=self.actions):
        """Returns str. Contains actions items + decorative elements."""
        string = ""
        
        string += ">>>|  ┌───┐\n"
        for action in actions:
            string += f">>>|  │ {action} │    {actions[action]}\n"
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


class MenuSesion(Menu):
    def __init__(self):
        super().__init__()
        self.actions.update({
            1 : "Nueva partida",
            2 : "Cargar partida",
            0 : "Salir del juego"
        })

    def cargar_partida(self):
        """Return Piloto object based on user input."""
        clear()
        print(gametext.LOAD_TITLE)
        print(gametext.SEP)
        
        while True:
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                break
            piloto = get_piloto(name)
            if piloto is not None:
                return piloto
            
            clear()
            print(gametext.LOAD_TITLE)
            print(gametext.SEP)
            print(f"No existen partidas guardadas para el nombre {name}")

    def nueva_partida(self):
        clear()

    def __str__(self):
        string = gametext.TITLE + gametext.SEP + str(self.get_str())
        return string


class MenuPrincipal(Menu):
    def __init__(self):
        super().__init__()




class MenuCompraVehiculos(Menu):
    def __init__(self):
        super().__init__()

    def recibir_input(self):
        pass

class MenuPreparacionCarrera(Menu):
    def __init__(self):
        super().__init__()

    def recibir_input(self):
        super().__init__()

class MenuCarrera(Menu):
    def __init__(self):
        super().__init__()

    def recibir_input(self):
        super().__init__()

class MenuPits(Menu):
    def __init__(self):
        super().__init__()

    def recibir_input(self):
        pass
