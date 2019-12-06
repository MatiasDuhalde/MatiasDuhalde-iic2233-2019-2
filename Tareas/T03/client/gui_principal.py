"""
Interfaz gráfica de la ventana principal
"""

import os
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap

class VentanaPrincipal(QWidget):
    """
    Representa la ventana de principal de la interfaz gráfica.
    """
    sendto_client_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.user = kwargs["user"]
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
        logo_pixmap = QPixmap(path_logo).scaled(32, 32, Qt.KeepAspectRatio)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Interactive
        user_info = f"Nombre de usuario: {self.user.username}\nAmigos:"

        self.logout_button = QPushButton('Salir', self)
        self.logout_button.clicked.connect(self.logout_click)
        self.user_info_label = QLabel(user_info, self)

        # Object Placement
        main_vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.logo)
        hbox1.addStretch(1)
        main_vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.user_info_label)
        hbox2.addStretch(1)
        main_vbox.addLayout(hbox2)

        main_vbox.addSpacing(30)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.logout_button)
        hbox3.addStretch(1)
        main_vbox.addLayout(hbox3)
        main_vbox.addStretch(1)

        self.setLayout(main_vbox)


    def logout_click(self):
        """
        Envía una señal al backend para enviar el nombre de usuario introducido
        al servidor.
        """
        dict_ = {
            "command": "logout"
        }
        self.hide()
        self.sendto_client_signal.emit(dict_)


    def handle_client(self, dict_):
        """
        Método conectado a señal, recibe diccionario desde el client
        """
        command = dict_["command"]
