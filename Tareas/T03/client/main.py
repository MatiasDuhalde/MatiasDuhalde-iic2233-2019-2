"""
Main script del cliente.
"""
import sys
from PyQt5.QtWidgets import QApplication
from gui_inicio import VentanaInicio
from client import Client

if __name__ == '__main__':
    app = QApplication([])
    ventana_inicio = VentanaInicio()
    client = Client()

    # Connect signal
    # ventana_inicio.username_signal = 

    sys.exit(app.exec_())
