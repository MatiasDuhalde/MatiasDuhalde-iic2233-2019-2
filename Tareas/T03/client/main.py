"""
Main script del cliente.
"""
import sys
from PyQt5.QtWidgets import QApplication
from client import Client

if __name__ == '__main__':
    APP = QApplication([])
    CLIENT = Client()

    sys.exit(APP.exec_())
