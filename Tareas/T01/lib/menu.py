from abc import ABC, abstractmethod
import lib.gametext as gametext
from lib.funciones import clear



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
            print(f"Debes entrar un número según las acciones disponibles")


    def get_str(self):
        """Returns str. Contains self.actions items + decorative elements."""
        string = ""
        
        string += ">>>|  ┌───┐\n"
        for action in self.actions:
            string += f">>>|  │ {action} │    {self.actions[action]}\n"
            if action != 0:
                string += ">>>|  ├───┤\n"
        string += ">>>|  └───┘\n"
        string += gametext.SEP2
        
        return string


    @abstractmethod
    def __str__(self):
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
        pass

    def crear_partida(self):
        pass

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
