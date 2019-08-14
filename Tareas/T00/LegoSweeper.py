from parametros import PROB_LEGO, POND_PUNT
from tablero import print_tablero
import random
import os
import math
import gametext
import sys

# NEXT FEATURES:
# Add highscore to in game screen
# Prevent user from losing in first reveal

# =============================================================================
#                          BOARD HANDLING FUNCTIONS
# =============================================================================

let_to_num = {} 


class Tablero:

    def __init__(self, largo, ancho, legos = []):
        self.largo = largo
        self.ancho = ancho
        self.legos = legos

        self.tablero = []
        for _ in range(largo):
            self.tablero.append([" "] * ancho)
        
        if self.legos == []:
            n_legos = math.ceil(largo * ancho * PROB_LEGO)
            self.legos = random.sample(range(largo * ancho), n_legos)

    def pos_to_num(self, fil, col):
        return self.ancho * fil + col

    def num_to_pos(self, num):
        # (fil, col)
        return (num // self.ancho, num % self.ancho)
    
    def lego_in_tile(self, fil, col):
        if self.pos_to_num(fil, col) in self.legos:
            return True
        return False

    def check_tile(self, fil, col):
        if self.lego_in_tile(fil, col):
            self.reveal_legos()
            return "L"
        else: 
            # COMPLETAR
            pass
    
    def reveal_legos(self):
        for i in self.legos:
            coords = self.num_to_pos(i)
            self.tablero[coords[0]][coords[1]] = "L"

    # COMPLETAR
    # COMPLETAR
    # COMPLETAR
    def guardar(self, username):
        pass

    def show(self):
        print_tablero(self.tablero)




# =============================================================================
#                              MISC. FUNCTIONS
# =============================================================================

# Limpia la pantalla, para hacer mejores las transiciones
# Snippet basado en respuesta de @popcnt en:
# https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
def clear_screen():
    _ = os.system("cls" if os.name == "nt" else "clear")
    return None

# Recibe un input estrictamente numérico (entero) entre 2 otros enteros.
# Opcionalmente recibe también el cero. Rechaza no-enteros o fuera de rango.
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

# Organiza la scoreboard de manera descendiente
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
        username, "Largo", largo, "Ancho", ancho, "[0]  Volver"))
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
        return (username, largo, ancho)
    clear_screen()
    return None


#PENDIENTE
#PENDIENTE
#PENDIENTE
#PENDIENTE
def menu_cargar_partida():
    print(gametext.BRICKS)
    print(gametext.LEGOBRICK)
    print("{:>15}    {}".format("[0]", "Volver"))
    print(gametext.BRICKS)
    username = input("\nInserte su nombre: ")
    if username != "0":
        pass
    clear_screen()

#PENDIENTE
#PENDIENTE
#PENDIENTE
#PENDIENTE
def main_game(username, largo, ancho):
    t = Tablero(largo, ancho)
    score = 0
    game_cycle = True
    while game_cycle:
        clear_screen()
        print(gametext.BRICKS)
        print("{:^35}{:^9}{:^35}".format("JUGADOR", gametext.MIDSEP1, "PUNTOS"))
        print("{:^35}{:^9}{:^35}".format(username, gametext.MIDSEP2, score))
        print(gametext.BRICKS)
        print(t.legos)
        t.show()
        print(gametext.BRICKS)
        print(gametext.GAMEMENU_OPTIONS)
        print(gametext.BRICKS)
        user_choice = input("Ingrese un comando: ")

        if user_choice == "0":
            exit_cycle = True
            clear_screen()
            while exit_cycle:
                print(gametext.BRICKS)
                print(gametext.EXITPROMPT_OPTIONS)
                print(gametext.BRICKS)
                exit_choice = get_int_input(0, 2)
                if exit_choice == 1:
                    clear_screen()
                    t.guardar(username)
                    exit_cycle = False
                    game_cycle = False
                elif exit_choice == 2:
                    exit_cycle = False
                    game_cycle = False
                elif exit_choice == 0:
                    exit_cycle = False
            clear_screen()
        
        elif user_choice == "1":
            t.guardar(username)
        
        elif "-" in user_choice:
            coords = user_choice.split("-")
            if len(coords) == 2 and coords[1].isdigit() and \
                coords[0].isalpha() and len(coords[0]) == 1:
                col = ord(coords[0].lower()) - 97
                fil = int(coords[1])
                tile = t.check_tile(fil, col)
                if tile == "L":
                    game_cycle = False
    return username, score, t
                
def end_screen(username, score, tablero):
    pass


# Muestra primeros 10 puntajes guardados en puntajes.txt
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
                username, score, tablero = main_game(*datos_juego)
                end_screen(username, score, tablero)
        elif user_choice == 2:
            menu_cargar_partida()

        elif user_choice == 3:
            scoreboard()
