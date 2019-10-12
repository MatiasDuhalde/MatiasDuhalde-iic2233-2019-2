import sys
import os
from functools import partial
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
    get_attribs_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tienda")
        self.tienda = WidgetTienda(self)

        # Signals
        self.t_to_p_signal = None
        self.p_to_t_signal.connect(self.show)
        self.volver_signal.connect(self.volver)
        self.tienda.volver_signal = self.volver_signal
        self.request_attribs_signal = None
        self.inventario_back_signal = None
        self.get_attribs_signal.connect(self.receive_attribs)
        self.init_gui()

    def receive_attribs(self, event):
        self.player_attribs = event

    def init_gui(self):
        self.setGeometry(800, 200, 0, 0)
        self.setCentralWidget(self.tienda)

    def volver(self):
        self.hide()
        self.t_to_p_signal.emit()

class WidgetTienda(QWidget):

    def __init__(self, container):
        super().__init__()
        self.precios = {
            "Azada" : PRECIO_AZADA,
            "Hacha" : PRECIO_HACHA,
            "SemillaChoclo" : PRECIO_SEMILLA_CHOCLOS,
            "SemillaAlcachofa" : PRECIO_SEMILLA_ALCACHOFAS,
            "Ticket" : PRECIO_TICKET,
            "Alcachofa" : PRECIO_ALACACHOFAS,
            "Choclo" : PRECIO_CHOCLOS,
            "Madera" : PRECIO_LEÑA,
            "Oro" : PRECIO_ORO
            }
        self.container = container
        self.volver_signal = None
        self.init_gui()

    def init_gui(self):
        # Font
        self.tienda_font_1 = QFont()
        self.tienda_font_1.setPixelSize(16)
        self.tienda_font_1.setBold(True)
        self.tienda_font_2 = QFont()
        self.tienda_font_2.setPixelSize(32)
        self.tienda_font_2.setBold(True)
        # Main Layout
        self.main_grid = QGridLayout()
        
        headers = [QLabel("Item", font=self.tienda_font_2), 
                   QLabel("Precio", font=self.tienda_font_2),
                   QLabel("Acción", font=self.tienda_font_2)]


        comprable = ["Azada", "Hacha", "SemillaChoclo", "SemillaAlcachofa", "Ticket"]
        vendible = ["Alcachofa", "Choclo", "Madera", "Oro"]

        # Comprable y vendible
        for index, header in enumerate(headers, start = 0):
            self.main_grid.addWidget(header, index, 0)
        for index, thing in enumerate(comprable, start = 1):
            icon_label = QLabel()
            pixmap = QPixmap(SPRITES_TIENDA[thing])
            icon_label.setPixmap(pixmap.scaled(50, 50))
            self.main_grid.addWidget(icon_label, 0, index)
            
            self.main_grid.addWidget(QLabel(f"${self.precios[thing]}", 
            font=self.tienda_font_1), 1, index)

            button_vbox = QVBoxLayout()
            boton_comprar = QPushButton("Comprar")
            boton_vender = QPushButton("Vender")
            boton_comprar.clicked.connect(partial(self.transaccion, thing, True))
            boton_vender.clicked.connect(partial(self.transaccion, thing, False))
            button_vbox.addWidget(boton_comprar)
            button_vbox.addWidget(boton_vender)

            self.main_grid.addLayout(button_vbox, 2, index)

        for index, thing in enumerate(vendible, start = len(comprable) + 1):
            icon_label = QLabel()
            pixmap = QPixmap(SPRITES_TIENDA[thing])
            icon_label.setPixmap(pixmap.scaled(50, 50))
            self.main_grid.addWidget(icon_label, 0, index)
            
            self.main_grid.addWidget(QLabel(f"${self.precios[thing]}", 
            font=self.tienda_font_1), 1, index)

            button_vbox = QVBoxLayout()
            boton_vender = QPushButton("Vender")
            boton_vender.clicked.connect(partial(self.transaccion, thing, False))
            button_vbox.addWidget(boton_vender)

            self.main_grid.addLayout(button_vbox, 2, index)

        self.boton_volver = QPushButton("Volver")
        self.boton_volver.clicked.connect(self.volver)

        self.main_grid.addWidget(self.boton_volver, 3, 0)
        self.setLayout(self.main_grid)

    def transaccion(self, thing, comprar):
        self.container.request_attribs_signal.emit()
        print(self.container.player_attribs)
        if comprar:
            if self.precios[thing] <= self.container.player_attribs["monedas"]:
                self.container.player_attribs["inventario"][thing] += 1
                self.container.player_attribs["monedas"] -= self.precios[thing]
            else:
                print("No se puede comprar este objeto")
        else:
            if self.container.player_attribs["inventario"][thing] >= 1:
                self.container.player_attribs["inventario"][thing] -= 1
                self.container.player_attribs["monedas"] += self.precios[thing]
            else:
                print("No se puede vender este objeto")
        self.container.inventario_back_signal.emit(self.container.player_attribs)

    def volver(self):
        self.volver_signal.emit()