"""
Código y funcionamiento del cliente.
"""
import threading
import socket
import os
import json
import time
from PyQt5.QtCore import pyqtSignal, QObject
from backend import Backend
from gui_inicio import VentanaInicio
from parametros import PARAMETROS

class Client(QObject):
    """
    Clase base, controla el frontend y se comunica con el servidor.
    Hereda de QObject para poder emitir y conectar señales.
    """
    sendto_inicio_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.start_time = time.strftime(r"%y-%m-%d %H.%M.%S")
        self.log("Inicializando cliente...")

        # Communication attributes
        self.host = PARAMETROS["host"]
        self.port = PARAMETROS["port"]
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Functional attributes
        self.backend = Backend()
        self.ventana_inicio = None
        self.venana_principal = None

        # Other attributes
        self.username = None
        self.connected = False

        try:
            self.client_socket.connect((self.host, self.port))
            self.log(f"Cliente conectado exitosamente al servidor en {self.host}:{self.port}")
            self.connected = True

            self.log("Iniciando GUI...")
            self.ventana_inicio = VentanaInicio()
            self.connect_signals()

            thread = threading.Thread(target=self.listen_thread, daemon=True)
            thread.start()
            self.log("Escuchando al servidor...")
        except ConnectionRefusedError:
            self.log(f"No se encontró un servidor en {self.host}:{self.port}")
            self.close_client()
        except ConnectionError:
            self.log("ERROR: Servidor desconectado.")
            self.close_client()

    def connect_signals(self):
        """
        Conecta señales del backend con el frontend

        TODO
        Otras ventanas
        """
        self.ventana_inicio.sendto_client_signal.connect(self.handle_gui)
        self.sendto_inicio_signal.connect(self.ventana_inicio.handle_client)

    def handle_gui(self, dict_):
        """
        Maneja información recibida desde la interfaz, y se comunica con el
        servidor en caso de ser necesario.
        """
        new_dict = Backend.handle_gui_signal(dict_)
        if new_dict["send"]:
            del new_dict["send"]
            self.send(**new_dict)
        else:
            raise NotImplementedError


    def listen_thread(self):
        """
        Método usado en un thread, esta pendiente de recibir los datos del
        servidor. Invoca a la función encargada de manejar los comandos.
        """
        while self.connected:
            data = self.receive()
            if data is None:
                raise ConnectionError
            self.handle_command(data)

    def handle_command(self, data):
        """
        Maneja la señal enviada por el servidor.

        TODO
        literalmente todo
        """
        command = data["command"]
        print("Se recibió:", data)

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
            blocks.append(n_chunk_bytes + chunk_bytes)
        return blocks

    def send(self, username, command):
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
            "command": command
        }

        msg_encoded = Client.encode_message(dict_)
        for chunk in msg_encoded:
            self.client_socket.send(chunk)

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
        Este método se encarga de recibir los mensajes del servidor.

        Retorna el objeto recibido y decodificado.
        """
        msg_length_bytes = self.client_socket.recv(4)
        if not msg_length_bytes:
            return None
        msg_length = int.from_bytes(msg_length_bytes, byteorder="little")

        msg = bytearray()
        proof_counter = 1
        while len(msg) < msg_length:
            bytes_msg = self.client_socket.recv(128)
            index = int.from_bytes(bytes_msg[0:4], byteorder="big")
            if proof_counter != index:
                error_msg = "Mensaje no recibido correctamente"
                self.log(error_msg)
                raise ValueError(error_msg)
            proof_counter += 1
            msg += bytes_msg[4:]

        return self.decode_message(msg)

    def close_client(self):
        """
        Cierra la conexión con sel servidor (socket) y termina el programa
        """
        self.log("Cerrando cliente")
        self.client_socket.close()
        exit()


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
        with open(filename_, mode, encoding="utf-8") as log_file:
            time_ = time.strftime(r"%y-%m-%d %H:%M:%S")
            output_ = f"[{time_}] {msg}{end}"
            log_file.write(output_)
            print(output_, end="")
