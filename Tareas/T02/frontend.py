"""
Este modulo contiene el frontend del programa
"""

import sys
import os
from time import sleep
from PyQt5.QtCore import pyqtSignal, Qt, QThread, QMutex
from PyQt5.Qt import QTest
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QVBoxLayout, QProgressBar,
                             QLabel, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap, QFont
from backend import BackendInicio
from mapa import Mapa
from player import Player
from parametros_generales import (N, SPRITES_PLAYER, SPRITE_WINDOW,
                                  SPRITE_INVENTARIO, TOP_OFFSET, 
                                  MONEDAS_INICIALES, ENERGIA_JUGADOR)

# -----------------------------------------------------------------------------
#                              VENTANA DE JUEGO
# -----------------------------------------------------------------------------

class VentanaPrincipal(QMainWindow):
    """
    Main Window de la ventana principal.
    Funciona como base para tener consistencia con la estructura, no tiene
    función real aparte de contener al widget central (Maingame)
    """

    t_to_p_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("DCCAMPO")

        # Signal handling
        self.p_to_t_signal = None
        self.t_to_p_signal.connect(self.show)

    def init_window(self, mapa):
        self.mapa = mapa
        self.juego = MainGame(self.mapa)
        # Max X
        self.ancho_ventana = max(N*self.mapa.ancho, 600)
        # Max Y
        self.largo_ventana = max(N*self.mapa.largo + TOP_OFFSET + 200, 0)
        self.init_gui()


    def init_gui(self):
        """
        Inicializa los elementos gráficos y funcionales del widget.
        """
        # Prepara layout inicial
        self.setGeometry(300, 200, self.ancho_ventana, self.largo_ventana)
        self.setFixedSize(self.ancho_ventana, self.largo_ventana)
        self.setCentralWidget(self.juego)

    key_event_dict = {
        Qt.Key_D : 'R',
        Qt.Key_A : 'L',
        Qt.Key_W : 'U',
        Qt.Key_S : 'D'
    }

    def keyPressEvent(self, event):
        """
        Dada la presión de una tecla se llama a esta función. Al
        apretarse una tecla chequeamos si está dentro de las teclas del
        control del juego y de ser así, se envía una señal al backend
        con la acción además de actualizar el sprite.
        :param event: QKeyEvent
        :return: None
        """
        if event.key() in self.key_event_dict and not event.isAutoRepeat():
            action = self.key_event_dict[event.key()]
            self.juego.update_character_signal.emit(action)


class MainGame(QWidget):
    """
    Widget central de la ventana principal. Aquí se desarrolla el juego y se
    muestran los elementos gráficos.
    """

    update_window_signal = pyqtSignal(dict)

    def __init__(self, mapa, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Map stuff
        self.mapa = mapa
        # Player stuff
        self.player = Player(TOP_OFFSET - 15, N) # Y, X
        self.player_label = None
        self.current_sprite = None
        # Map stuff
        self.mapa.inicializar_map_layout(self)
        self.init_gui()
        self.init_player_visuals()

        # Connecting signals
        self.update_window_signal.connect(self.move_player)
        self.player.update_window_signal = self.update_window_signal
        self.update_character_signal = self.player.update_character_signal

    def init_gui(self):
        """
        Inicializa los elementos gráficos y funcionales del widget:
            - ...
            - ...
        """

        # Status Bar
        self.status_bar = QLabel(self)
        self.setGeometry(0, 0, 600, TOP_OFFSET)
        self.status_bar.setFixedSize(600, TOP_OFFSET)
        status_bar_pixmap = QPixmap(SPRITE_WINDOW)
        self.status_bar.setPixmap(status_bar_pixmap)
        self.status_bar.setScaledContents(True)
        
        # Status Bar Elements

        # Fuente general
        self.status_font_1 = QFont()
        self.status_font_1.setPixelSize(20)
        self.status_font_1.setBold(True)

        # Tiempo
        self.label_dia = QLabel("Dia: 1", self)
        self.label_dia.move(20, 10)
        self.label_hora = QLabel("Hora: 12:00", self)
        self.label_hora.move(20, 80)
        self.label_dia.setFont(self.status_font_1)
        self.label_hora.setFont(self.status_font_1)

        # Energía
        self.label_energia = QLabel("Energía: ", self)
        self.label_energia.move(160, 10)
        self.label_energia.setFont(self.status_font_1)
        self.barra_energia = QProgressBar(self)
        self.barra_energia.setGeometry(260, 10, 200, 25)
        self.barra_energia.setMaximum(ENERGIA_JUGADOR)
        self.barra_energia.setValue(ENERGIA_JUGADOR)

        # Dinero
        self.label_dinero = QLabel(f"Dinero: ${MONEDAS_INICIALES}", self)
        self.label_dinero.move(160, 80)
        self.label_dinero.setFont(self.status_font_1)

        # Botones
        self.exit_button = QPushButton("Salir", self)
        self.exit_button.setGeometry(460, 10, 100, 25)
        self.exit_button.clicked.connect(sys.exit)
        self.pause_button = QPushButton("Pausa", self)
        self.pause_button.setGeometry(460, 80, 100, 25)
        self.pause_button.clicked.connect(print)



        # Inventario
        self.inventory = QLabel(self)
        self.inventory.setGeometry(0, TOP_OFFSET + self.mapa.largo*N, 600, 200)
        self.inventory.setFixedSize(600, 200)
        inventory_pixmap = QPixmap(SPRITE_INVENTARIO)
        self.inventory.setPixmap(inventory_pixmap)
        self.inventory.setScaledContents(True)


    def init_player_visuals(self):
        self.player_label = QLabel(self)
        self.current_sprite = QPixmap(SPRITES_PLAYER['D1'])
        self.player_label.setPixmap(self.current_sprite)
        self.player_label.move(N, TOP_OFFSET - 15) # 


    def move_player(self, event):
        """
        Función que recibe un diccionario con la información del
        personaje y las actualiza en el front-end.
        """
        if event['direction'] in ['R', 'L']:
            if event['direction'] == 'R':
                dir_ = 1
                sprites = self.player.r_pool
            else:
                dir_ = -1
                sprites = self.player.l_pool
            for j in range(event['old_j'], event['j'] + 1, dir_):
                self.current_sprite = QPixmap(SPRITES_PLAYER[next(sprites)])
                self.player_label.setPixmap(self.current_sprite)
                self.player_label.move(j, event['i'])
                self.player_label.raise_()
                QTest.qWait(5)
        elif event['direction'] in ['U', 'D']:
            if event['direction'] == 'D':
                dir_ = 1
                sprites = self.player.d_pool
            else:
                dir_ = -1
                sprites = self.player.u_pool
            for i in range(event['old_i'], event['i'] + 1, dir_):
                self.current_sprite = QPixmap(SPRITES_PLAYER[next(sprites)])
                self.player_label.setPixmap(self.current_sprite)
                self.player_label.move(event['j'], i)
                self.player_label.raise_()
                QTest.qWait(5)


# -----------------------------------------------------------------------------
#                                 TIENDA
# -----------------------------------------------------------------------------