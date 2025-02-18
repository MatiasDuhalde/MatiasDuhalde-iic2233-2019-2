from collections import namedtuple, defaultdict
from lib.funciones import clear
from lib.menu import MenuSesion, MenuPrincipal, MenuCarrera, \
    MenuCompraVehiculos, MenuPits, MenuPreparacionCarrera, MenuSelectVehiculo


# -----------------------------------------------------------------------------
#                                 GAME FLOW
# -----------------------------------------------------------------------------

def default():
    InactiveMenu = namedtuple("InactiveMenu", ["active"])
    return InactiveMenu(False)

if __name__ == "__main__":

    menus = defaultdict(default)
    # menus looks like: {"StringWithNameofClass" : instanceofClass, ...}
    main_loop = True

    menu_sesion = MenuSesion()
    menus[type(menu_sesion).__name__] = menu_sesion

    # All the sub loops literally look the same. Something should be done about it
    while main_loop:
        while menus["MenuSesion"].active:
            menu_actual = menus["MenuSesion"]
            
            clear()
            print(menu_actual)
            user_input = menu_actual.recibir_input()
            menu_actual = menu_actual.go_to(user_input)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual
        
        while menus["MenuPrincipal"].active:
            menu_actual = menus["MenuPrincipal"]
            
            clear()
            print(menu_actual)
            user_input = menu_actual.recibir_input()
            menu_actual = menu_actual.go_to(user_input)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual

        while menus["MenuPreparacionCarrera"].active:
            menu_actual = menus["MenuPreparacionCarrera"]
            
            clear()
            print(menu_actual)
            user_input = menu_actual.recibir_input()
            menu_actual = menu_actual.go_to(user_input)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual

        while menus["MenuSelectVehiculo"].active:
            menu_actual = menus["MenuSelectVehiculo"]
            
            clear()
            print(menu_actual)
            user_input = menu_actual.recibir_input()
            menu_actual = menu_actual.go_to(user_input)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual

        while menus["MenuCompraVehiculos"].active:
            menu_actual = menus["MenuCompraVehiculos"]
            
            clear()
            print(menu_actual)
            user_input = menu_actual.recibir_input()
            menu_actual = menu_actual.go_to(user_input)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual

        while menus["MenuCarrera"].active:
            menu_actual = menus["MenuCarrera"]
            piloto = menu_actual.piloto
            vehiculo = menu_actual.vehiculo
            pista = menu_actual.pista

            clear()
            print(menu_actual)
            input("Presiona ENTER para comenzar la carrera...")
            clear()
            pits = MenuPits(piloto, vehiculo)
            menu_actual.empezar_carrera(pits)
            
            menu_actual = MenuPrincipal(piloto)
            if menu_actual:
                menus[type(menu_actual).__name__] = menu_actual

