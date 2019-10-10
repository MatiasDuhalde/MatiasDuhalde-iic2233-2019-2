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


class Tile(QLabel):
    """
    Objeto tile. Corresponde a un QObject. Contiene labels
    """
    def __init__(self, pos, pixmap_base, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.i = pos[0]
        self.j = pos[1]
        self.setFixedSize(N, N)
        self.pixmap_base = pixmap_base


class Libre(Tile):
    """
    Tile tipo 'O'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'O'
        super().__init__(pos, *args, *kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(0,0), self.pixmap_base.scaled(N, N))
        painter.end()
    
    def mousePressEvent(self, event):
        pass

class Cultivable(Tile):
    """
    Tile tipo 'C'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'C'
        super().__init__(pos, *args, *kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(0,0), self.pixmap_base.scaled(N, N))
        painter.end()

    def mousePressEvent(self, event):
        pass

class Piedra(Tile):
    """
    Tile tipo 'R'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'R'
        super().__init__(pos, *args, *kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        self.pixmap_objeto = QPixmap(choice(SPRITES_MAPA[self.tipo]))
        painter.drawPixmap(QPoint(0,0), self.pixmap_base.scaled(N, N))
        painter.drawPixmap(QPoint(0,0), self.pixmap_objeto.scaled(N, N))
        painter.end()

    def mousePressEvent(self, event):
        pass

class Tienda(Tile):
    """
    Tile tipo 'T'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'T'
        super().__init__(pos, *args, *kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(0,0), self.pixmap_base.scaled(N, N))
        painter.end()


class Casa(Tile):
    """
    Tile tipo 'H'
    """
    def __init__(self, pos, *args, **kwargs):
        self.tipo = 'H'
        super().__init__(pos, *args, *kwargs)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(0,0), self.pixmap_base.scaled(N, N))
        painter.end()



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
        house_found = False
        store_found = False
        for i in range(self.largo):
            for j in range(self.ancho):
                tile_type = self.mapa[i][j]
                pixmap_base = QPixmap(choice(SPRITES_MAPA[self.get_tipo(i,j)]))
                tile = self.tile_types[tile_type]((i, j), pixmap_base)
                grilla_mapa.addWidget(tile, i, j)
                if tile_type == 'H' and not house_found:
                    coords_house = (i, j)
                    print(coords_house)
                    house_found = True
                if tile_type == 'T' and not store_found:
                    coords_store = (i, j)
                    store_found = True
        label_casa = QLabel()
        label_casa.setFixedSize(2*N, 2*N)
        pixmap_casa = QPixmap(choice(SPRITES_MAPA['H']))
        label_casa.setPixmap(pixmap_casa.scaled(2*N, 2*N))
        i, j = coords_house
        grilla_mapa.addWidget(label_casa, i, j, 2, 2)

        label_store = QLabel()
        label_store.setFixedSize(2*N, 2*N)
        pixmap_store = QPixmap(choice(SPRITES_MAPA['T']))
        label_store.setPixmap(pixmap_store.scaled(2*N, 2*N))
        i, j = coords_store
        grilla_mapa.addWidget(label_store, i, j, 2, 2)
        
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
