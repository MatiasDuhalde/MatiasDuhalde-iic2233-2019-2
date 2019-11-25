import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout,
                             QVBoxLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap

class VentanaInicio(QWidget):
    """
    Representa la ventana de inicio de la interfaz gráfica.
    Permite iniciar sesión al usuario dado un nombre de usuario.

    Consideraciones del nombre de usuario:
     - Debe estar registrado en nombres.json
     - No debe haber otro usuario con el mismo nombre ya conectado
    """
    feedback_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username_signal = None
        self.feedback_signal.connect(self.update_feedback)
        self.init_gui()
        self.show()

    def init_gui(self):
        """
        Inicializa la interfaz gráfica
        """
        self.setWindowTitle('DCCLUB')
        self.setGeometry(50, 50, 500, 500)

        # Logo
        path_logo = os.path.join('sprites', 'personajes', 'robot', 'fallDown.png')
        logo_pixmap = QPixmap(path_logo)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Interactive
        self.prompt_label = QLabel('Nombre de usuario: ', self)
        self.text_box = QLineEdit(self)
        self.start_button = QPushButton('Iniciar Sesión', self)
        self.start_button.clicked.connect(self.boton_clickeado)
        self.feedback_label = QLabel(self)

        # Object Placement
        main_vbox = QVBoxLayout()
        main_vbox.addStretch(1)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.logo)
        hbox1.addStretch(1)
        main_vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.prompt_label)
        hbox2.addWidget(self.text_box)
        hbox2.addStretch(1)
        main_vbox.addLayout(hbox2)

        main_vbox.addSpacing(30)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.start_button)
        hbox3.addStretch(1)
        main_vbox.addLayout(hbox3)

        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(self.feedback_label)
        hbox4.addStretch(1)
        main_vbox.addLayout(hbox4)
        main_vbox.addStretch(1)

        self.setLayout(main_vbox)

    def update_feedback(self, msg):
        self.feedback_label.setText(msg)
