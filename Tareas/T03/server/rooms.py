"""
Modela a las Salas de Chat de la aplicación.
La aplicación debe tener 4 salas de chat distintas.
Instancias de la clase Sala estarán contenidas dentro de una lista en la
instancia principal del servidor.
"""

class Room:
    """
    Modela a una Sala.

    Atributos:
     - Nombre
     - Personaje

    Métodos:
     - get_usuarios
     - get_amigos
    """
    def __init__(self, nombre, usuarios_conectados=None):
        # CANNOT SERIALIZE SOCKETS
        if usuarios_conectados is None:
            usuarios_conectados = dict()
        self.nombre = nombre
        self.usuarios_conectados = usuarios_conectados

    def __repr__(self):
        return self.nombre + f"\nUsuarios conectados: {self.usuarios_conectados}"
