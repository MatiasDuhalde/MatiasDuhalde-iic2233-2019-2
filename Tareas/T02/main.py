import sys
from PyQt5.QtWidgets import QApplication
from ventana_inicio import VentanaInicio
from frontend import VentanaPrincipal

if __name__ == '__main__':
    app = QApplication([])

    # Creación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_tienda = None

    # Conectar ventana inicio con ventana principal
    ventana_inicio.ventana_principal = ventana_principal

    # start
    ventana_inicio.show()

    sys.exit(app.exec_())