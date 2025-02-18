"""
Contiene constantes para usar en el juego, según el enunciado.
"""
import os

# Jugador
MONEDAS_INICIALES = 80    # Monedas con las que se parte
VEL_MOVIMIENTO = 30         # Pixeles avanzados por button press
ENERGIA_JUGADOR = 100      # Energía máxima
ENERGIA_DORMIR = 60       # Energía recuperada al dormir

# Generación
PROB_ARBOL = 0.01           # Probabilidad de aparición de un árbol
PROB_ORO = 0.5             # Probabilidad de aparición de oro

# Tiempo
# DEFINIR PARÁMETRO QUE CONTROLE QUE TAN RÁPIDO PASA EL TIEMPO (seccion 4.1)
DURACION_LENA = 20        # Duración de la leña antes de desaparecer
DURACION_ORO = 20         # Duración del oro antes de desaparecer

# Mapa
N = 30                      # Dimensión del tile en mapa

# Cheats
DINERO_TRAMPA = 100

# Pesca
LARGO_RECTANGULO = None     # Porcentaje, fracción del rectángulo verde 
LARGO_PESCADO = None        # Porcentaje, fracción del pescado respecto al rectángulo azul
VEL_PESCADO = None          # Velocidad de movimiento del pescado
TIEMPO_PESCADO = None       # Tiempo máximo para cambiar de sentido
PRECIO_PESCADO = None       # Dinero ganado por pescado capturado


TOP_OFFSET = 120 # Largo status bar

# Paths sprites


SPRITES_TIENDA = {
    'Azada' : os.path.join("sprites", "otros", "hoe.png"),
    'Hacha' : os.path.join("sprites", "otros", "axe.png"),
    'SemillaChoclo' : os.path.join("sprites", "cultivos", "choclo", "seeds.png"),
    'SemillaAlcachofa' : os.path.join("sprites", "cultivos", "alcachofa", "seeds.png"),
    'Alcachofa' : os.path.join("sprites", "recursos", "artichoke.png"),
    'Choclo' : os.path.join("sprites", "recursos", "corn.png"),
    'Madera' : os.path.join("sprites", "recursos", "wood.png"),
    'Oro' : os.path.join("sprites", "recursos", "gold.png"),
    'Ticket' : os.path.join("sprites", "otros", "ticket.png")
}

SPRITES_ALCACHOFA = {
    1 : os.path.join("sprites", "cultivos", "alcachofa", "stage_1.png"),
    2 : os.path.join("sprites", "cultivos", "alcachofa", "stage_2.png"),
    3 : os.path.join("sprites", "cultivos", "alcachofa", "stage_3.png"),
    4 : os.path.join("sprites", "cultivos", "alcachofa", "stage_4.png"),
    5 : os.path.join("sprites", "cultivos", "alcachofa", "stage_5.png"),
    6 : os.path.join("sprites", "cultivos", "alcachofa", "stage_6.png")
}

SPRITES_CHOCLO = {
    1 : os.path.join("sprites", "cultivos", "choclo", "stage_1.png"),
    2 : os.path.join("sprites", "cultivos", "choclo", "stage_2.png"),
    3 : os.path.join("sprites", "cultivos", "choclo", "stage_3.png"),
    4 : os.path.join("sprites", "cultivos", "choclo", "stage_4.png"),
    5 : os.path.join("sprites", "cultivos", "choclo", "stage_5.png"),
    6 : os.path.join("sprites", "cultivos", "choclo", "stage_6.png"),
    7 : os.path.join("sprites", "cultivos", "choclo", "stage_7.png")  # Cultivado
}

SPRITE_INVENTARIO = os.path.join("sprites", "otros", "invetary_template.jpg")
SPRITE_WINDOW = os.path.join("sprites", "otros", "window_template.jpg")

SPRITES_PLAYER = {
    'U1' : os.path.join("sprites", "personaje", "up_1.png"),
    'U2' : os.path.join("sprites", "personaje", "up_2.png"),
    'U3' : os.path.join("sprites", "personaje", "up_3.png"),
    'U4' : os.path.join("sprites", "personaje", "up_4.png"),
    'D1' : os.path.join("sprites", "personaje", "down_1.png"),
    'D2' : os.path.join("sprites", "personaje", "down_2.png"),
    'D3' : os.path.join("sprites", "personaje", "down_3.png"),
    'D4' : os.path.join("sprites", "personaje", "down_4.png"),
    'R1' : os.path.join("sprites", "personaje", "right_1.png"),
    'R2' : os.path.join("sprites", "personaje", "right_2.png"),
    'R3' : os.path.join("sprites", "personaje", "right_3.png"),
    'R4' : os.path.join("sprites", "personaje", "right_4.png"),
    'L1' : os.path.join("sprites", "personaje", "left_1.png"),
    'L2' : os.path.join("sprites", "personaje", "left_2.png"),
    'L3' : os.path.join("sprites", "personaje", "left_3.png"),
    'L4' : os.path.join("sprites", "personaje", "left_4.png")
}


SPRITES_MAPA = {
    'O9' : [os.path.join("sprites", "mapa", "tile036.png")],
    'O8' : [os.path.join("sprites", "mapa", "tile037.png"),
            os.path.join("sprites", "mapa", "tile041.png"),
            os.path.join("sprites", "mapa", "tile034.png")],
    'O7' : [os.path.join("sprites", "mapa", "tile039.png")],
    'O6' : [os.path.join("sprites", "mapa", "tile042.png")],
    'O5' : [os.path.join("sprites", "mapa", "tile000.png"),
            os.path.join("sprites", "mapa", "tile001.png"),
            os.path.join("sprites", "mapa", "tile002.png"),
            os.path.join("sprites", "mapa", "tile006.png"),
            os.path.join("sprites", "mapa", "tile028.png"),
            os.path.join("sprites", "mapa", "tile029.png")],
    'O4' : [os.path.join("sprites", "mapa", "tile045.png")],
    'O3' : [os.path.join("sprites", "mapa", "tile048.png")],
    'O2' : [os.path.join("sprites", "mapa", "tile040.png"),
            os.path.join("sprites", "mapa", "tile046.png"),
            os.path.join("sprites", "mapa", "tile047.png"),
            os.path.join("sprites", "mapa", "tile049.png")],
    'O1' : [os.path.join("sprites", "mapa", "tile051.png")],
    'O10' : [os.path.join("sprites", "mapa", "tile033.png")],
    'O12' : [os.path.join("sprites", "mapa", "tile050.png")],
    'O16' : [os.path.join("sprites", "mapa", "tile032.png")],
    'O18' : [os.path.join("sprites", "mapa", "tile038.png")],
    'O19' : [os.path.join("sprites", "mapa", "tile052.png"),
             os.path.join("sprites", "mapa", "tile053.png")],
    'R' : [os.path.join("sprites", "mapa", "tile030.png"),
           os.path.join("sprites", "mapa", "tile087.png")],
    'C' : [os.path.join("sprites", "mapa", "tile031.png"),
           os.path.join("sprites", "mapa", "tile043.png"),
           os.path.join("sprites", "mapa", "tile044.png")],
    'H' : [os.path.join("sprites", "mapa", "house.png")],
    'T' : [os.path.join("sprites", "mapa", "store.png")]
    }

"""
SPRITES:
    Casa                house.png
    Tienda              store.png
    Espacio libre       tile000.png (type 5)
                        tile001.png (type 5)
                        tile002.png (type 5)
                        tile006.png (type 5)
                        tile028.png (type 5)
                        tile029.ong (type 5)

                        tile036.png (type 1)

                        tile037.png (type 2)
                        tile041.png (type 2)
                        tile034.png (type 2)

                        tile039.png (type 3)

                        tile042.png (type 4)

                        tile045.png (type 6)

                        tile048.png (type 7)

                        tile040.png (type 8)
                        tile046.png (type 8)
                        tile047.png (type 8)
                        tile049.png (type 8)

                        tile051.png (type 9)

                        tile033.png (type 10)

                        tile050.png (type 12)

                        tile032.png (type 16)

                        tile038.png (type 18)

                        tile052.png (type 19)
                        tile053.png (type 19)


    Espacio Cultivable  tile031.png
                        tile043.png
                        tile044.png

    Piedra              tile030.png
                        tile087.png

    Discarded           tile007-027
                        tile035.png
                        tile052.png
                        tile053.png
                        tile054-086

Tipos:
         1 | 2 | 3
        ___|___|___
         4 | 5 | 6
        ___|___|___
         7 | 8 | 9
           |   |

"""
