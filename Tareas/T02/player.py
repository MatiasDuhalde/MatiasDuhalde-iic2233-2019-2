from itertools import cycle
from PyQt5.QtCore import QObject, pyqtSignal
from parametros_generales import (N, VEL_MOVIMIENTO, MONEDAS_INICIALES,
                                  ENERGIA_JUGADOR, DINERO_TRAMPA)


class Player(QObject):
    # Código basado en ayudantía extra

    update_character_signal = pyqtSignal(str)
    cheat_signal = pyqtSignal(str)

    def __init__(self, i, j):
        super().__init__()
        # Datos iniciales
        self.direction = 'R'
        self._i = i # Y
        self._j = j # X
        self._monedas = MONEDAS_INICIALES
        self._energia = ENERGIA_JUGADOR
        self.inventario = []

        # Signals init and connect
        self.update_window_signal = None
        self.update_status_labels_signal = None
        self.update_character_signal.connect(self.move)
        self.cheat_signal.connect(self.cheat_code)

        self.create_sprite_pools()


    @property
    def monedas(self):
        return self._monedas

    @monedas.setter
    def monedas(self, value):
        if value < 0:
            print("what")
        self._monedas = value
        self.update_status_labels_signal.emit({
            'dinero' : self._monedas,
            'energia' : self._energia
        })

    @property
    def energia(Self):
        return self._energia

    @energia.setter
    def energia(self, value):
        if value < 0:
            print("what")
        self._energia = value
        self.update_status_labels_signal.emit({
            'dinero' : self._monedas,
            'energia' : self._energia
        })

    def cheat_code(self, event):
        if event == "KIP":
            self.energia = ENERGIA_JUGADOR
        elif event == "MNY":
            self.monedas += DINERO_TRAMPA


    #--------------------------------------------------------------------------
    #                  Movement Methods and Properties
    #--------------------------------------------------------------------------
    def create_sprite_pools(self):
        self.u_pool = cycle(['U1', 'U2', 'U3', 'U4'])
        self.r_pool = cycle(['R1', 'R2', 'R3', 'R4'])
        self.d_pool = cycle(['D1', 'D2', 'D3', 'D4'])
        self.l_pool = cycle(['L1', 'L2', 'L3', 'L4'])

    def update_window_character(self):
        """
        Envía los datos del personaje a frontend
        """
        if self.update_window_signal:
            self.update_window_signal.emit({
                'i': self.i,
                'j': self.j,
                'direction': self.direction
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
        self._j = value
        self.update_window_character()

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
        self._i = value
        self.update_window_character()

    def move(self, event):
        if event == 'R':
            self.direction = 'R'
            for _ in range(VEL_MOVIMIENTO):
                self.j += 1
        elif event == 'L':
            self.direction = 'L'
            for _ in range(VEL_MOVIMIENTO):
                self.j -= 1
        elif event == 'U':
            self.direction = 'U'
            for _ in range(VEL_MOVIMIENTO):
                self.i -= 1
        elif event == 'D':
            self.direction = 'D'
            for _ in range(VEL_MOVIMIENTO):
                self.i += 1
