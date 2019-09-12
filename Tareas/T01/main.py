from lib.funciones import clear
from lib.menu import MenuSesion, MenuPrincipal, MenuCarrera, \
    MenuCompraVehiculos, MenuPits, MenuPreparacionCarrera
import time

# -----------------------------------------------------------------------------
#                                 GAME FLOW
# -----------------------------------------------------------------------------

menus = {}
main_loop = True

menu_sesion = MenuSesion()
menu_actual = menu_sesion
menus[type(menu_actual).__name__] = menu_actual

while main_loop:
    
    sesion_loop = True
    while sesion_loop:
        print(menu_sesion)
        
        user_input = menu_sesion.recibir_input()
        piloto = None
        if user_input == 1:
            piloto = menu_sesion.nueva_partida()
        elif user_input == 2:
            piloto = menu_sesion.cargar_partida()
        if piloto:
            sesion_loop = False
            menu_actual = menu_sesion.go_to(user_input)(piloto)
            print(type(menu_actual))
            menus[type(menu_actual).__name__] = menu_actual

    principal_loop = True
    while principal_loop:
        clear()
        p = menu_actual.piloto
        print(p.nombre, p.vehículos)

        print(menu_actual)
        user_input = menu_actual.recibir_input()

        principal_loop = False
    
    main_loop = False


