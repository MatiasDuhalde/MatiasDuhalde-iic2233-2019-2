"""
Código y funcionamiento del servidor.
"""
import threading
import socket
import os
import json
import time
from parametros import PARAMETROS

class Server:
    """
    Esta clase maneja el funcionamiento base del servidor.

    Crea un socket principal y trabaja sobre este para aceptar conexiones
    entrantes desde múltiples clientes.
    """

    def __init__(self):
        self.start_time = time.strftime(r"%y-%m-%d %H.%M.%S")
        self.log("Inicializando servidor...")

        # Diccionario a contener los sockets de los clients
        self.sockets = dict()

        self.host = PARAMETROS["host"]
        self.port = PARAMETROS["port"]
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.bind((self.host, self.port))
        self.log("Dirección y puerto enlazados..")

        self.server_socket.listen()
        self.log(f"Servidor escuchando en {self.host}:{self.port}...")

        # Thread para aceptar conexiones entrantes
        thread = threading.Thread(target=self.login_thread, daemon=True)
        thread.start()
        self.log("Servidor aceptando conexiones...")


    def login_thread(self):
        """
        Este método acepta conexiones entrantes y se encarga de iniciar sesión
        a los usuarios. Recibe un socket y luego un nombre de usuario. Si este
        es válido, se acepta la conexión y se guarda el socket en self.sockets.

        TODO
        NO SIRVE LUL
        """
        while True:
            client_socket, _ = self.server_socket.accept()
            self.log("Servidor conectado a un nuevo cliente...")

            # RECIBIR NOMBRE DEL USUARIO (O INSTANCIA USUARIO) desde client

            # Guarda el socket
            self.sockets["name"] = client_socket

            # Inicia el thread encargado de escuchar al cliente
            # listening_client_thread = threading.Thread(
            #     target=self.listen_client_thread,
            #     args=(client_socket, id_),
            #     daemon=True
            # )
            # listening_client_thread.start()

    def listen_client_thread(self, client_socket, id_cliente):
        """
        Este método va a ser usado múltiples veces en threads pero cada vez con
        sockets de clientes distintos.
        :param client_socket: objeto socket correspondiente a algún cliente
        :return:

        TODO
        LEER Y ARREGLAR ESTO ALSO DOC
        """

        while True:
            try:
                # Primero recibimos los 4 bytes del largo
                response_bytes_length = client_socket.recv(4)
                # Los decodificamos
                response_length = int.from_bytes(response_bytes_length,
                                                 byteorder="big")

                # Luego, creamos un bytearray vacío para juntar el mensaje
                response_bytes = bytearray()

                # Recibimos datos hasta que alcancemos la totalidad de los datos
                # indicados en los primeros 4 bytes recibidos.
                while len(response_bytes) < response_length:
                    largo_por_recibir = min(response_length - len(response_bytes), 256)
                    response_bytes += client_socket.recv(largo_por_recibir)

                # Una vez que tenemos todos los bytes, entonces ahí decodificamos
                response = response_bytes.decode()

                # Luego, debemos cargar lo anterior utilizando json
                decoded = json.loads(response)

                # Para evitar hacer muy largo este método, el manejo del mensaje se
                # realizará en otro método
                self.manejar_comando(decoded, client_socket)
            except ConnectionResetError:  # Es decir, si el cliente se desconecta
                del self.sockets[id_cliente]
                break

    def manejar_comando(self, recibido, socket):
        """
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param received: diccionario de la forma: {"palabra": Palabra recibida}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:

        TODO
        MODIFICAR PARA ESTE CONTEXTO
        """

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(recibido))

        palabra = recibido['palabra']
        palabra_fonetica, palabra_traducida = traducir(palabra)

        mensaje = {"propio": True,
                   "original": palabra,
                   "fonetica": palabra_fonetica,
                   "traducida": palabra_traducida}

        # primero le enviamos la respuesta al que pidio la conversion
        self.send(socket, mensaje)

        # despues le actualizamos la ultima consulta a todas los clientes
        mensaje.update({"propio": False})
        self.sendall(mensaje)

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

    @staticmethod
    def send(socket_, msg=None):
        """
        Este método envía la información al cliente correspondiente al socket.

        Parámetros:
         - msg: Objeto a enviar
         - socket_: socket del cliente target

        TODO
        AGREGAR LOS OTROS PARÁMETROS
        """

        dict_ = {
            "something": msg
        }

        msg_encoded = Server.encode_message(dict_)
        for chunk in msg_encoded:
            socket_.send(chunk)

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
                self.log(f'Error de conexion con cliente ')
            except ConnectionAbortedError:
                del self.sockets[username]
                self.log('Error de conexion con cliente')
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
        msg_json = msg.decode(encoding="utf-8")
        decoded_msg = json.loads(msg_json)

        return decoded_msg

    def receive(self):
        """
        Este método se encarga de recibir los mensajes del cliente.

        Retorna el objeto recibido y decodificado.
        """
        msg_length_bytes = self.server_socket.recv(4)
        msg_length = int.from_bytes(msg_length_bytes, byteorder="little")

        msg = bytearray()
        proof_counter = 1
        while len(msg) < msg_length:
            bytes_msg = self.server_socket.recv(128)
            index = int.from_bytes(bytes_msg[0:4], byteorder="big")
            if proof_counter != index:
                error_msg = "Mensaje no recibido correctamente"
                self.log(error_msg)
                raise ValueError(error_msg)
            proof_counter += 1
            msg += bytes_msg[4:]

        return self.decode_message(msg)


    def log(self, msg):
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
        with open(filename_, mode) as log_file:
            time_ = time.strftime(r"%y-%m-%d %H:%M:%S")
            log_file.write(f"[{time_}] {msg}\n")
