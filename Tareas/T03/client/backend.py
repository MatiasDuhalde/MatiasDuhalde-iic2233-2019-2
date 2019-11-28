"""
Funcionamiento de la parte de usuario del programa
"""
from PyQt5.QtCore import pyqtSignal, QObject

class Backend(QObject):
    """
    Esta clase maneja el funcionamiento del programa client-side

    Actúa como puente entre el frontend y el client.
    Hereda de QObject para poder emitir y conectar señales.
    """

    # Signals
    username_signal = pyqtSignal(str)

    def __init__(self):
        # El init simplemente maneja la declaración y conexión de las señales
        super().__init__()
        self.username_signal.connect(self.receive_username)
        self.feedback_signal = None

    def receive_username(self, username):
        """
        Recibe un username desde el frontend para ser enviado y analizado
        por el server.

        Parámetros:
         - username: nombre de usuario recibido desde el frontend

        Retorna un feedback legible al frontend en caso de ser necesario.

        TODO
        HANDLE USERNAME
        """
        return

        if username == "":
            msg = "El nombre no puede estar vacío."
        else:
            msg = f"ingresaste: {username}"
        if self.feedback_signal is None:
            raise NotImplementedError
        self.feedback_signal.emit(msg)
