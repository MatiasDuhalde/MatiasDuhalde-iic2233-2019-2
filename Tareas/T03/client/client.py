"""
Código y funcionamiento del cliente.
"""
import threading
import socket
import os
import json
import time
from PyQt5.QtCore import pyqtSignal, QObject
from parametros import PARAMETROS

class Client():
    """
    Esta clase funciona como conexión entre el backend del programa y el
    servidor.
    """

    def __init__(self):
        self.start_time = time.strftime(r"%y-%m-%d %H.%M.%S")
        self.log("Inicializando cliente...")

        # Communication attributes
        self.host = PARAMETROS["host"]
        self.port = PARAMETROS["port"]
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Other attributes
        self.username = None
        self.connected = False

        try:
            self.socket_cliente.connect((self.host, self.port))
            self.log(f"Cliente conectado exitosamente al servidor en {self.host}:{self.port}")
            self.connected = True

            # Thread para interactuar con el servidor
            thread = threading.Thread(target=self.listen_thread, daemon=True)
            thread.start()
            self.log("Escuchando al servidor...")
        except ConnectionRefusedError:
            self.log(f"No se encontró un servidor en {self.host}:{self.port}")
            self.log("Cerrando cliente")
            self.socket_cliente.close()
            exit()

    def listen_thread(self):
        """
        Este método es el usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        :return:

        TODO
        ESTA WEA NO SIRVE JJJJJJJAAAAAAAAAA
        """

        # Si desean que un usuario pueda desconectarse
        while self.connected:
            # Primero recibimos los 4 bytes del largo
            response_bytes_length = self.socket_cliente.recv(4)
            # Los decodificamos
            response_length = int.from_bytes(response_bytes_length, byteorder="little")

            # Luego, creamos un bytearray vacío para juntar el mensaje
            response_bytes = bytearray()

            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response_bytes) < response_length:
                largo_por_recibir = min(response_length - len(response_bytes), 256)
                response_bytes += self.socket_cliente.recv(largo_por_recibir)

            # Una vez que tenemos todos los bytes, entonces ahí decodificamos
            response = response_bytes.decode()

            # Luego, debemos cargar lo anterior utilizando json
            decoded = json.loads(response)

            # Para evitar hacer muy largo este método, el manejo del mensaje se
            # realizará en otro método
            self.manejar_comando(decoded)

    @staticmethod
    def encode_message(msg):
        """
        Transforma un mensaje en chunks. Este se serializa usando JSON, y luego
        se codifica según el protocolo descrito en el enunciado:
         - Primeros 4 bytes indican el largo del contenido del mensaje, en
           little endian.
         - Los chunks que representan el mensaje se separan en 124 bytes.
         - Cada chunk es antecedido por el número de chunk, 4 bytes en
           big endian.
         - Si un chunk tiene menos de 124 bytes, estos se rellenan con ceros
           a la derecha.

        Parámetros:
         - msg: Objeto a codificar

        Retorna una lista de cadenas de bytes según el protocolo.

        VER: https://github.com/IIC2233/syllabus/issues/546#issuecomment-559302753
        """
        msg_json = json.dumps(msg)
        msg_bytes = msg_json.encode()

        msg_length = len(msg_bytes)
        msg_length_bytes = msg_length.to_bytes(4, byteorder="little")

        blocks = [msg_length_bytes]
        for i in range(0, msg_length, 124):
            n_chunk = i//124 + 1
            n_chunk_bytes = n_chunk.to_bytes(4, byteorder="big")
            chunk_bytes = msg_bytes[i:80+i]
            if len(chunk_bytes) < 124:
                chunk_bytes += b"\x00"*(124 - len(chunk_bytes))
            blocks.append(n_chunk_bytes)
            blocks.append(chunk_bytes)
        return blocks

    def send(self, username=None, action="nothing"):
        """
        Este método se encarga de comunicarse con el servidor. La información
        es indexada dentro de un diccionario, el cual se codifica y se manda.

        Parámetros:
         - username: Nombre de usuario

        TODO
        AGREGAR LOS OTROS PARÁMETROS
        """

        dict_ = {
            "username": username,
            "action": action
        }

        msg_encoded = Client.encode_message(dict_)
        for chunk in msg_encoded:
            self.socket_cliente.send(chunk)

    @staticmethod
    def decode_message(msg):
        """
        Transforma una cadena de bytes en un objeto (revisar protocolo en
        self.encode_message).

        Parámetros:
         - msg: Bytes a decodificar

        Retorna el objeto decodificado.
        """
        msg_json = msg.decode(encoding="utf-8")
        decoded_msg = json.loads(msg_json)

        return decoded_msg

    def receive(self):
        """
        Este método se encarga de comunicarse con el servidor. La información
        es indexada dentro de un diccionario, el cual se codifica y se manda.

        Parámetros:
         - username: Nombre de usuario

        Retorna el objeto recibido y decodificado.
        """
        # Recibir largo del mensaje (bytes)
        msg_length_bytes = self.socket_cliente.recv(4)
        msg_length = int.from_bytes(msg_length_bytes, byteorder="little")

        msg = bytearray()
        proof_counter = 1
        while len(msg) < msg_length:
            bytes_msg = self.socket_cliente.recv(128)
            index = int.from_bytes(bytes_msg[0:4], byteorder="big")
            if proof_counter != index:
                error_msg = "Mensaje no recibido correctamente"
                self.log(error_msg)
                raise ValueError(error_msg)
            proof_counter += 1
            msg += bytes_msg[4:]

        return self.decode_message(msg)

    def log(self, msg, end="\n"):
        """
        Escribe en el archivo txt de log/registro.

        Parámetros:
         - msg: Mensaje a escribir en el log
        """
        filename_ = f'[{self.start_time}] client log.txt'
        if os.path.isfile(filename_):
            mode = "a"
        else:
            mode = "w"
        with open(filename_, mode) as log_file:
            time_ = time.strftime(r"%y-%m-%d %H:%M:%S")
            log_file.write(f"[{time_}] {msg}{end}")
