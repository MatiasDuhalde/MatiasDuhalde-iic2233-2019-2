from parametros import PROB_LEGO, POND_PUNT
from tablero import print_tablero
import gametext
import random
import os
import math
import sys

# FUTURE FEATURES:
# Easter eggs
# Add highscore to in game screen
# Prevent user from losing in first reveal
# maybe do something to prevent exploiting load/save feature

# =============================================================================
#                          BOARD HANDLING FUNCTIONS
# =============================================================================

class Tablero:

    def __init__(self, largo, ancho, legos = [], rev = 0, tab = []):
        # use defaults to autogen, specify to load a game
        self.largo = largo
        self.ancho = ancho
        self.legos = legos.copy()
        self.reveladas = rev

        self.tablero = tab.copy()
        if self.tablero == []:
            for _ in range(largo):
                self.tablero.append([" "] * ancho)
        
        if self.legos == []:
            n_legos = math.ceil(largo * ancho * PROB_LEGO)
            self.legos = random.sample(range(largo * ancho), n_legos)

    def pos_to_num(self, fil, col):
        return self.ancho * fil + col

    def num_to_pos(self, num):
        # retorna (fil, col)
        return (num // self.ancho, num % self.ancho)
    
    # coloca L's en el tablero
    def reveal_legos(self):
        for i in self.legos:
            coords = self.num_to_pos(i)
            self.tablero[coords[0]][coords[1]] = "L"

    def lego_in_tile(self, fil, col):
        if self.pos_to_num(fil, col) in self.legos:
            return True
        return False
    
    # True si están todas las casillas reveladas (menos las con lego)
    def check_comp(self):
        if self.reveladas == self.ancho * self.largo - len(self.legos):
            return True
        return False
    
    # retorna num de legos adyacentes a la casilla deseada
    def adj_legos(self, fil, col):
        legos_found = 0
        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if 0 <= n + fil < self.largo and 0 <= m + col < self.ancho:
                    num = self.pos_to_num(n + fil, m + col)
                    if num in self.legos:
                        legos_found += 1
        return legos_found

    # revisa si la casilla elegida tiene un lego o ya fue revelada
    def check_tile(self, fil, col):
        if self.lego_in_tile(fil, col):
            self.reveal_legos()
            return "L"
        elif fil >= self.largo or col >= self.ancho:
            print("Esta casilla no se encuentra en el tablero.")
        elif self.tablero[fil][col] != " ":
            print("Esta casilla ya ha sido revelada. Intenta con otra.")
        else: 
            self.reveladas += 1
            self.tablero[fil][col] = self.adj_legos(fil, col)
            if self.tablero[fil][col] == 0:
                self.auto_reveal(fil, col)

    # corresponde al bonus, revela tiles adyacentes con solo un comando.
    def auto_reveal(self, fil, col):
        if self.tablero[fil][col] == 0:
            for n in [-1, 0, 1]:
                for m in [-1, 0, 1]:
                    if 0 <= n + fil < self.largo and 0 <= m + col < self.ancho:
                        if self.tablero[n + fil][m + col] == " ":
                            self.tablero[n + fil][m + col] = \
                                self.adj_legos(n + fil, m + col)
                            self.reveladas += 1
                            if self.tablero[n + fil][m + col] == 0: 
                                self.auto_reveal(n + fil, m + col)



    # guarda la partida en partidas/username.txt
    def guardar(self, username):
        f = open("partidas/" + username + ".txt", "w")
        
        # username
        print(username, file = f)
        # dimensions
        print(self.largo, self.ancho, sep = ",", file = f)
        # legos csv
        print(*self.legos, sep = ",", file = f)
        # reveladas
        print(self.reveladas, file = f)
        # filas esc, cols csv
        for fila in self.tablero:
            print(*fila, sep = ",", file = f)
        
        f.close()
        print(gametext.BRICKS)
        print("{:^79}".format("La partida ha sido guardada."))
        print(gametext.BRICKS)
        input("Presione ENTER para continuar...")

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

# Rechaza strings largos y con caracteres que generan conflictos al usarlos en
# directorios.
def get_str_input():
    banned_chr = ["/", "\\", "?", "%", "*", ":", "|", "\"", "<", ">", ".", " "]
    a = input("Ingrese su nombre: ")
    if a == "":
        clear_screen()
    if len(a) > 20:
        clear_screen()
        print("Tu nombre no puede tener más de 20 caracteres.")
        return ""
    for i in a:
        if i in banned_chr:
            clear_screen()
            print("Tu nombre no puede contener espacios ni los siguientes caracteres:")
            print(" ".join(banned_chr))
            return ""
    return a
    
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

def end_screen(tablero, username, score, win=False):
    print(gametext.BRICKS)
    if not win:
        print(gametext.LOSE_TEXT)
    else:
        print(gametext.WIN_TEXT)
    print(gametext.BRICKS)
    tablero.reveal_legos()
    tablero.show()
    print(gametext.BRICKS)
    print("{:^35}{:^9}{:^35}".format("JUGADOR", gametext.MIDSEP1, "PUNTOS"))
    print("{:^35}{:^9}{:^35}".format(username, gametext.MIDSEP2, score))
    print(gametext.BRICKS)
    f = open("puntajes.txt", "a")
    f.write(username + "," + str(score) + "\n")
    f.close()
    input("Presione ENTER para volver al menú principal...")
    clear_screen()


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
            username = get_str_input()
            if username == "0":
                break
            elif username != "":
                status = 1
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


# Carga datos según archivos guardados en el directorio partidas/
def menu_cargar_partida():
    load_loop = True
    while load_loop:
        print(gametext.BRICKS)
        print("{:^79}".format("CARGAR PARTIDA"))
        print(gametext.BRICKS)
        print(gametext.LEGOBRICK)
        print("{:>15}    {}".format("[0]", "Volver"))
        print(gametext.BRICKS)
        username = get_str_input()
        if username == "0":
            load_loop = False
            break
        if username + ".txt" in os.listdir("partidas/"):
            f = open("partidas/" + username + ".txt", "r")
            
            username = f.readline().rstrip("\n")
            largo, ancho = map(int, f.readline().rstrip("\n").split(","))
            legos = list(map(int, f.readline().rstrip("\n").split(",")))
            reveladas = int(f.readline().rstrip("\n"))
            tablero = []
            for _ in range(largo):
                tablero.append((f.readline().rstrip("\n")).split(","))
            
            f.close()
            clear_screen()
            return username, largo, ancho, legos, reveladas, tablero
        elif username != "":
            clear_screen()
            print("No existen partidas guardadas para el usuario " + username + ".")
        
    clear_screen()
    return None


def main_game(username, largo, ancho, legos = [], reveladas = 0, tablero = []):
    t = Tablero(largo, ancho, legos, reveladas, tablero)
    score = 0
    game_cycle = True
    while game_cycle:
        score = t.reveladas * len(t.legos) * POND_PUNT
        print(gametext.BRICKS)
        print("{:^35}{:^9}{:^35}".format("JUGADOR", gametext.MIDSEP1, "PUNTOS"))
        print("{:^35}{:^9}{:^35}".format(username, gametext.MIDSEP2, score))
        print(gametext.BRICKS)
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
                    clear_screen()
                    exit_cycle = False
                    game_cycle = False
                elif exit_choice == 2:
                    exit_cycle = False
                    game_cycle = False
                elif exit_choice == 0:
                    exit_cycle = False
            clear_screen()
        
        elif user_choice == "1":
            clear_screen()
            t.guardar(username)
            clear_screen()
        
        elif "-" in user_choice:
            clear_screen()
            coords = user_choice.split("-")
            if len(coords) == 2 and coords[1].isdigit() and \
                coords[0].isalpha() and len(coords[0]) == 1:
                col = ord(coords[0].lower()) - 97
                fil = int(coords[1])
                tile = t.check_tile(fil, col)
                
                if tile == "L":
                    end_screen(t, username, score)
                    game_cycle = False
                
                if t.check_comp():
                    end_screen(t, username, score, win=True)
                    game_cycle = False
        
        elif user_choice.isdigit() and not 0 <= int(user_choice) <= 1:
            clear_screen()
            print("El número debe estar entre 0 y 1 incluyéndolos.")
        else:
            clear_screen()
    return username, score, t


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
            print("{:8d}.{:5}{:21.16}{}{:>20}".format(index, "", name, 
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
            datos_juego = menu_cargar_partida()
            if datos_juego != None:
                print(gametext.BRICKS)
                print("{:^79}".format("PARTIDA CARGADA CON ÉXITO!"))
                print(gametext.BRICKS)
                input("Presione ENTER para continuar...")
                clear_screen()
                main_game(*datos_juego)
        elif user_choice == 3:
            scoreboard()
