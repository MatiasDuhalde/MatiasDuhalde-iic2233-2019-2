import sys
from random import random, sample, choice

import lib.gametext as gametext
import lib.parametros as pm
import lib.funciones as f
from lib.carrera import carrera
from lib.entidades import Piloto, Contrincante
from lib.entidades import Automovil, Motocicleta, Troncomovil, Bicicleta
from lib.mainmenu import Menu

class MenuSesion(Menu):
    def __init__(self):
        super().__init__()
        self.actions.update({
            1 : "Nueva partida",
            2 : "Cargar partida",
            0 : "Salir del juego"})

    def cargar_partida(self):
        """Return Piloto object based on user input. Loads from pilotos.csv"""
        f.clear()
        print(gametext.LOAD_TITLE)
        print(gametext.SEP + self.get_str({0 : "Volver"}))
        
        while True:
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                break
            piloto = f.get_piloto(name, self.TIPOS_VEHICULO, Piloto)
            if piloto:
                return piloto
            
            f.clear()
            print(gametext.LOAD_TITLE)
            print(gametext.SEP + self.get_str({0 : "Volver"}))
            print(f"No existen partidas guardadas para el nombre '{name}'.")

    def nueva_partida(self):
        """Return Piloto object based on user input."""
        f.clear()
        print(gametext.NEW_TITLE)
        print(gametext.SEP + self.get_str({0 : "Volver"}))
        
        while True: # This chunk (while) gets the name
            name = input("Introduzca su nombre: ")
            
            if name == "0":
                name = False
                break
            elif len(name) > 40:
                f.clear()
                print(gametext.NEW_TITLE)
                print(gametext.SEP + self.get_str({0 : "Volver"}))
                print("Nombre de usuario muy largo! Intente con uno más corto.")
            elif name == "":
                f.clear()
                print(gametext.NEW_TITLE)
                print(gametext.SEP + self.get_str({0 : "Volver"}))
                print("Debes ingresar un nombre.")
            else:
                piloto = f.get_piloto(name, self.TIPOS_VEHICULO, Piloto)
                
                if piloto: # In case name is already registered
                    actions = {1 : f"Crear nueva partida con nombre {name}",
                    0 : "Volver"}
                    string = gametext.NEW_TITLE + '\n' + gametext.SEP + '\n' + \
                        '{:^79}'.format("El nombre de usuario ya existe!") + '\n' + \
                        self.get_str(actions=actions)
                    
                    f.clear()
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
            
            f.clear()
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
            f.guardar_partida(piloto, self.TIPOS_VEHICULO)
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
            if self.iniciar_carrera():
                return destinations[option](self.piloto)
        elif option == 2:
            return destinations[option](self.piloto)
        elif option == 3:
            self.guardar()
            return destinations[option](self.piloto)


    def iniciar_carrera(self):
        if len(self.piloto.vehículos) == 0: 
            print("No tienes ningún vehículo! Prueba comprando alguno.")
            self.active = True
            input("Presione enter para volver...")
            return False
        return True

    def guardar(self, show=True):
        f.guardar_partida(self.piloto, self.TIPOS_VEHICULO)
        self.active = True
        if show:
            f.clear()
            print(gametext.SAVE_TITLE)
            print(gametext.SEP)
            input("Presione enter para volver...")
    
    def __str__(self):
        string = gametext.SEP3 + '\n' + f"    Piloto: {self.piloto.nombre}\n" + \
            f"    Dinero: ${str(self.piloto.dinero)}\n" + gametext.SEP3 + \
            '\n' + self.get_str()
        return string

class MenuCompraVehiculos(Menu):
    def __init__(self, piloto, gratis=True):
        super().__init__()
        self.piloto = piloto
        self.__gratis = gratis
        self.actions.update({
        1 : f"Automóvil         ${pm.PRECIOS['AUTOMOVIL']}",
        2 : f"Motocicleta       ${pm.PRECIOS['MOTOCICLETA']}",
        3 : f"Troncomóvil       ${pm.PRECIOS['TRONCOMOVIL']}",
        4 : f"Bicicleta         ${pm.PRECIOS['BICICLETA']}",
        0 : "Volver"})
    
    @property
    def gratis(self):
        self.__gratis = len(self.piloto.vehículos) == 0
        return self.__gratis

    def go_to(self, option):
        super().go_to(option)
        destinations = {0 : MenuPrincipal}
        if option == 0:
            return destinations[option](self.piloto)
        else:
            self.comprar_vehiculos(option)
            self.active = True

    def comprar_vehiculos(self, option):
        clases_vehiculos = list(self.TIPOS_VEHICULO.values())
        vehiculo = {index : clases_vehiculos[index - 1] for index in range(1,5)}[option]
        if self.piloto.dinero < pm.PRECIOS[vehiculo.__name__.upper()] and not self.gratis:
            print("No tienes el dinero suficiente para comprar este vehículo.")
            input("Presione enter para continuar...")
        else:
            while True:
                car_name = input("Ingrese un nombre para el vehículo: ")
                if car_name == "0":
                    break
                elif car_name in [car.nombre for car in self.piloto.vehículos]:
                    print("Ya tienes un vehículo con este nombre.")
                else:
                    self.piloto.vehículos.append(vehiculo(car_name, 
                    self.piloto.nombre, new_car = True))
                    self.piloto.dinero -= pm.PRECIOS[vehiculo.__name__.upper()]
                    f.guardar_partida(self.piloto, self.TIPOS_VEHICULO)
                    break

    def __str__(self):
        string = gametext.STORE_TITLE + '\n' + gametext.SEP2 + '\n' + \
        f"    Dinero: ${str(self.piloto.dinero)}\n" + \
        f"    Tienes {len(self.piloto.vehículos)} vehículos.\n" + str(self.get_str())
        if self.gratis:
            string += "\nEl primer vehículo es gratis!"
        return string

class MenuPreparacionCarrera(Menu):
    def __init__(self, piloto):
        super().__init__()
        self.piloto = piloto
        self.pistas = f.get_pistas(self.TIPOS_PISTA, self.TIPOS_VEHICULO, Contrincante)
        self.actions = {index : str(self.pistas[index - 1]) for index in range(1, 
        len(self.pistas) + 1)}
        self.actions.update({0 : "Volver"})

    def go_to(self, option):
        super().go_to(option)
        destinations = {0 : MenuPrincipal, 1 : MenuSelectVehiculo}
        if option == 0:
            return destinations[option](self.piloto)
        else:
            return destinations[1](self.piloto, self.pistas[option - 1])

    def __str__(self):
        string = gametext.SEP + "{:^79}\n".format("Elige una pista") + \
        gametext.SEP2 + '\n' + ' '*15 + "{:38} {:14}{:15}\n".format("Nombre", \
        "Tipo", "N vueltas") + str(self.get_str())
        return string

class MenuSelectVehiculo(Menu):
    def __init__(self, piloto, pista):
        super().__init__()
        self.piloto = piloto
        self.pista = pista
        self.actions = {index : str(self.piloto.vehículos[index - 1]) for \
            index in range(1, len(self.piloto.vehículos) + 1)}
        self.actions.update({0 : "Volver"})

    def go_to(self, option):
        super().go_to(option)
        destinations = {0 : MenuPreparacionCarrera, 1 : MenuCarrera}
        if option == 0:
            return destinations[option](self.piloto)
        else:
            return destinations[1](self.piloto, self.pista, 
            self.piloto.vehículos[option - 1])

    def __str__(self):
        string = gametext.SEP + "{:^79}\n".format("Elige un vehículo") + \
        gametext.SEP2 + '\n' + ' '*15 + "{:49}{:15}\n".format("Nombre", \
        "Clase") + str(self.get_str())
        return string

class MenuCarrera(Menu):
    def __init__(self, piloto, pista, vehiculo):
        super().__init__()
        self.piloto = piloto
        self.pista = pista
        self.vehiculo = vehiculo
        self.actions.update({1 : "Entrar a los pits",
        2 : "Siguiente vuelta",
        0 : "Volver"})
        
        if len(self.pista.contrincantes) > pm.NUMERO_CONTRINCANTES:
            self.pista.contrincantes = sample(self.pista.contrincantes, \
            pm.NUMERO_CONTRINCANTES)
        for contrincante in self.pista.contrincantes:
             contrincante.vehiculo = choice(contrincante.vehículos)

    def go_to(self, option):
        super().go_to(option)

    def empezar_carrera(self, Pits):
        carrera(self.piloto, self.vehiculo, self.pista, self, Pits)
        self.active = False

    def __str__(self):
        string = gametext.SEP3 + '\n' + \
        "    {:15.15}{:60.60}\n".format("Pista: ", self.pista.nombre) + \
        "    {:15.15}{:60.60}\n".format("Piloto: ", self.piloto.nombre) + \
        "    {:15.15}{:60.60}\n".format("Vehículo: ", self.vehiculo.nombre) + \
        gametext.SEP3 + '\n'
        return string

class MenuPits(Menu):
    def __init__(self, piloto, pista, vehiculo):
        super().__init__()
        self.piloto = piloto
        self.pista = pista
        self.vehiculo = vehiculo
        power = "Zapatillas" if type(self.vehiculo) in [Troncomovil, Bicicleta] \
            else "Motor"
        self.actions.update({
        1 : "Chasis         ${}".format(pm.MEJORAS['CHASIS']['COSTO']),
        2 : "Carrocería     ${}".format(pm.MEJORAS['CARROCERIA']['COSTO']),
        3 : "Ruedas         ${}".format(pm.MEJORAS['RUEDAS']['COSTO']),
        4 : "{:15}${}".format(power, pm.MEJORAS[power.upper()]['COSTO']),
        0 : "Volver"})

    def go_to(self, option):
        super().go_to(option)

    def __str__(self):
        string = gametext.PITS_TITLE + '\n' + gametext.SEP2 + \
        f"\n    Dinero:   ${self.piloto.dinero}\n" + \
        f"\n    Vehiculo: ${self.vehiculo.nombre}\n" + gametext.SEP2 + '\n' + \
        "{:^79}".format("Selecciona una mejora!") + '\n' + str(self.get_str())
        return string
