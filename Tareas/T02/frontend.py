"""
Este modulo contiene el frontend del programa
"""

import sys
import os
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QLabel, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap
from backend import BackendInicio


# VENTANA DE INICIO
# VENTANA DE JUEGO
# TIENDA

class WidgetCargar(QWidget):
    """
    Widget central de la ventana de inicio.
    Conecta directamente con el backend a través de señales.
    También conecta con la ventana principal (MainGame), para iniciar el juego.

    Señales:
     - path_signal : emite un string conteniendo un path hacia el backend
     - feedback_signal : recibe un string desde backend, para actualizar el
                         label de feedback (self.feedback_label)
     -
    """
    feedback_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_signal = None
        self.feedback_signal.connect(self.update_feedback)
        self.init_gui()

    def init_gui(self):
        """
        Inicializa los elementos gráficos y funcionales del widget:
            - Imagen de título
            - Label de prompt
            - Input Line
            - Label de Error (feedback)
            - Push Button para iniciar
        """
        main_vbox = QVBoxLayout()
        main_vbox.addStretch(1)

        # Title image
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        ruta_imagen_titulo = os.path.join("sprites", "otros", "logo.png")
        self.imagen_titulo = QLabel()
        self.imagen_titulo.setPixmap(QPixmap(ruta_imagen_titulo))
        hbox.addWidget(self.imagen_titulo)
        hbox.addStretch(1)
        main_vbox.addLayout(hbox)

        # Label, texto, y botón
        grilla = QGridLayout()
        self.prompt = QLabel("Ingresa el archivo del mapa a cargar: ")
        self.input_path = QLineEdit("")
        self.boton_empezar = QPushButton("Jugar")
        self.boton_empezar.clicked.connect(self.enviar_path)

        grilla.addWidget(self.prompt, 0, 0)
        grilla.addWidget(self.input_path, 0, 1)
        grilla.addWidget(self.boton_empezar, 1, 1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(grilla)
        hbox.addStretch(1)
        main_vbox.addLayout(hbox)

        # Feedback Label
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.feedback_label = QLabel("")
        hbox.addWidget(self.feedback_label)
        hbox.addStretch(1)
        main_vbox.addLayout(hbox)

        main_vbox.addStretch(1)
        self.setLayout(main_vbox)

    def enviar_path(self):
        """
        Envía el path ingresado por el usuario en self.input_path al backend.
        """
        self.path_signal.emit(self.input_path.text())

    def update_feedback(self, texto):
        """
        Actualiza el mensaje de feedback, según lo enviado luego de
        self.enviar_path por el backend.
        """
        self.feedback_label.setText(texto)


class MainGame(QWidget):
    """
    Widget central de la ventana principal. Aquí se desarrolla el juego y se
    muestran los elementos gráficos.
    Conecta directamente con el backend a través de señales.
    También conecta con la ventana principal (MainGame), la ventana de tienda y
    la ventana de la casa.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Inicializa los elementos gráficos y funcionales del widget:
            - ...
            - ...
        """
        main_vbox = QVBoxLayout()

        self.label = QLabel("Testing")
        main_vbox.addWidget(self.label)
        self.setLayout(main_vbox)


class VenanaInicio(QMainWindow):
    """
    Main Window de la ventana de inicio.
    Funciona como base para tener consistencia con la estructura, no tiene
    función real aparte de contener al widget central (WidgetCargar)
    """
    goto_principal_signal = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Ventana de Carga")

        # Instancia ventana principal (para activar desde self.goto_principal)
        self.ventana_principal = None
        # Instanciar elementos
        self.ventana_cargar = WidgetCargar()
        self.backend = BackendInicio()
        # Conectar Señales
        self.goto_principal_signal.connect(self.goto_principal)
        self.backend.feedback_signal = self.ventana_cargar.feedback_signal
        self.ventana_cargar.path_signal = self.backend.path_signal
        self.backend.goto_signal = self.goto_principal_signal

        # Determina Tamaño y posición
        self.setGeometry(780, 415, 420, 250)

        # Agregar widget a Main Window
        self.setCentralWidget(self.ventana_cargar)

    def goto_principal(self):
        """
        Método ejecutado al cargar mapa correctamente desde backend.
        Esconde la ventana de inicio y abre la principal.
        """
        self.hide()
        self.ventana_principal.show()


class VentanaPrincipal(QMainWindow):
    """
    Main Window de la ventana principal.
    Funciona como base para tener consistencia con la estructura, no tiene
    función real aparte de contener al widget central (WidgetCargar)
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.juego = MainGame()
        self.setCentralWidget(self.juego)


if __name__ == '__main__':
    app = QApplication([])

    # Creación de ventanas
    ventana_inicio = VenanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_tienda = None

    # Conectar ventana inicio con ventana principal
    ventana_inicio.ventana_principal = ventana_principal

    # start
    ventana_inicio.show()

    sys.exit(app.exec_())
