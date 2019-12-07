"""
Este módulo actúa como unidad de procesamiento del server.
"""
from parametros import PARAMETROS

class ServerBackend:
    """
    Contiene métodos estáticos que procesan información proveniente desde el
    servidor. Luego de procesar, retorna hacia este.
    """

    @staticmethod
    def validate_username(sockets, usuarios, username):
        """
        Valida el nombre de usuario ingresado según el enunciado. Solo se
        admite si cumple con las siguientes condiciones.
         - El username está registrado (en usuarios.json)
         - El username no está actualmente conectado
        El username es case-sensitive!

        Parámetros:
         - sockets: Diccionario de sockets de clientes conectados en la forma
                    {username : socket}
         - usuarios: Diccionario de instancias de Usuario {username : Usuario}
         - username: Nombre de usuario a analizar

        Retorna bool indicando si el nombre de usuario es válido o no, un
        diccionario de respuesta, y un mensaje a escribir en el log.
        """
        log_output = f"Se recibe el nombre '{username}'."
        response = {
            "command": "login",
            "feedback": ""
        }
        if username == "":
            feedback = f"El nombre ingresado no es válido."
            log_output += "\n" + feedback
            response["feedback"] = feedback
            return response, log_output
        if username in sockets:
            feedback = f"El usuario {username} ya está conectado."
            log_output += "\n" + feedback
            return response, log_output
        if username in usuarios:
            user = usuarios[username]
            response["command"] = "start"
            response["user"] = user
            return response, log_output
        feedback = f"El usuario {username} no está registrado en el servidor."
        log_output += "\n" + feedback
        response["feedback"] = feedback
        return response, log_output

    @staticmethod
    def grant_room_access(user, room, rooms):
        room_name = room.nombre
        response = dict()
        log_output = f"{user.username} solicita entrar a {room_name}."
        for r in rooms:
            if r.nombre == room_name:
                target_room = r
                break
        if len(target_room.usuarios_conectados) < PARAMETROS["rooms_number"]:
            log_output += f"\nSolicitud aceptada."
            response["command"] = "access_granted"
        else:
            log_output += f"\nSolicitud rechazada, sala llena."
            response["command"] = "access_denied"
            response["feedback"] = "No se puede entrar a esta sala, está llena."
        return response, log_output
