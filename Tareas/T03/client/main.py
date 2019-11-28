"""
Main script del cliente.
"""
import sys
from PyQt5.QtWidgets import QApplication
from client import Client
from backend import Backend
from gui_inicio import VentanaInicio

if __name__ == '__main__':
    APP = QApplication([])

    CLIENT = Client()
    print("jaja")
    # Connect signal
    VENTANA_INICIO.username_signal = BACKEND.username_signal
    BACKEND.feedback_signal = VENTANA_INICIO.feedback_signal

    sys.exit(APP.exec_())
