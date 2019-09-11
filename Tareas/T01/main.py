from lib.funciones import clear
from lib.menu import MenuSesion, MenuPrincipal, MenuCarrera, \
    MenuCompraVehiculos, MenuPits, MenuPreparacionCarrera

# -----------------------------------------------------------------------------
#                                 GAME FLOW
# -----------------------------------------------------------------------------
menu_sesion = MenuSesion()
print(menu_sesion)
a = menu_sesion.recibir_input()
