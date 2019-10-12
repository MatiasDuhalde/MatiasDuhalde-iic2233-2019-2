"""
Este módulo incluye la clase Mapa, además de todas las funciones para el
manejo de sus instancias:
"""
from random import choice
from abc import ABC, abstractmethod
from PyQt5.QtCore import QObject, Qt, QPoint
from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QPainter
from parametros_generales import SPRITES_MAPA, N, SPRITE_INVENTARIO, SPRITE_WINDOW


class BaseTile(QLabel):
    """
    Objeto tile. Corresponde a un QObject. Contiene labels
    """
    def __init__(self, pos, size, top_offset, parent, *args, **kwargs):
        self.parent = parent
        super().__init__(parent, *args, **kwargs)
        self.i = pos[0]
        self.j = pos[1]
        self.top_offset = top_offset
        self.setGeometry(N*self.j, N*self.i + top_offset, size, size)
        self.setFixedSize(size, size)


class Libre(BaseTile):
    """
    Tile tipo 'O'
    """
    def __init__(self, pos, top_offset, pixmap, parent, *args, **kwargs):
        self.tipo = 'O'
        # Tiene pixmap porque distintos tipos hacen variar sprite
        size = N
        super().__init__(pos, size, top_offset, parent, *args, *kwargs)
        self.setPixmap(pixmap)
    
    def mousePressEvent(self, event):
        # Check for hoe
        if event.button() == Qt.LeftButton:
            new_tile = Cultivable((self.i, self.j), self.top_offset, self.parent)
            new_tile.raise_()
            new_tile.show()

class Cultivable(BaseTile):
    """
    Tile tipo 'C'
    """
    def __init__(self, pos, top_offset, parent, *args, **kwargs):
        self.tipo = 'C'
        size = N
        super().__init__(pos, size, top_offset, parent, *args, *kwargs)
        pixmap = QPixmap(choice(SPRITES_MAPA[self.tipo])).scaled(N, N)
        self.setPixmap(pixmap)


class Piedra(BaseTile):
    """
    Tile tipo 'R'
    """
    def __init__(self, pos, top_offset, parent, *args, **kwargs):
        self.tipo = 'R'
        size = N
        super().__init__(pos, size, top_offset, parent, *args, *kwargs)
        pixmap = QPixmap(choice(SPRITES_MAPA[self.tipo])).scaled(N, N)
        self.setPixmap(pixmap)


class Tienda(BaseTile):
    """
    Tile tipo 'T'
    """
    def __init__(self, pos, top_offset, parent, *args, **kwargs):
        self.tipo = 'T'
        size = 2*N
        super().__init__(pos, size, top_offset, parent, *args, *kwargs)
        pixmap = QPixmap(choice(SPRITES_MAPA[self.tipo])).scaled(2*N, 2*N)
        self.setPixmap(pixmap)
        self.raise_()


class Casa(BaseTile):
    """
    Tile tipo 'H'
    """
    def __init__(self, pos, top_offset, parent, *args, **kwargs):
        self.tipo = 'H'
        size = 2*N
        super().__init__(pos, size, top_offset, parent, *args, *kwargs)
        pixmap = QPixmap(choice(SPRITES_MAPA[self.tipo])).scaled(2*N, 2*N)
        self.setPixmap(pixmap)
        self.raise_()


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

    def __init__(self, mapa, top_offset = 80):
        """
        Recibe como parámetro lista con las filas del mapa.
        """
        super().__init__()
        self.mapa = mapa # Lista de listas, forma de matriz
        self.largo = len(self.mapa) # max Y
        self.ancho = len(self.mapa[0]) # max X
        self.top_offset = top_offset
        self.game_widget = None

    def inicializar_map_layout(self, parent):
        self.game_widget = parent
        house_count = 0
        store_count = 0
        store_detected = False
        for i in range(self.largo):
            for j in range(self.ancho):
                tile_type = self.mapa[i][j]
                pixmap = QPixmap(choice(SPRITES_MAPA[self.get_tipo(i, j)])).scaled(N, N)
                if tile_type == 'C':
                    Cultivable((i, j), self.top_offset, self.game_widget)
                else:
                    Libre((i, j), self.top_offset, pixmap, self.game_widget)
                if tile_type == "R":
                    self.tile_types[tile_type]((i, j), self.top_offset, self.game_widget)
                elif tile_type == "H":
                    house_count += 1
                    if house_count == 4:
                        house_count += 1
                        self.tile_types[tile_type]((i-1, j-1), self.top_offset, 
                        self.game_widget)
                elif tile_type == "T":
                    store_count += 1
                    if store_count == 4:
                        store_count += 1
                        self.tile_types[tile_type]((i-1, j-1), self.top_offset, 
                        self.game_widget)




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


class Inventario(QLabel):
    
    def __init__(self, ancho):
        super().__init__()
        self.ancho = ancho
        self.init_gui()
        
    def init_gui(self):
        self.base_pixmap = QPixmap(SPRITE_INVENTARIO)
        self.setPixmap(self.base_pixmap.scaled(self.ancho, self.ancho, Qt.KeepAspectRatio))


class StatusBar(QLabel):

    def __init__(self, ancho):
        super().__init__()
        self.ancho = ancho
        self.init_gui()
        
    def init_gui(self):
        self.base_pixmap = QPixmap(SPRITE_WINDOW)
        self.setPixmap(self.base_pixmap.scaled(self.ancho, 80))
