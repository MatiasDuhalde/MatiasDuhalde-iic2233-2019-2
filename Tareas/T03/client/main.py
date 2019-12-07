"""
Main script del cliente.
"""
import sys
from PyQt5.QtWidgets import QApplication
from client import Client

if __name__ == '__main__':
    while True:
        APP = QApplication([])
        CLIENT = Client()

        APP.exec_()
        del APP
        if CLIENT.forced_exit:
            print("yeet")
            app = QApplication([])
            CLIENT.ventana_error.show()
            app.exec_()
            del app
        if not CLIENT.reset:
            break
        del CLIENT
