from itertools import cycle
from PyQt5.QtCore import QObject, pyqtSignal
from parametros_generales import N, VEL_MOVIMIENTO


class Player(QObject):
    # Código basado en ayudantía extra

    update_character_signal = pyqtSignal(str)

    def __init__(self, i, j):
        super().__init__()
        # Datos iniciales
        self.direction = 'R'
        self._i = i # Y
        self._j = j # X
        self.u_pool = cycle(['U1', 'U2', 'U3', 'U4'])
        self.r_pool = cycle(['R1', 'R2', 'R3', 'R4'])
        self.d_pool = cycle(['D1', 'D2', 'D3', 'D4'])
        self.l_pool = cycle(['L1', 'L2', 'L3', 'L4'])


        # Signals init and connect
        self.update_window_signal = None
        self.update_character_signal.connect(self.move)

    def update_window_character(self, old_i, old_j):
        """
        Envía los datos del personaje a frontend
        """
        if self.update_window_signal:
            self.update_window_signal.emit({
                'i': self.i,
                'j': self.j,
                'old_i' : old_i,
                'old_j' : old_j,
                'direction': self.direction,
            })

    @property
    def j(self):
        return self._j

    @j.setter
    def j(self, value):
        """
        Actualiza j y llama a update_window_character
        """
        # Check if character in map
        if value > self._j:
            self.direction = 'R'
        elif value < self._j:
            self.direction = 'L'
        old_i = self._i
        old_j = self._j
        self._j = value
        self.update_window_character(old_i, old_j)

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, value):
        """
        Actualiza i y llama a update_window_character
        """
        # Check if character in map
        if value > self._i:
            self.direction = 'D'
        elif value < self._i:
            self.direction = 'U'
        old_i = self._i
        old_j = self._j
        self._i = value
        self.update_window_character(old_i, old_j)

    def move(self, event):
        if event == 'R':
            self.direction = 'R'
            self.j += VEL_MOVIMIENTO
        elif event == 'L':
            self.direction = 'L'
            self.j -= VEL_MOVIMIENTO
        elif event == 'U':
            self.direction = 'U'
            self.i -= VEL_MOVIMIENTO
        elif event == 'D':
            self.direction = 'U'
            self.i += VEL_MOVIMIENTO

