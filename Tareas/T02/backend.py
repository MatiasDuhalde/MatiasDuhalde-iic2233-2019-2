"""
Este modulo contiene el backend de la ventana inicial
"""

import os
from PyQt5.QtCore import QObject, pyqtSignal
from mapa import Mapa


class BackendInicio(QObject):
    """
    Procesador de ventana de inicio.

    Señales:
     - path_signal : recibe un string conteniendo un path desde el frontend
     - feedback_signal : emite un string hacia el frontend, para actualizar el
                         label de feedback de este (self.feedback_label)
    """
    path_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.feedback_signal = None
        self.goto_signal = None
        self.path_signal.connect(self.get_file)

    def get_file(self, path_mapa):
        """
        Recibe un string con el path de la partida.

        Revisa los archivos dentro de mapas/, y maneja posibles sub-directorios
        dentro de dicha carpeta.

        Es posible que un archivo no posea extensión en algunos sistemas
        operativos, por lo que este método no chequea si el input tenga una.
        """
        path_mapa = path_mapa.strip()
        if "\\" in path_mapa:
            msg = "Path debe usar slash '/', no backslash '\\'"
            self.feedback_signal.emit(msg)
        elif path_mapa == "":
            msg = ""
            self.feedback_signal.emit(msg)
        else:
            path_mapa = ["mapas"] + path_mapa.split("/")
            try:
                with open(os.path.join(*path_mapa)) as archivo_mapa:
                    lista_mapa = []
                    for linea in archivo_mapa.read().splitlines():
                        lista_mapa.append(linea.split(" "))
                    mapa = Mapa(lista_mapa)
                    # procesar...
                    # Agregar error de formato en mapa
                    self.goto_signal.emit(mapa)

            except FileNotFoundError as err:
                msg = f"ERROR: {err.filename} no existe."
                self.feedback_signal.emit(msg)
