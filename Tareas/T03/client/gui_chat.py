"""
Interfaz gráfica de la ventana de inicio (primera ventana)
"""
import random
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLineEdit, QTextEdit)
from PyQt5.QtGui import QPixmap
from parametros import PARAMETROS

class VentanaChat(QWidget):
    """
    Representa la ventana de chat de la interfaz gráfica.
    Permite comunicarse con otros usuarios (clients) por medio de una interfaz
    de mensajería instantánea.
    """
    sendto_client_signal = pyqtSignal(dict)

    def __init__(self, room, user, *args, **kwargs):
        super().__init__()
        self.room = room
        self.user = user
        self.init_gui()
        self.show()

    def init_gui(self):
        """
        Inicializa la interfaz gráfica
        """
        self.setWindowTitle(self.room.nombre)
        self.setGeometry(50, 50, 700, 650)
        self.setFixedSize(700, 650)

        # Logo
        path_logo = PARAMETROS["path"]["logo"]
        logo_pixmap = QPixmap(path_logo)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Fondo
        path_fondo = random.choice(PARAMETROS["path"]["fondos"])
        fondo_pixmap = QPixmap(path_fondo).scaled(700, 300)
        self.fondo = QLabel(self)
        self.fondo.setPixmap(fondo_pixmap)

        # Screen
        self.text_screen = QTextEdit(self)
        self.text_screen.setReadOnly(True)
        self.text_screen.move(5, 305)
        self.text_screen.setFixedSize(690, 245)

        # Line Input
        self.line_input = QLineEdit(self)
        self.line_input.setFixedSize(525, 25)
        self.line_input.move(5, 555)
        self.line_input.returnPressed.connect(self.enter_text_input)

        # Enter Button
        self.enter_button = QPushButton("Enter", self)
        self.enter_button.move(550, 555)
        self.enter_button.setFixedSize(145, 25)
        self.enter_button.clicked.connect(self.enter_text_input)

        # Exit button
        self.exit_button = QPushButton("Salir", self)
        self.exit_button.move(300, 600)
        self.exit_button.clicked.connect(self.exit_click)
        # Interactive

        # Object Placement
        self.fondo.move(0, 0)

        # main_vbox = QVBoxLayout()
        # main_vbox.addStretch(1)

        # hbox1 = QHBoxLayout()
        # hbox1.addStretch(1)
        # hbox1.addWidget(self.logo)
        # hbox1.addStretch(1)
        # main_vbox.addLayout(hbox1)


        # self.setLayout(main_vbox)

    def handle_client(self, dict_):
        """
        Método conectado a señal, recibe diccionario desde el client
        """
        command = dict_["command"]
        if command == "receive_message":
            self.display_message(dict_["text"])

    def exit_click(self):
        dict_ = {
            "command": "exit_room",
            "text": self.line_input.text(),
            "room": self.room,
        }
        exit()


    def enter_text_input(self):
        if self.line_input.text().strip() != "":
            dict_ = {
                "command": "enter_text",
                "text": self.line_input.text(),
                "room": self.room,

            }
            self.sendto_client_signal.emit(dict_)
        self.line_input.clear()

    def display_message(self, text):
        self.text_screen.append(text)
