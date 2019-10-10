"""
Este módulo incluye la clase Mapa, además de todas las funciones para el
manejo de sus instancias:
"""
from random import choice
from abc import ABC, abstractmethod
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QGridLayout, QLabel
from PyQt5.QtGui import QPixmap, QPainter
from parametros_generales import SPRITES_MAPA, N

class Tile(QObject):
    """
    Objeto tile. Corresponde a un QLabel
    """
    @abstractmethod
    def __init__(self, pos, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i = pos[0]
        self.j = pos[1]
        self.base_label = None


class Libre(Tile):
    """
    Tile tipo 'O'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'O'
        super().__init__(pos, *args, *kwargs)
        

class Cultivable(Tile):
    """
    Tile tipo 'C'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'C'
        super().__init__(pos, *args, *kwargs)


class Piedra(Tile):
    """
    Tile tipo 'R'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'R'
        super().__init__(pos, *args, *kwargs)
        self.label = None


class Tienda(Tile):
    """
    Tile tipo 'T'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'T'
        super().__init__(pos, *args, *kwargs)
        self.label = None


class Casa(Tile):
    """
    Tile tipo 'H'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'H'
        super().__init__(pos, *args, *kwargs)
        self.label = None


class Mapa(QObject):
    """
    Objeto mapa, contiene el layout de este y sus elementos.

    Elementos:
     - O : Espacio libre
     - C : Espacio cultivable
     - R : Piedra
     - H : Casa
     - T : Tienda
    """

    tile_types = {
        'O' : Libre,
        'C' : Cultivable,
        'R' : Piedra,
        'H' : Casa,
        'T' : Tienda
    }

    def __init__(self, mapa):
        """
        Recibe como parámetro lista con las filas del mapa.
        """
        super().__init__()
        self.mapa = mapa # Lista de listas, forma de matriz
        self.largo = len(self.mapa) # max Y
        self.ancho = len(self.mapa[0]) # max X

    def get_map_grid(self):
        """
        Retorna grid que contiene las tiles del mapa.
        """
        grilla_mapa = QGridLayout()
        grilla_mapa.setHorizontalSpacing(0)
        grilla_mapa.setVerticalSpacing(0)
        grid_top = []
        for i in range(self.largo):
            for j in range(self.ancho):
                tile_type = self.mapa[i][j]
                tile = self.tile_types[tile_type]((i, j))

                tile_base_label = QLabel()
                tile_base_pixmap = QPixmap(choice(SPRITES_MAPA[self.get_tipo(i, j)]))
                tile_base_label.setPixmap(tile_base_pixmap.scaled(N,N))
                # Put label in class
                tile.base_label = tile_base_label
                # Put label in grid
                grilla_mapa.addWidget(tile.base_label, i, j)

                if not tile_type in ['O', 'C']:
                    if (tile_type in ['H', 'T'] and 
                        (i < (self.largo - 1) and j < (self.ancho - 1))):
                        if (self.mapa[i][j] == self.mapa[i + 1][j] == 
                            self.mapa[i][j + 1] == self.mapa[i + 1][j + 1]):
                            tile_label = QLabel()
                            tile_pixmap = QPixmap(choice(SPRITES_MAPA[tile_type]))
                            tile_label.setPixmap(tile_pixmap.scaled(N*2,N*2))
                            # Put label in class
                            tile.label = tile_label
                            # Put label in grid
                            grid_top.append((tile.label, i, j, i + 1, j + 1))
                                

                    else:
                        tile_label = QLabel()
                        tile_pixmap = QPixmap(choice(SPRITES_MAPA[tile_type]))
                        tile_label.setPixmap(tile_pixmap.scaled(N,N))
                        # Put label in class
                        tile.label = tile_label
                        # Put label in grid
                        grilla_mapa.addWidget(tile.label, i, j)
        for element in grid_top:
            grilla_mapa.addWidget(*element)
                
        return grilla_mapa

    def get_tipo(self, fil, col):
        # Bugeada para casos específicos, como checked pattern o 5 y 4 adj cult
        adjacent = self.get_adjacent_matrix(fil, col)
        t_adjacent = list(zip(*adjacent))
        cant_cultivable = [element for sublist in adjacent for element in sublist].count('C')
        if adjacent[1][1] == 'C':
            return 'C'
        elif cant_cultivable == 0:
            return 'O5'
        elif cant_cultivable >= 6:
            return 'O19'
        elif cant_cultivable == 1:
            if adjacent[0][0] == 'C':
                return 'O1'
            elif adjacent[0][2] == 'C':
                return 'O3'
            elif adjacent[2][0] == 'C':
                return 'O7'
            elif adjacent[2][2] == 'C':
                return 'O9'
        if (('C' in adjacent[0] and 'C' in adjacent[1])):
            if adjacent[0][0] == adjacent[0][1] == adjacent[1][0] == 'C':
                return 'O10'
            elif adjacent[0][2] == adjacent[0][1] == adjacent[1][2] == 'C':
                return 'O12'
        elif (('C' in adjacent[2] and 'C' in adjacent[1])):
            if adjacent[1][0] == adjacent[2][0] == adjacent[2][1] == 'C':
                return 'O16'
            elif adjacent[1][2] == adjacent[2][1] == adjacent[2][2] == 'C':
                return 'O18'
        if (('C' in adjacent[0] and not 'C' in adjacent[1])):
            return 'O2'
        elif (('C' in adjacent[2] and not 'C' in adjacent[1])):
            return 'O8'
        elif (('C' in t_adjacent[0] and not 'C' in t_adjacent[1])):
            return 'O4'
        elif (('C' in t_adjacent[2] and not 'C' in t_adjacent[1])):
            return 'O6'
        return 'O19'

    def get_adjacent_matrix(self, fil, col):
        adjacent = [[None, None, None],
                    [None, None, None],
                    [None, None, None]]
        for n in [-1, 0, 1]:
            for m in [-1, 0, 1]:
                if 0 <= n + fil < self.largo and 0 <= m + col < self.ancho:
                    adjacent[n + 1][m + 1] = self.mapa[n + fil][m + col]
        return adjacent
