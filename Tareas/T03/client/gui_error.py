"""
Interfaz gráfica de la ventana de error (sale en caso de desconexión con
servidor)
"""
from PyQt5.QtCore import pyqtSignal, Qt, QCoreApplication
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap
from parametros import PARAMETROS

class VentanaError(QWidget):
    """
    Ventana de error
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Inicializa la interfaz gráfica
        """
        self.setWindowTitle('Error')
        self.setGeometry(200, 200, 200, 80)

        # Logo
        path_logo = PARAMETROS["path"]["logo"]
        logo_pixmap = QPixmap(path_logo).scaled(100, 100, Qt.KeepAspectRatio)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Interactive
        self.error_label = QLabel('El servidor ha dejado de funcionar', self)
        self.close_button = QPushButton('Salir', self)
        self.close_button.clicked.connect(self.close_click)

        # Object Placement
        main_vbox = QVBoxLayout()
        main_vbox.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.logo)
        hbox1.addStretch(1)
        hbox1.addWidget(self.error_label)
        hbox1.addStretch(1)
        main_vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.close_button)
        hbox2.addStretch(1)
        main_vbox.addLayout(hbox2)
        main_vbox.addStretch(1)

        self.setLayout(main_vbox)

    def close_click(self):
        """
        Envía una señal al backend para enviar el nombre de usuario introducido
        al servidor.
        """
        self.hide()
        QCoreApplication.quit()
