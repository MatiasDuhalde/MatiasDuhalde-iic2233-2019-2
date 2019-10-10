"""
Contiene constantes para usar en el juego, según el enunciado.
"""
import os

# Jugador
MONEDAS_INICIALES = None    # Monedas con las que se parte
VEL_MOVIMIENTO = None       # Pixeles avanzados por button press
ENERGIA_JUGADOR = None      # Energía máxima
ENERGIA_DORMIR = None       # Energía recuperada al dormir

# Generación
PROB_ARBOL = None           # Probabilidad de aparición de un árbol
PROB_ORO = None             # Probabilidad de aparición de oro

# Tiempo
# DEFINIR PARÁMETRO QUE CONTROLE QUE TAN RÁPIDO PASA EL TIEMPO (seccion 4.1)
DURACION_LENA = None        # Duración de la leña antes de desaparecer
DURACION_ORO = None         # Duración del oro antes de desaparecer

# Mapa
N = 30                      # Dimensión del tile en mapa

# Pesca
LARGO_RECTANGULO = None     # Porcentaje, fracción del rectángulo verde respecto al rectángulo azul
LARGO_PESCADO = None        # Porcentaje, fracción del pescado respecto al rectángulo azul
VEL_PESCADO = None          # Velocidad de movimiento del pescado
TIEMPO_PESCADO = None       # Tiempo máximo para cambiar de sentido
PRECIO_PESCADO = None       # Dinero ganado por pescado capturado

# Paths sprites

SPRITE_INVENTARIO = os.path.join("sprites", "otros", "invetary_template.jpg")
SPRITE_WINDOW = os.path.join("sprites", "otros", "window_template.jpg")


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
