import sys
from PyQt5.QtWidgets import QApplication
from ventana_inicio import VentanaInicio
from frontend import VentanaPrincipal
from ventana_tienda import VentanaTienda

if __name__ == '__main__':
    app = QApplication([])

    # Creación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_principal = VentanaPrincipal()
    ventana_tienda = VentanaTienda()

    # Conectar ventana inicio y tienda con ventana principal
    ventana_inicio.ventana_principal = ventana_principal
    ventana_principal.tienda = ventana_tienda

    # Conectar señal tienda
    ventana_principal.p_to_t_signal = ventana_tienda.p_to_t_signal
    ventana_tienda.t_to_p_signal = ventana_principal.t_to_p_signal

    # start
    ventana_inicio.show()

    sys.exit(app.exec_())