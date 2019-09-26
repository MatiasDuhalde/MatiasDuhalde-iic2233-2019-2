from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)


"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que enviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(200,300, 300,300)
        self.show()

    def actualizar_imagen(self):
        pass

    def keyPressEvent(self, event):
        """
        Este método maneja el evento que se produce al presionar las teclas.
        Muestra la última letra presionada.
        """
        #self. asdasd .setText(f'{event.text()}')
        self.label_letra.setText(event.text())
        self.label_letra.resize(self.label_letra.sizeHint())

    def recibir_senal(self, datos):
        self.datos = datos

        self.grilla = QGridLayout()

        self.label_letra = QLabel(self.datos["msg"], self)


        self.label_msg = QLabel('Ingresa una letra: ', self)

        self.label_letras_usadas = \
            QLabel(f'Letras usadas: \n{self.datos["usadas"]}', self)
        self.label_letras_disponibles = \
            QLabel(f'Letras disponibles: \n{self.datos["disponibles"]}', self)
        

        self.boton_enviar = QPushButton('Ingresar Letra', self)
        self.boton_nuevo = QPushButton('Nuevo Juego', self)

        self.imagen = QLabel(self)
        self.pixmap_imagen = QPixmap(self.datos["imagen"])
        self.imagen.setPixmap(self.pixmap_imagen)

        self.grilla.addWidget(self.imagen, *(0,0))
        self.grilla.addWidget(self.label_msg, *(1,0))
        self.grilla.addWidget(self.label_letra, *(4,0))
        self.grilla.addWidget(self.boton_enviar, *(5,0))
        self.grilla.addWidget(self.boton_nuevo, *(6,0))
        self.grilla.addWidget(self.label_letras_usadas, *(0,1))
        self.grilla.addWidget(self.label_letras_disponibles, *(1,1))


        vbox = QVBoxLayout()
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)
