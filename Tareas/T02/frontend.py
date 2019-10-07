"""
Este modulo contiene el frontend del programa
"""

import sys
import os
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QHBoxLayout, QVBoxLayout, QGridLayout,
                             QLabel, QPushButton, QLineEdit)
from PyQt5.QtGui import (QPixmap, QColor)
from backend import BackendInicio


# VENTANA DE INICIO
# VENTANA DE JUEGO
# TIENDA

class WidgetCargar(QWidget):
    """
    Widget central de la ventana de inicio
    """
    update_signal = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.path_signal = None
        self.update_signal.connect(self.update_feedback)
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
        self.path_signal.emit(self.input_path.text())

    def update_feedback(self, texto):
        self.feedback_label.setText(texto)


class VenanaInicio(QMainWindow):
    """
    Main Window de la ventana de inicio
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Ventana de Juego")
        self.ventana_cargar = WidgetCargar()
        self.setCentralWidget(self.ventana_cargar)

        self.show()


if __name__ == '__main__':
    app = QApplication([])

    # Ventana de inicio
    backend_inicio = BackendInicio()
    ventana_inicio = VenanaInicio()
    backend_inicio.feedback_signal = ventana_inicio.ventana_cargar.update_signal
    ventana_inicio.ventana_cargar.path_signal = backend_inicio.path_signal

    ventana_principal = None
    ventana_tienda = None

    sys.exit(app.exec_())
