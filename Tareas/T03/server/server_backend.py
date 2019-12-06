"""
Este módulo actúa como unidad de procesamiento del server.
"""
from usuarios import Usuario

class ServerBackend:
    """
    Contiene métodos estáticos que procesan información proveniente desde el
    servidor. Luego de procesar, retorna hacia este.
    """

    def __init__(self):
        self.usuarios_registrados = Usuario.get_usuarios()
        self.usernames_registrados = [u.username for u in self.usuarios_registrados]

    def validate_username(self, sockets, username):
        """
        Valida el nombre de usuario ingresado según el enunciado. Solo se
        admite si cumple con las siguientes condiciones.
         - El username está registrado (en usuarios.json)
         - El username no está actualmente conectado
        El username es case-sensitive!

        Parámetros:
         - username: Nombre de usuario a analizar

        Retorna bool indicando si el nombre de usuario es válido o no y un
        mensaje a escribir en el log.
        """
        log_output = f"Se recibe el nombre '{username}'."
        if username in sockets:
            log_output += f"\nEl usuario {username} ya está conectado."
            return False, log_output
        if username in self.usernames_registrados:
            return True, log_output
        log_output += f"\nEl usuario {username} no está registrado en el servidor."
        return False, log_output
