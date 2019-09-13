import os
import sys
from abc import ABC, abstractmethod

import lib.gametext as gametext
from lib.funciones import clear, get_piloto
from lib.carreras import Piloto
from lib.carreras import Automovil, Motocicleta, Troncomovil, Bicicleta
from lib.carreras import PistaHelada, PistaRocosa, PistaSuprema

# CHECK PARAMETERS IN PARAMETROS.PY


class Menu(ABC):
    """Abstract class. Inherited by more specific menu classes."""

    # Objects dicts:

    # SUPUESTO: Híbridos se escribe con tilde en pilotos.csv, no hay ejemplo en 
    # datos originales.

    # string based in original data form vehículos.csv
    TIPOS_VEHICULO = {"automóvil" : Automovil, "motocicleta" : Motocicleta, 
    "troncomóvil" : Troncomovil, "bicicleta" : Bicicleta}

    TIPOS_PISTA = {"PistaHelada" : PistaHelada, "PistaRocosa" : PistaRocosa, 
    "PistaSuprema" : PistaSuprema}

    @abstractmethod
    def __init__(self):
        self.actions = {}

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
            clear()
            if not to_print:
                print(self)
            else:
                print(to_print)
            print(f"Debes entrar un número según las acciones disponibles.")

    @abstractmethod
    def go_to(self, option):
        pass

    def get_str(self, actions={}):
        """Returns str. Contains actions items + decorative elements."""
        if not actions:
            actions = self.actions

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
            0 : "Salir del juego"})

    def cargar_partida(self):
        """Return Piloto object based on user input."""
        clear()
        print(gametext.LOAD_TITLE)
        print(gametext.SEP + self.get_str({0 : "Volver"}))
        
        while True:
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                break
            piloto = get_piloto(name, self.TIPOS_VEHICULO, Piloto)
            if piloto:
                return piloto
            
            clear()
            print(gametext.LOAD_TITLE)
            print(gametext.SEP + self.get_str({0 : "Volver"}))
            print(f"No existen partidas guardadas para el nombre '{name}'.")

    def nueva_partida(self):
        clear()
        print(gametext.NEW_TITLE)
        print(gametext.SEP + self.get_str({0 : "Volver"}))
        
        # This chunk gets the name
        while True:
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                name = False
                break
            elif len(name) > 40:
                clear()
                print(gametext.NEW_TITLE)
                print(gametext.SEP + self.get_str({0 : "Volver"}))
                print("Nombre de usuario muy largo! Intente con uno más corto.")
            else:
                piloto = get_piloto(name, self.TIPOS_VEHICULO, Piloto)
                
                # In case name is already registered
                if piloto:
                    actions = {1 : f"Crear nueva partida con nombre {name}",
                    0 : "Volver"}
                    string = gametext.NEW_TITLE + '\n' + gametext.SEP + '\n' + \
                        '{:^79}'.format("El nombre de usuario ya existe!") + '\n' + \
                        self.get_str(actions=actions)
                    
                    clear()
                    print(string)
                    
                    user_input = self.recibir_input(actions=actions, to_print=string)
                    if user_input == 0:
                        name = False
                break
        
        # This chunk gets the team
        while name:
            actions = {1 : "Tareos", 2 : "Híbridos", 3 : "Docencios", 0 : "Volver"}
            string = gametext.NEW_TITLE + '\n' +  gametext.SEP + '\n' + \
                '{:^79}'.format("Elije un equipo:") + '\n' + \
                self.get_str(actions=actions)
            
            clear()
            print(string)

            user_input = self.recibir_input(actions=actions, to_print=string)
            if user_input == 0:
                break
            else:
                return Piloto(name, actions[user_input], new_pilot=True)

    def go_to(self, option):
        """
        This method may seem trivial for this menu/subclass, but it makes 
        sense for the others.
        """
        destinations = {0 : "Exit", 1 : MenuPrincipal, 2: MenuPrincipal}
        if option == 0:
            sys.exit(0)
        return destinations[option]

    def __str__(self):
        string = gametext.TITLE + gametext.SEP + str(self.get_str())
        return string


class MenuPrincipal(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
        self.actions.update({1 : "Iniciar Carrera", 
        2 : "Comprar vehículos",  
        3 : "Guardar partida",
        0 : "Volver"})

    def go_to(self, option):
        destinations = {0 : "MenuSesion", 
        1 : "MenuPreparacionCarrera", 
        2 : "MenuCompraVehiculos"}
        return destinations[option]

    def __str__(self):
        string = f"    Piloto: {self.piloto.nombre}\n" + \
            f"    Dinero: ${str(self.piloto.dinero)}\n" + gametext.SEP2 + \
            '\n' + self.get_str()
        return string

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
