import sys
from PyQt5.QtWidgets import QApplication
from gui_inicio import VentanaInicio

if __name__ == '__main__':
    app = QApplication([])
    form = VentanaInicio()
    sys.exit(app.exec_())
