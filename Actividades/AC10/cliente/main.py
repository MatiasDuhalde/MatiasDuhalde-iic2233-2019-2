import socket
import json
import pickle
import re

class Cliente:

    def __init__(self):
        '''Inicializador de cliente.

        Crea su socket, e intente conectarse a servidor.
        '''
        # --------------------
        # Completar desde aquí

        # PAUTA - Host y Port
        self.host = "localhost"
        self.port = 14502
        # PAUTA - Se inicia el socket
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Aqui deberas intentar conectar al servidor.
            self.socket_cliente.connect((self.host, self.port))
            # Completar hasta aquí
            # --------------------
            print("Cliente conectado exitosamente al servidor.")
            self.interactuar_con_servidor()
        except ConnectionRefusedError:
            self.cerrar_conexion()

    def interactuar_con_servidor(self):
        '''Comienza ciclo de interacción con servidor.

        Recibe estado y envia accion.
        '''
        while True:
            mensaje, continuar = self.recibir_estado()
            print(mensaje)
            if not continuar:
                break
            accion = self.procesar_comando_input()
            while accion is None:
                print('Input invalido.')
                accion = self.procesar_comando_input()
            self.enviar_accion(accion)
        self.cerrar_conexion()

    def recibir_estado(self):
        '''Recibe actualización de estado desde servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        # PAUTA - Se recibe el mensaje serializado
        bytes_length = self.socket_cliente.recv(4)
        msg_length = int.from_bytes(bytes_length, byteorder="little")
        bytes_recibidos = self.socket_cliente.recv(msg_length)
        # En caso de que se cierre la conexión con el servidor
        if not bytes_length:
            print("Ha ocurrido un error de conexión con el servidor")
            return None, False

        # PAUTA - Se usa pickle para deserializar (BONUS)
        dict_recibido = pickle.loads(bytes_recibidos)
        # Debe haber un string para imprimirse
        mensaje = dict_recibido["mensaje"]
        # Debe haber un boolean para saber si continuar funcionando
        continuar = dict_recibido["continuar"]

        # Completar hasta aquí
        # --------------------
        return mensaje, continuar

    def procesar_comando_input(self):
        '''Procesa y revisa que el input del usuario sea valido'''
        input_usuario = input('-> ')
        # ---------
        # Completar
        # PAUTA - Se revisa si el input es válido y retorna
        input_usuario = input_usuario.lower().strip()
        if re.match(r'\\juego_nuevo$', input_usuario):
            return input_usuario
        if re.match(r'\\salir$', input_usuario):
            return input_usuario
        if re.match(r'\\jugada [0-9]+$', input_usuario):
            return input_usuario
        return None
        # Completar hasta aquí
        # --------------------

    def enviar_accion(self, accion):
        '''Envia accion asociada a comando ya procesado al servidor.'''
        # ----------------------------------------------------------
        # Completar y usar un metodo para cualquier largo de mensaje

        # PAUTA - Se usa JSON para serializar (BONUS)
        dict_ = {
            "accion": accion
        }
        mensaje_codificado = json.dumps(dict_).encode(encoding='utf-8')
        bytes_length = len(mensaje_codificado).to_bytes(4, byteorder="little")
        # PAUTA - Se envía el mensaje
        self.socket_cliente.send(bytes_length)
        self.socket_cliente.send(mensaje_codificado)
        # Completar hasta aquí
        # --------------------

    def cerrar_conexion(self):
        '''Cierra socket de conexión.'''
        self.socket_cliente.close()
        print("Conexión terminada.")


if __name__ == "__main__":
    Cliente()
