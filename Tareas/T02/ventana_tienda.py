import sys
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QMainWindow, QWidget, QLabel, QGridLayout,
                             QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap, QFont
from parametros_generales import SPRITES_TIENDA
from parametros_precios import (PRECIO_ALACACHOFAS, PRECIO_CHOCLOS, 
                                PRECIO_LEÑA, PRECIO_ORO, 
                                PRECIO_SEMILLA_ALCACHOFAS,
                                PRECIO_SEMILLA_CHOCLOS, PRECIO_HACHA, 
                                PRECIO_AZADA, PRECIO_TICKET)


class VentanaTienda(QMainWindow):

    p_to_t_signal = pyqtSignal()
    volver_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.t_to_p_signal = None
        self.p_to_t_signal.connect(self.show)
        self.volver_signal.connect(self.volver)

        self.tienda = WidgetTienda()
        self.tienda.volver_signal = self.volver_signal
        self.init_gui()

    def init_gui(self):
        self.setGeometry(300, 200, 400, 400)
        self.setCentralWidget(self.tienda)

    def volver(self):
        self.hide()
        self.t_to_p_signal.emit()

class WidgetTienda(QWidget):

    def __init__(self):
        super().__init__()
        self.volver_signal = None
        self.init_gui()

    def init_gui(self):
        # Font
        self.tienda_font_1 = QFont()
        self.tienda_font_1.setPixelSize(50)
        self.tienda_font_1.setBold(True)
        self.tienda_font_2 = QFont()
        self.tienda_font_2.setPixelSize(32)
        self.tienda_font_2.setBold(True)
        # Main Layout
        self.main_grid = QGridLayout()

        self.label_titulo = QLabel("Tienda")
        self.label_titulo.setFont(self.tienda_font_1)
        self.main_grid.addWidget(self.label_titulo, 1, 0)
        headers = [QLabel("Item", font=self.tienda_font_2), 
                   QLabel("Precio", font=self.tienda_font_2),
                   QLabel("Acción", font=self.tienda_font_2)]
        comprable = ["Azada", "Hacha", "SemillaChoclo", "SemillaAlcachofa", "Ticket"]
        vendible = ["Alcachofa", "Choclo", "Madera", "Oro"]

        # Comprable y vendible
        for headers, index in enumerate(headers, start = 0):
            self.main_grid.addWidget(header, index, 1)
        for thing, index in enumerate(comprable, start = 2):
            pixmap = QPixmap(SPRITES_TIENDA[thing])
            self.main_grid.addWidget(pixmap.scaled(50, 50), 0, index)
            self.main_grid.addWidget(QLabel(f"${PRECIO_AZADA}"))
            vbox = QVBoxLayout()
            vbox.addWidget()
        
        # Solo vendible
        # for thing, index in enumerate(["Azada", "Hacha", "SemillaChoclo", "S"], start = 0):

        self.boton_volver = QPushButton("Volver")
        self.boton_volver.clicked.connect(self.volver)

        self.main_grid.addWidget(self.boton_volver, 2, 2)
        self.setLayout(self.main_grid)

    def volver(self):
        self.volver_signal.emit()