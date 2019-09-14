from collections import namedtuple, defaultdict
from lib.funciones import clear
from lib.menu import MenuSesion, MenuPrincipal, MenuCarrera, \
    MenuCompraVehiculos, MenuPits, MenuPreparacionCarrera


# -----------------------------------------------------------------------------
#                                 GAME FLOW
# -----------------------------------------------------------------------------

def default():
    InactiveMenu = namedtuple("InactiveMenu", ["active"])
    return InactiveMenu(False)

menus = defaultdict(default)
# menus looks like: {"StringWithNameofClass" : instanceofClass, ...}
main_loop = True

menu_sesion = MenuSesion()
menus[type(menu_sesion).__name__] = menu_sesion

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
        piloto = menu_actual.piloto
        
        clear()
        print(menu_actual)
        
        user_input = menu_actual.recibir_input()
        menu_actual = menu_actual.go_to(user_input)
        if menu_actual:
            menus[type(menu_actual).__name__] = menu_actual

    while menus["MenuPreparacionCarrera"].active:
        menu_actual = menus["MenuPreparacionCarrera"]
        piloto = menu_actual.piloto
        
        clear()
        print(menu_actual)
        print("Acá se prepara la carrera!")
        user_input = menu_actual.recibir_input()
        menu_actual = menu_actual.go_to(user_input)
        if menu_actual:
            menus[type(menu_actual).__name__] = menu_actual


    while menus["MenuCompraVehiculos"].active:
        menu_actual = menus["MenuCompraVehiculos"]
        piloto = menu_actual.piloto
        
        clear()
        print(menu_actual)
        user_input = menu_actual.recibir_input()
        menu_actual = menu_actual.go_to(user_input)
        if menu_actual:
            menus[type(menu_actual).__name__] = menu_actual
