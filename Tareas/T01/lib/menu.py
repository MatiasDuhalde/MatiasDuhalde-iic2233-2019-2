import os
import sys
from abc import ABC, abstractmethod

import lib.gametext as gametext
import lib.parametros as pm
from lib.funciones import clear, get_piloto
from lib.carreras import Piloto
from lib.carreras import Automovil, Motocicleta, Troncomovil, Bicicleta
from lib.carreras import PistaHelada, PistaRocosa, PistaSuprema

class Menu(ABC):
    """Abstract class. Inherited by more specific menu classes."""

    # strings based in original data from vehículos.csv and pistas.csv
    TIPOS_VEHICULO = {"automóvil" : Automovil, "motocicleta" : Motocicleta, 
    "troncomóvil" : Troncomovil, "bicicleta" : Bicicleta}
    TIPOS_PISTA = {"PistaHelada" : PistaHelada, "PistaRocosa" : PistaRocosa, 
    "PistaSuprema" : PistaSuprema}

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
            clear()
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
        """Return Piloto object based on user input. Loads from pilotos.csv"""
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
        """Return Piloto object based on user input."""
        clear()
        print(gametext.NEW_TITLE)
        print(gametext.SEP + self.get_str({0 : "Volver"}))
        
        while True: # This chunk (while) gets the name
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                name = False
                break
            elif len(name) > 40:
                clear()
                print(gametext.NEW_TITLE)
                print(gametext.SEP + self.get_str({0 : "Volver"}))
                print("Nombre de usuario muy largo! Intente con uno más corto.")
            elif name == "":
                clear()
                print(gametext.NEW_TITLE)
                print(gametext.SEP + self.get_str({0 : "Volver"}))
                print("Debes ingresar un nombre.")
            else:
                piloto = get_piloto(name, self.TIPOS_VEHICULO, Piloto)
                
                if piloto: # In case name is already registered
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
        
        while name: # This chunk gets the team
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
        This method may seem trivial for this menu/subclass as there's only one 
        destination, but it makes sense for the others.
        """
        super().go_to(option)
        destinations = {0 : "Exit", 1 : MenuPrincipal, 2: MenuPrincipal}
        piloto = None
        if option == 0:
            sys.exit(0)
        elif option == 1:
            piloto = self.nueva_partida()
        elif option == 2:
            piloto = self.cargar_partida()
        if piloto:
            return destinations[option](piloto)
        self.active = True
        return None

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
        super().go_to(option)
        destinations = {0 : MenuSesion, 
        1 : MenuPreparacionCarrera, 
        2 : MenuCompraVehiculos, 
        3 : MenuPrincipal}
        if option == 0:
            return destinations[option]()
        elif option == 1:
            self.iniciar_carrera()
        elif option == 2:
            self.comprar_vehiculos()
        elif option == 3:
            self.guardar_partida()

        return destinations[option]

    def iniciar_carrera(self):
        if len(self.piloto.vehículos) == 0: 
            print("No tienes ningún vehículo! Prueba comprando alguno.")
            self.active = True
            input("Presiona enter para volver...")
    
    def comprar_vehiculos(self):
        pass

    def guardar_partida(self):
        """
        Overwrites pilotos.csv, vehículos.csv
        A same pilot with the same name can't have 2 entries in pilotos.csv
        Previous lines describing the pilot are deleted and replaced with new
        ones based on the pilot's attributes.
        """
        # Delete old line(s) in pilotos.csv
        lines = []
        with open(os.path.join(*pm.PATHS["PILOTOS"]), 'r', 
        encoding='utf-8') as pilotos:
            headers_string = pilotos.readline()
            lines.append(headers_string)
            headers = headers_string.rstrip().split(",")
            for line in pilotos:
                lines.append(line)
                line = line.rstrip().split(",")
                kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
                if kwargs["nombre"] == self.piloto.nombre:
                    lines.pop()
        
        # Rewrite pilotos.csv
        save_data = {"Nombre" : self.piloto.nombre, 
        "Dinero" : self.piloto.dinero, "Personalidad" : self.piloto.personalidad, 
        "Contextura" : self.piloto.contextura, "Equilibrio" : self.piloto.equilibrio, 
        "Experiencia" : self.piloto.experiencia, "Equipo" : self.piloto.equipo}
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
        with open(os.path.join(*pm.PATHS["VEHICULOS"]), 'r', 
        encoding='utf-8') as vehiculos:
            headers_string = vehiculos.readline()
            lines.append(headers_string)
            headers = headers_string.rstrip().split(",")
            for line in vehiculos:
                lines.append(line)
                line = line.rstrip().split(",")
                kwargs = {headers[index].lower() : line[index] for index in range(len(line))}
                if kwargs["dueño"] == self.piloto.nombre:
                    lines.pop()
        
        # Rewrite vehículos.csv
        for vehiculo in self.piloto.vehículos:
            save_data = {"Nombre" : vehiculo.nombre, "Dueño" : vehiculo.dueño, 
            "Categoría" : list(self.TIPOS_VEHICULO.keys())[list(
                self.TIPOS_VEHICULO.values()).index(type(vehiculo))], 
            "Chasis" : vehiculo.chasis, "Carrocería" : vehiculo.carrocería, 
            "Ruedas" : vehiculo.ruedas, "Motor o Zapatillas" : vehiculo.motor 
            if type(vehiculo) in [Automovil, Motocicleta] else vehiculo.zapatillas, 
            "Peso" : vehiculo.peso}
            order = {headers[index] : index for index in range(len(headers))}
            save_data = [str(save_data[key]) for key in sorted(save_data, key=order.get)]
            save_data = ",".join(save_data) + '\n'
            lines.append(save_data)
        with open(os.path.join(*pm.PATHS["VEHICULOS"]), 'w', 
        encoding='utf-8') as vehiculos:
            for line in lines:
                vehiculos.write(line)
        
        self.active = True
        print(gametext.SAVE_TITLE)
        print(gametext.SEP)
        input("Presione enter para volver...")

    def __str__(self):
        string = gametext.SEP3 + '\n' + f"    Piloto: {self.piloto.nombre}\n" + \
            f"    Dinero: ${str(self.piloto.dinero)}\n" + gametext.SEP3 + \
            '\n' + self.get_str()
        return string

class MenuCompraVehiculos(Menu):
    def __init__(self):
        super().__init__()

    def go_to(self, option):
        super().go_to(option)

    def __str__(self):
        pass

class MenuPreparacionCarrera(Menu):
    def __init__(self):
        super().__init__()

    def go_to(self, option):
        super().go_to(option)

    def __str__(self):
        pass

class MenuCarrera(Menu):
    def __init__(self):
        super().__init__()

    def go_to(self, option):
        super().go_to(option)

    def __str__(self):
        pass

class MenuPits(Menu):
    def __init__(self):
        super().__init__()

    def go_to(self, option):
        super().go_to(option)

    def __str__(self):
        pass
