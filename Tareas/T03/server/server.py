"""
Código y funcionamiento del servidor.
"""
import threading
import socket
import os
import pickle
import time
from rooms import Room
from server_backend import ServerBackend
from parametros import PARAMETROS

class Server:
    """
    Esta clase maneja el funcionamiento base del servidor.

    Crea un socket principal y trabaja sobre este para aceptar conexiones
    entrantes desde múltiples clientes.
    """

    lock = threading.Lock()

    def __init__(self):
        # Log attribute
        self.start_time = time.strftime(r"%y-%m-%d %H.%M.%S")
        self.log("Inicializando servidor...")

        # Diccionario a contener los sockets de los clients
        self.host = PARAMETROS["host"]
        self.port = PARAMETROS["port"]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Other attributes
        self.sockets = dict()
        self.backend = ServerBackend()
        self.rooms = [Room(nombre=f"Sala {i}") for i in range(4)]

        self.server_socket.bind((self.host, self.port))
        self.log("Dirección y puerto enlazados..")

        self.server_socket.listen()
        self.log(f"Servidor escuchando en {self.host}:{self.port}...")

        thread = threading.Thread(target=self.login_thread, daemon=True)
        thread.start()
        self.log("Servidor aceptando conexiones...")

    def login_thread(self):
        """
        Este método acepta conexiones entrantes y se encarga de iniciar sesión
        a los usuarios. Recibe un socket y luego un nombre de usuario. Si este
        es válido, se acepta la conexión y se guarda el socket en self.sockets.
        Finalmente, se inicia un thread que escucha al socket en cuestión.
        """
        while True:
            client_socket, _ = self.server_socket.accept()
            self.log("Servidor conectado a un nuevo cliente...")

            # Recibir y validar username para indexar el socket en self.sockets
            username_valid = False
            while not username_valid:
                try:
                    dict_ = self.receive(client_socket)
                    if not dict_:
                        # Case ConnectionError in self.receive()
                        self.log("Se perdió la conexión con el cliente.")
                        break
                except ConnectionResetError:
                    self.log(f"No se pudo concretar comunicación con usuario.")
                    self.log(f"Cerrando conexión...")
                    del client_socket
                    break
                username = dict_["username"]
                username_valid, response, log_output = self.backend.validate_username(
                    self.sockets, username)
                if response["command"] == "start":
                    response["rooms"] = self.rooms
                self.log(log_output)
                self.send(client_socket, response)
            if not 'client_socket' in locals():
                continue
            if not username_valid:
                # Case ConnectionError in self.receive()
                self.log("Cerrando socket...")
                client_socket.close()
                continue

            self.log(f"Usuario {username} iniciando sesión...")
            self.sockets[username] = client_socket

            # Inicia el thread encargado de escuchar al cliente
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket, username),
                daemon=True
            )
            listening_client_thread.start()

    def listen_client_thread(self, client_socket, username):
        """
        Un thread por cada socket, que recibe los mensajes del usuario.
        El recibir un mensaje, invoca a self.handle_command() para trabajar
        el comando. En caso de desconexión borra el socket y cierra el thread.
        """
        while True:
            try:
                dict_ = self.receive(client_socket)
                if dict_ is None:
                    raise ConnectionResetError
                self.handle_command(dict_, client_socket)
            except ConnectionResetError:  # Es decir, si el cliente se desconecta
                self.log(f"El usuario {username} se ha desconectado.")
                self.log(f"Cerrando conexión...")
                del self.sockets[username]
                break

    def handle_command(self, dict_, client_socket):
        """
        Este método analiza el diccionario recibido por el cliente
        correspondiente al socket pasado como argumento.
        Procesa la solicitud según lo pedido.

        Parámetros:
         - dict_: Diccionario proveniente del client.
         - client_socket: socket correspondiente al client.
        """
        command = dict_["command"]
        if command == "logout":
            # Return same dict to accept closure
            self.send(client_socket, dict_)
            raise ConnectionResetError
        if command == "enter":
            user = dict_["user"]
            room = dict_["room"]
            response, log_output = self.backend.grant_room_access(
                client_socket, user, room, self.rooms)
            self.log(log_output)
            if response["command"] == "access_granted":
                for temp_room in self.rooms:
                    if temp_room.nombre == room.nombre:
                        temp_room.usuarios_conectados.append(user)
                        room = temp_room
                        break
            response["rooms"] = self.rooms
            response["room"] = room
            self.send(client_socket, response)
            new_dict = {
                "command": "update_rooms",
                "rooms": self.rooms
            }
            self.sendall(new_dict)

    @staticmethod
    def encode_message(msg):
        """
        Transforma un mensaje en chunks según el protocolo descrito en el
        enunciado:
         - Primeros 4 bytes indican el largo del contenido del mensaje, en
           little endian.
         - Los chunks que representan el mensaje se separan en 124 bytes
         - Cada chunk es antecedido por el número de chunk, 4 bytes en
           big endian
         - Si un chunk tiene menos de 124 bytes, estos se rellenan con ceros
           a la derecha.

        Parámetros:
         - msg: Objeto a codificar

        Retorna una cadena de bytes según el protocolo.

        VER: https://github.com/IIC2233/syllabus/issues/546#issuecomment-559302753
        """
        msg_bytes = pickle.dumps(msg)
        msg_length = len(msg_bytes)
        msg_length_bytes = msg_length.to_bytes(4, byteorder="little")
        blocks = [msg_length_bytes]
        for i in range(0, msg_length, 124):
            n_chunk = i//124 + 1
            n_chunk_bytes = n_chunk.to_bytes(4, byteorder="big")
            chunk_bytes = msg_bytes[i:i+124]
            if len(chunk_bytes) < 124:
                chunk_bytes += b"\x00"*(124 - len(chunk_bytes))
            blocks.append(n_chunk_bytes + chunk_bytes)
        return blocks

    @staticmethod
    def send(socket_, dict_=None):
        """
        Este método envía la información al cliente correspondiente al socket.

        Parámetros:
         - msg: Objeto a enviar
         - socket_: socket del cliente target
        """
        Server.lock.acquire()
        msg_encoded = Server.encode_message(dict_)
        for chunk in msg_encoded:
            socket_.send(chunk)
        Server.lock.release()

    def sendall(self, mensaje):
        """
        Envía el mensaje a todos los sockets conectados.
        Maneja los casos en los cuales ocurra una desconexión.

        Parámetros:
         - msg: Mensaje a enviar a todos los sockets conectados
        """
        username_list = list(self.sockets.keys())[:]
        for username in username_list:
            try:
                self.send(self.sockets[username], mensaje)
            except ConnectionResetError:
                del self.sockets[username]
                self.log(f'Error de conexión con cliente ')
            except ConnectionAbortedError:
                del self.sockets[username]
                self.log('Error de conexión con cliente')
            except IndexError:
                self.log('Ya se ha eliminado el cliente del diccionario')

    @staticmethod
    def decode_message(msg):
        """
        Transforma una cadena de bytes en un objeto (revisar protocolo en
        self.encode_message).

        Parámetros:
         - msg: Bytes a decodificar

        Retorna el objeto decodificado.
        """
        decoded_msg = pickle.loads(msg)
        return decoded_msg

    def receive(self, client_socket):
        """
        Este método se encarga de recibir los mensajes del cliente.

        Retorna el objeto recibido y decodificado.
        """
        msg_length_bytes = client_socket.recv(4)
        if not msg_length_bytes:
            return None
        msg_length = int.from_bytes(msg_length_bytes, byteorder="little")

        msg = bytearray()
        proof_counter = 1
        while len(msg) < msg_length:
            bytes_msg = client_socket.recv(128)
            index = int.from_bytes(bytes_msg[0:4], byteorder="big")
            if proof_counter != index:
                error_msg = "Mensaje no recibido correctamente"
                self.log(error_msg)
                raise ValueError(error_msg)
            proof_counter += 1
            msg += bytes_msg[4:]
        msg = msg[:msg_length]
        return self.decode_message(msg)

    def log(self, msg, end="\n"):
        """
        Escribe en el archivo txt de log/registro

        Parámetros:
         - msg: Mensaje a escribir en el log
        """
        filename_ = f'[{self.start_time}] server log.txt'
        if os.path.isfile(filename_):
            mode = "a"
        else:
            mode = "w"
        time_ = time.strftime(r"%y-%m-%d %H:%M:%S")
        output_ = f"[{time_}] {msg}{end}"
        with open(filename_, mode, encoding="utf-8") as log_file:
            log_file.write(output_)
        print(output_, end="")
