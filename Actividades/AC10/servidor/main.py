import socket
import json
import pickle
import re
from juego import Juego


class Servidor:

    def __init__(self):
        '''Inicializador de servidor.

        Crea socket de servidor, lo vincula a un puerto.'''
        # -----------------------------------------
        # Completar y agregar argumentos desde aquí

        # PAUTA - Host y Port
        self.host = "localhost"
        self.port = 14502
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Aqui deberas preparar el socket para que escuche una conexion
        # PAUTA - Se inicia el socket
        self.socket_servidor.bind((self.host, self.port))
        # PAUTA - El socket escucha conexiones
        self.socket_servidor.listen()

        # Completar y agregar argumentos hasta aquí
        # -----------------------------------------
        print("Servidor iniciado.")
        self.juego = None  # Juego comienza nulo.
        self.socket_cliente = None  # Aún no hay cliente.

    def esperar_conexion(self):
        '''Espera a la conectarse con un cliente y obtiene su socket.'''
        print("Esperando cliente...")
        # --------------------
        # Completar desde aquí
        # Debes actualizar el valor de self.socket_cliente al conectar
        # PAUTA - Se conecta y guarda el socket
        self.socket_cliente, _ = self.socket_servidor.accept()

        # Completar hasta aquí
        # --------------------
        print("¡Servidor conectado a cliente!")
        self.interactuar_con_cliente()

    def interactuar_con_cliente(self):
        '''Comienza ciclo de interacción con cliente.

        Recibe un acción y responde apropiadamente.'''
        self.enviar_estado('', True)
        while self.socket_cliente:
            accion = self.recibir_accion()
            self.manejar_accion(accion)

    def enviar_estado(self, mensaje, continuar):
        '''Envia estado del juego en el servidor.'''
        if continuar:
            if self.juego is not None:
                mensaje = f'{self.juego.tablero_string()}\n{mensaje}\n'
            acciones = ("¿Qué deseas hacer?\n"
                        "Para jugar nuevo juego: \\juego_nuevo\n"
                        "Para jugar en una columna: \\jugada columna\n"
                        "Para salir: \\salir\n")
            mensaje = mensaje + acciones
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje

        dict_ = {
            "mensaje": mensaje,
            "continuar": continuar
        }

        # PAUTA - Se usa pickle para serializar (BONUS)
        mensaje_codificado = pickle.dumps(dict_)
        bytes_length = len(mensaje_codificado).to_bytes(4, byteorder="little")

        # PAUTA - Se envía el mensaje
        self.socket_cliente.send(bytes_length)
        self.socket_cliente.send(mensaje_codificado)

        # Completar hasta aquí
        # --------------------

    def recibir_accion(self):
        '''Recibe mensaje desde el cliente y lo decodifica.'''
        # -----------------------------------------------------
        # Completar y usar un metodo para todo largo de mensaje

        # PAUTA - Se recibe el mensaje
        bytes_length = self.socket_cliente.recv(4)
        msg_length = int.from_bytes(bytes_length, byteorder="little")
        bytes_recibidos = self.socket_cliente.recv(msg_length)
        # En caso de que se cierre la conexión con el cliente
        if not bytes_length:
            print("Ha ocurrido un error de conexión con el cliente")
            return None

        # PAUTA - Se usa JSON para deserializar (BONUS)
        dict_recibido = json.loads(bytes_recibidos.decode(encoding="utf-8"))

        accion = dict_recibido["accion"]  # Respuesta resultante

        # Completar hasta aquí
        # --------------------
        return accion

    def manejar_accion(self, accion):
        '''Maneja la acción recibida del cliente.'''
        print(f'Acción recibida: {accion}')
        # --------------------
        # Completar desde aquí

        # Obtener el tipo de acción que envió el cliente.
        # PAUTA - Se obtiene el comando del cliente (1/2)
        if accion is None:
            self.socket_cliente.close()
            print('Cliente desconectado.\n')
            self.socket_cliente = None
            return
        if re.match(r'\\juego_nuevo$', accion):
            tipo = '\\juego_nuevo'
        elif re.match(r'\\salir$', accion):
            tipo = '\\salir'
        elif re.match(r'\\jugada [0-9]+$', accion):
            tipo = '\\jugada'
        else:
            raise ValueError("QUE PAAAASOO")
        # Completar hasta aquí
        # --------------------
        if tipo == '\\juego_nuevo':
            self.juego = Juego()
            self.juego.crear_tablero()
            self.enviar_estado('', True)
        elif tipo == '\\salir':
            self.enviar_estado('¡Adios!', False)
            self.juego = None
            self.socket_cliente.close()
            print('Cliente desconectado.\n')
            self.socket_cliente = None
        elif tipo == '\\jugada':
            if self.juego is None:
                self.enviar_estado('Ningún juego ha iniciado.', True)
            else:
                # --------------------
                # Completar desde aquí

                # Obtener la jugada que envió el cliente.
                # PAUTA - Se obtiene el comando del cliente (2/2)
                jugada = int(re.search(r'[0-9]+', accion).group())

                # Completar hasta aquí
                # --------------------
                if not self.juego.es_jugada_valida(jugada):
                    self.enviar_estado('Jugada inválida.', True)
                else:
                    gano = self.juego.turno_jugador(jugada)
                    if gano:
                        self.enviar_estado('¡Ganaste! Se acabó el juego.', True)
                        self.juego = None
                    else:
                        perdio = self.juego.turno_cpu()
                        if perdio or self.juego.empate():
                            self.enviar_estado('No ganaste :( Se acabó el juego.', True)
                            self.juego = None
                        else:
                            self.enviar_estado('', True)


if __name__ == "__main__":
    servidor = Servidor()
    while True:
        try:
            servidor.esperar_conexion()
        except KeyboardInterrupt:
            print("\nServidor interrumpido")
            break
