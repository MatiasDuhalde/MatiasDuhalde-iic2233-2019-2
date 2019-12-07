"""
Interfaz gráfica de la ventana de inicio (primera ventana)
"""

import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap

class VentanaChat(QWidget):
    """
    Representa la ventana de chat de la interfaz gráfica.
    Permite comunicarse con otros usuarios (clients) por medio de una interfaz
    de mensajería instantánea.
    """
    sendto_client_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self):
        """
        Inicializa la interfaz gráfica
        """
        self.setWindowTitle('DCCLUB')
        self.setGeometry(50, 50, 500, 500)

        # Logo
        path_logo = os.path.join('..', 'sprites', 'logo.png')
        logo_pixmap = QPixmap(path_logo)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Interactive

        # Object Placement
        main_vbox = QVBoxLayout()
        main_vbox.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.logo)
        hbox1.addStretch(1)
        main_vbox.addLayout(hbox1)


        self.setLayout(main_vbox)

    def handle_client(self, dict_):
        """
        Método conectado a señal, recibe diccionario desde el client
        """
        command = dict_["command"]
