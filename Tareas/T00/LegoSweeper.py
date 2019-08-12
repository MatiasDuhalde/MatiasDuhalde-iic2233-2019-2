from parametros import PROB_LEGO, POND_PUNT
from tablero import print_tablero
import os
import math
import random
import gametext
import sys

# LIMPIA LA PANTALLA, PARA HACER MEJOR LAS TRANSICIONES
def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")
    return None

# RECIBE UN INPUT ESTRICTAMENTE NUMÉRICO ENTRE DOS VALORES DADOS. ESPECIALMENTE
# ÚTIL EN LOS MENÚS
def get_int_input(a, b ,prompt="Ingrese un número: ", acceptZero=False):
    n = input(prompt)
    if n.isdigit():
        n = int(n)
        if acceptZero and n == 0:
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


def menu_inicio():
    print(gametext.BRICKS)
    print(gametext.TITLE)
    endCycle = False
    while not endCycle:
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
            acceptZero=True)
            if largo == 0:
                break
            elif largo != None:
                status = 2
                clear_screen()
            else:
                largo = ""

        elif status == 2:
            ancho = get_int_input(3, 15, "Ingrese el ancho del tablero: ", 
            acceptZero=True)
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
        return True
    return False

def menu_cargar_partida():
    pass

def main_game():
    pass

def scoreboard():
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
        index = 0
        for line in f:
            name, score = line.split(",")
            print("{:14}{:21.10}{}{:>20}".format("", name, 
            gametext.MIDSEP1 if index%2 == 0 else gametext.MIDSEP2, 
            score.rstrip()))
            index += 1
        print("{:^79}".format(
        gametext.MIDSEP1 if index%2 == 1 else gametext.MIDSEP2))
    print(gametext.BRICKS)
    f.close()
    input("Presione ENTER para volver al menú principal...")
    clear_screen()
    return None


if __name__ == '__main__':
    # PREPROCESSING
    if not os.path.isfile("puntajes.txt"):
        f = open("puntajes.txt", "a+")
        f.close()
    if not os.path.exists("partidas"):
        os.mkdir("partidas")
    # END OF PREPROCESSING

    # GAME START
    mainCycle = True
    while mainCycle:
        userChoice = menu_inicio()
        
        if userChoice == 1:
            success = menu_nueva_partida()
            if success:
                main_game()
    
        elif userChoice == 2:
            pass

        elif userChoice == 3:
            scoreboard()
