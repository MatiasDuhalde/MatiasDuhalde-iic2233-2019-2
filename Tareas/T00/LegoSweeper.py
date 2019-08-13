from parametros import PROB_LEGO, POND_PUNT
from tablero import print_tablero
import random
import os
import math
import gametext
import sys

# =============================================================================
#                              MISC. FUNCTIONS
# =============================================================================


# LIMPIA LA PANTALLA, PARA HACER MEJOR LAS TRANSICIONES
# Snippet basado en respuesta de @popcnt en:
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")
    return None

# RECIBE UN INPUT ESTRICTAMENTE NUMÉRICO ENTRE DOS VALORES DADOS. ESPECIALMENTE
# ÚTIL EN LOS MENÚS
def get_int_input(a, b, prompt="Ingrese un número: ", accept_zero=False):
    n = input(prompt)
    if n.isdigit():
        n = int(n)
        if accept_zero and n == 0:
            return 0
        elif a <= n <= b:
            return n
        else:
            clear_screen()
            print("El número debe estar entre", str(a) , "y", str(b) + 
            " incluyéndolos.")
    else:
        clear_screen()
        return None
    return None

# ORGANIZA LA SCOREBOARD DE MANERA DESCENDIENTE
def sort_scoreboard():
    temp = []
    f = open("puntajes.txt", "r")
    for line in f:
        temp.append(line.split(","))
    f.close
    temp.sort(key=lambda x: int(x[1].rstrip()), reverse=True)
    f = open("puntajes.txt", "w")
    for line in temp:
        f.write(",".join(line))
    f.close
    return None


# =============================================================================
#                          BOARD HANDLING FUNCTIONS
# =============================================================================


# En el enunciado está implícito que se debe ocupar math.ceil para aproximar
# la cantidad de legos
def crear_tablero(largo, ancho):
    n_legos = math.ceil(largo * ancho * PROB_LEGO)
    pos_legos = random.sample(range(largo * ancho), n_legos)
    print(pos_legos)
    tablero = []
    for _ in range(largo):
        tablero.append([" "] * ancho)
    return tablero, pos_legos


# =============================================================================
#                             MENU FUNCTIONS
# =============================================================================

def menu_inicio():
    print(gametext.BRICKS)
    print(gametext.TITLE)
    end_cycle = False
    while not end_cycle:
        print(gametext.BRICKS)
        print(gametext.MAINMENU_OPTIONS)
        print(gametext.BRICKS)
        n = get_int_input(0,3)
        if n == 0:
            sys.exit(0)
        elif n in [1,2,3]:
            clear_screen()
            return n

def menu_nueva_partida():
    username = ""
    largo = ""
    ancho = ""
    status = 0
    while status != 4:
        print(gametext.BRICKS)
        print("{:>15}: {}\n{:>15}: {}\n{:>15}: {}\n{:>40}".format("JUGADOR", 
        username, "Largo", largo, "Ancho", ancho, "[0]  Salir"))
        print(gametext.BRICKS)

        if status == 0:
            username = input("Ingrese su nombre: ")
            if username == "0":
                break
            elif username != "":
                status = 1
                clear_screen()
            else:
                clear_screen()

        elif status == 1:
            largo = get_int_input(3, 15, "Ingrese el largo del tablero: ", 
            accept_zero=True)
            if largo == 0:
                break
            elif largo != None:
                status = 2
                clear_screen()
            else:
                largo = ""

        elif status == 2:
            ancho = get_int_input(3, 15, "Ingrese el ancho del tablero: ", 
            accept_zero=True)
            if ancho == 0:
                break
            elif ancho != None:
                status = 3
                clear_screen()
            else:
                ancho = ""
        elif status == 3:
            status = 4

    if status == 4:
        input("Presione ENTER para comenzar la partida...")
        clear_screen()
        return (username, largo, ancho)
    clear_screen()
    return None

def menu_cargar_partida():
    pass

def main_game(username, largo, ancho):
    tablero, pos_legos = crear_tablero(largo, ancho)
    print_tablero(tablero)

def scoreboard():
    clear_screen()
    print(gametext.BRICKS)
    print("{:^79}".format("PUNTAJES"))
    print(gametext.BRICKS)
    sort_scoreboard()
    f = open("puntajes.txt", "r")
    if len(list(f)) == 0:
        print("{:^79}".format("Aún no hay puntajes para mostrar..."))
    else:
        f.close()
        f = open("puntajes.txt", "r")
        print("{:^35}{}{:^35}".format("Nombre", gametext.MIDSEP1, "Puntos"))
        print("{:^79}".format(gametext.MIDSEP2))
        index = 1
        for line in f:
            if index == 11:
                break
            name, score = line.split(",")
            print("{:8d}.{:5}{:21.10}{}{:>20}".format(index, "", name, 
            gametext.MIDSEP1 if index % 2 == 1 else gametext.MIDSEP2, 
            score.rstrip()))
            index += 1
        print("{:^79}".format(
        gametext.MIDSEP1 if index % 2 == 1 else gametext.MIDSEP2))
    print(gametext.BRICKS)
    f.close()
    input("Presione ENTER para volver al menú principal...")
    clear_screen()
    return None


# =============================================================================
#                          
# =============================================================================


if __name__ == '__main__':
    
    # PREPROCESSING
    if not os.path.isfile("puntajes.txt"):
        f = open("puntajes.txt", "a+")
        f.close()
    if not os.path.exists("partidas"):
        os.mkdir("partidas")
    # END OF PREPROCESSING

    # GAME START
    main_cycle = True
    while main_cycle:
        user_choice = menu_inicio()
        
        if user_choice == 1:
            datos_juego = menu_nueva_partida()
            if datos_juego != None:
                main_game(*datos_juego)
    
        elif user_choice == 2:
            pass

        elif user_choice == 3:
            scoreboard()
