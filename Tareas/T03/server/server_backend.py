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
        response = {
            "command": "login",
            "feedback": ""
        }
        if username in sockets:
            feedback = f"El usuario {username} ya está conectado."
            log_output += "\n" + feedback
            return False, response, log_output
        if username in self.usernames_registrados:
            for usuario in self.usuarios_registrados:
                if usuario.username == username:
                    user = usuario
                    break
            response["command"] = "start"
            response["user"] = user
            return True, response, log_output
        feedback = f"El usuario {username} no está registrado en el servidor."
        log_output += "\n" + feedback
        response["feedback"] = feedback
        return False, response, log_output

    def grant_room_access(self, client_socket, user, room, rooms):
        room_name = room.nombre
        response = dict()
        log_output = f"{user.username} solicita entrar a {room_name}."
        for r in rooms:
            if r.nombre == room_name:
                target_room = r
                break
        if len(target_room.usuarios_conectados) < 5:
            log_output += f"\nSolicitud aceptada."
            response["command"] = "access_granted"
        else:
            log_output += f"\nSolicitud rechazada, sala llena."
            response["command"] = "access_denied"
            response["feedback"] = "No se puede entrar a esta sala, está llena."
        return response, log_output
