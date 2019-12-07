"""
Este módulo actúa como unidad de procesamiento del server.
"""
import re
from parametros import PARAMETROS
from usuarios import Usuario

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
            response["feedback"] = feedback
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

    @staticmethod
    def check_for_command(text):
        if re.match(r'/friend \'[^ ]+\' \'[^ ]+\'$', text):
            text = text.replace("'", "")
            args = text.split()[1:]
            return True, "/friend", args
        elif re.match(r'/unfriend \'[^ ]+\' \'[^ ]+\'$', text):
            text = text.replace("'", "")
            args = text.split()[1:]
            return True, "/unfriend", args
        elif re.match(r'/get reachable \'[^ ]+\' [1-9]+$', text):
            text = text.replace("'", "")
            args = text.split()[2:]
            return True, "/get reachable",args
        elif re.match(r'/get affinity \'[^ ]+\' \'[^ ]+\'$', text):
            text = text.replace("'", "")
            args = text.split()[2:]
            return True, "/get affinity", args
        elif re.match(r'/get recommendation \'[^ ]+\'$', text):
            text = text.replace("'", "")
            args = text.split()[2:]
            return True, "/get recommendation", args
        else:
            return False, None, None

    @staticmethod
    def exec_command(command, args, usuarios):
        if command == "/friend":
            try:
                username_a = args[0]
                username_b = args[1]
                user_a = usuarios[username_a]
                user_b = usuarios[username_b]
            except KeyError:
                output = "Error - usuario no existe"
                return output, usuarios
            if not username_b in user_a.amigos:
                user_a.amigos.append(username_b)
            if not username_a in user_b.amigos:
                user_b.amigos.append(username_a)
            usuarios[username_a] = user_a
            usuarios[username_b] = user_b
            Usuario.write_amigos(user_a)
            Usuario.write_amigos(user_b)
            output = f"{username_a} y {username_b} son amigos!"
        elif command == "/unfriend":
            try:
                username_a = args[0]
                username_b = args[1]
                user_a = usuarios[args[0]]
                user_b = usuarios[args[1]]
            except KeyError:
                output = "Error - usuario no existe"
                return output, usuarios
            if username_b in user_a.amigos:
                user_a.amigos.remove(username_b)
            if username_a in user_b.amigos:
                user_b.amigos.remove(username_a)
            usuarios[username_a] = user_a
            usuarios[username_b] = user_b
            Usuario.write_amigos(user_a)
            Usuario.write_amigos(user_b)
            output = f"{username_a} y {username_b} ya no son amigos!"
        elif command == "/get reachable":
            try:
                username_a = args[0]
                user_a = usuarios[args[0]]
            except KeyError:
                output = "Error - usuario no existe"
                return output, usuarios
            distance = int(args[1])
            output = "No se"
        elif command == "/get affinity":
            try:
                username_a = args[0]
                username_b = args[1]
                user_a = usuarios[args[0]]
                user_b = usuarios[args[1]]
            except KeyError:
                output = "Error - usuario no existe"
                return output, usuarios
            output = "No se"
        elif command == "/get recommendation":
            try:
                username_a = args[0]
                user_a = usuarios[args[0]]
            except KeyError:
                output = "Error - usuario no existe"
                return output, usuarios
            output = "No se"
        return output, usuarios
