"""
Interfaz gráfica de la ventana principal
"""
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QGridLayout,
                             QVBoxLayout, QPushButton)
from PyQt5.QtGui import QPixmap
from parametros import PARAMETROS

class VentanaPrincipal(QWidget):
    """
    Representa la ventana de principal de la interfaz gráfica.
    """
    sendto_client_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.user = kwargs["user"]
        self._rooms = kwargs["rooms"]
        self.numero_salas = len(self.rooms)
        self.init_gui()
        self.show()

    @property
    def rooms(self):
        """
        Property que guarda una lista de instancias de Room
        """
        return self._rooms

    @rooms.setter
    def rooms(self, value):
        self._rooms = value
        self.update_counters()

    def init_gui(self):
        """
        Inicializa la interfaz gráfica
        """
        self.setWindowTitle('DCCLUB')
        self.setGeometry(50, 50, 500, 300)

        # Logo
        path_logo = PARAMETROS["path"]["logo"]
        logo_pixmap = QPixmap(path_logo).scaled(100, 100, Qt.KeepAspectRatio)
        self.logo = QLabel(self)
        self.logo.setPixmap(logo_pixmap)

        # Interactive
        amigos = f"\n\t\t\t".join([str(amigo) for amigo in self.user.amigos])
        user_info = (f"Nombre de usuario: \t{self.user.username}\n" + 
                     f"Amigos ({len(self.user.amigos)}): \t\t{amigos}")

        self.logout_button = QPushButton('Salir', self)
        self.logout_button.clicked.connect(self.logout_click)
        self.user_info_label = QLabel(user_info, self)
        self.salas_title_label = QLabel("Salas disponibles:", self)
        self.feedback_label = QLabel(self)
        self.counter_labels = []

        # Object Placement
        main_vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.logo)
        hbox1.addStretch(1)
        hbox1.addWidget(self.user_info_label)
        hbox1.addStretch(1)
        main_vbox.addLayout(hbox1)

        main_vbox.addSpacing(30)

        salas_grid_hbox = QHBoxLayout()
        self.salas_grid = QGridLayout()

        self.salas_grid.addWidget(self.salas_title_label, 0, 0)
        for index, sala in enumerate(self.rooms, start=1):
            nombre_sala_label = QLabel(f"Nombre: {sala.nombre}")
            usuarios_sala_label = QLabel(
                f"Usuarios conectados: {len(sala.usuarios_conectados)}/5")
            self.counter_labels.append(usuarios_sala_label)
            entrar_button = QPushButton("Entrar", self)
            entrar_button.clicked.connect(self.entrar_sala_wrapper(sala))
            self.salas_grid.addWidget(nombre_sala_label, index, 0)
            self.salas_grid.addWidget(usuarios_sala_label, index, 1)
            self.salas_grid.addWidget(entrar_button, index, 2)

        salas_grid_hbox.addStretch(1)
        salas_grid_hbox.addLayout(self.salas_grid)
        salas_grid_hbox.addStretch(1)
        main_vbox.addLayout(salas_grid_hbox)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.logout_button)
        hbox2.addStretch(1)
        main_vbox.addLayout(hbox2)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(self.feedback_label)
        hbox3.addStretch(1)
        main_vbox.addLayout(hbox3)

        main_vbox.addStretch(1)

        self.setLayout(main_vbox)

    def entrar_sala_wrapper(self, room):
        """
        Wrapper de la función de handling de clickeo del botón para entrar
        a una sala de chat. Esto así para poder ser usado via clicked.connect
        """
        def entrar_sala_click():
            """
            Envía una solicitud por medio de señales al client para luego
            llegar al server. Pide a este entrar a una sala de chat específica.
            """
            dict_ = {
                "command": "enter",
                "room": room
            }
            self.sendto_client_signal.emit(dict_)
        return entrar_sala_click

    def logout_click(self):
        """
        Envía una señal al client para hacer logout.
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
        if command == "logout":
            raise TypeError
        elif command == "access_granted":
            self.update_feedback("")
            self.sendto_client_signal.emit(dict_)
            self.hide()
        elif command == "access_denied":
            self.update_feedback(dict_["feedback"])
            self.sendto_client_signal.emit(dict_)

    def update_feedback(self, msg):
        """
        Cambia el valor del label de feedback, en caso de que no se haya
        haya admitido el nombre de usuario (ver casos arriba).
        """
        self.feedback_label.setText(msg)

    def update_counters(self):
        """
        Actualiza los contadores de los labels que indican cuantas personas
        hay en una sala. Se utiliza cada vez que se actualiza la property
        self.rooms
        """
        for room, label in zip(self.rooms, self.counter_labels):
            text = f"Usuarios conectados: {len(room.usuarios_conectados)}/5"
            label.setText(text)
