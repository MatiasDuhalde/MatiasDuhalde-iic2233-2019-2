from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest


class Player(QObject):
    """
    Clase que se encargará de manejar los datos internos del personaje.
    Es parte del back-end del programa, al contener parte de la lógica.
    """

    update_character_signal = pyqtSignal(str)

    def __init__(self, x, y):
        super().__init__()
        # Datos iniciales
        self.direction = 'L'
        self._i = i # Y
        self._j = j # X

        # Se inicializa nula la señal de actualizar la interfaz
        self.update_window_signal = None

        # Se conecta la señal de actualizar datos del personaje
        self.update_character_signal.connect(self.move)

    def update_window_character(self):
        """
        Envía los datos del personaje mediante una señal a la
        interfaz para ser actualizados.
        :param position: str
        :return: None
        """
        if self.update_window_signal:
            self.update_window_signal.emit({
                'i': self.i,
                'j': self.j,
                'direction': self.direction,
                'position': position
            })

    @property
    def j(self):
        return self._j

    @j.setter
    def j(self, value):
        """
        Actualiza el valor de j del personaje y envía señal de
        actualización a la interfaz.
        :param value: int
        :return: None
        """
        if value > self._j:
            self.direction = 'U'
        elif value < self._j:
            self.direction = 'D'
        self._j = value
        self.update_window_character(direction)

    @property
    def i(self):
        return self._i

    @x.setter
    def i(self, value):
        """
        Chequea que la coordenada i se encuentre dentro los límites
        y envía la señal de actualización a la interfaz.
        :param value: int
        :return: None
        """
        if value > self._i:
            self.direction = 'R'
        elif value < self._i:
            self.direction = 'L'
        self._i = value
        self.update_window_character(direction)

    def move(self, event):
        """
        Función que maneja los eventos de movimiento desde la interfaz.
        :param event: str
        :return: None
        """
        if event == 'R':
            self.direction = 'R'
            self.x += 10
        elif event == 'L':
            self.direction = 'L'
            self.x -= 10
        elif event == 'Jump':
            self.jump()
        elif event == "Duck" and not self.is_ducked:
            self.is_ducked = True
        elif event == "Unduck":
            self.is_ducked = False

