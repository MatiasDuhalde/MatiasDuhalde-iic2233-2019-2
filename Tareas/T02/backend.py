"""
Este modulo contiene el backend del programa
"""

import os
from PyQt5.QtCore import QObject, pyqtSignal


class BackendInicio(QObject):
    """
    asd
    """

    path_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.feedback_signal = None
        self.path_signal.connect(self.get_file)

    def get_file(self, path_mapa):
        """
        Recibe un string con el path de la partida.

        Revisa los archivos dentro de mapas/, y maneja posibles sub-directorios
        dentro de dicha carpeta.

        Es posible que un archivo no posea extensión en algunos sistemas
        operativos, por lo que este método no chequea si el input tenga una.
        """
        if "\\" in path_mapa:
            msg = "Path debe usar slash '/', no backslash '\\'"
            self.feedback_signal.emit(msg)
        else:
            path_mapa = ["mapas"] + path_mapa.split("/")
            try:
                with open(os.path.join(*path_mapa)) as mapa:
                    pass
                    # procesar...
                    # Agregar error de formato en mapa

            except FileNotFoundError as err:
                msg = f"ERROR: {err.filename} no existe."
                self.feedback_signal.emit(msg)
