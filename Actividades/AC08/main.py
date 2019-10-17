from cargar import cargar_archivos
from os import path
from collections import deque


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id = id_usuario
        self.nombre = nombre
        self.seguidos = []
        # self.seguidores = [] # almacenar a los seguidores es opcional.


class Pintogram:
    def __init__(self):
        # Recuerda que debes almacenar todos los usuarios dentro de la red
        self.usuarios = {}

    def nuevo_usuario(self, id_usuario, nombre):
        # Método que se encarga de agregar un usuario a la red
        usuario = Usuario(id_usuario, nombre)
        self.usuarios[id_usuario] = usuario

    def follow(self, id_seguidor, id_seguido):
        # Método que permite a un usuario seguir a otro
        try: 
            if id_seguidor == id_seguido:
                raise ValueError(f"No te puedes seguir a ti mismo.")
            if id_seguido in self.usuarios[id_seguidor].seguidos:
                raise ValueError(f"El usuario {id_seguidor} ya sigue al usuario {id_seguido}.")
            else: 
                self.usuarios[id_seguidor].seguidos.append(id_seguido)
        except ValueError as err:
            print(err)

    def cargar_red(self, ruta_red):
        # Método que se encarga de generar la red social, cargando y
        # guardando cada uno de los usuarios. Quizás otras funciones de
        # Pintogram sean útiles.
        for id_usuario, nombre, seguidos in cargar_archivos(ruta_red):
            self.nuevo_usuario(id_usuario, nombre)
            for usuario_seguido in seguidos:
                self.follow(id_usuario, usuario_seguido)
            

    def unfollow(self, id_seguidor, id_seguido):
        # Método que pertmite a un usuario dejar de seguir a otro
        try:
            if id_seguidor == id_seguido:
                raise ValueError(f"No te puedes dejar de seguir a ti mismo.")
            self.usuarios[id_seguidor].seguidos.remove(id_seguido)
        except ValueError:
            print(f"El usuario {id_seguidor} no sigue al usuario {id_seguido}.")

    def mis_seguidos(self, id_usuario):
        # Método que retorna los seguidores de un usuario
        n_seguidores = 0
        for key in self.usuarios:
            if id_usuario in self.usuarios[key].seguidos:
                n_seguidores += 1
        return n_seguidores

    def distancia_social(self, start, end, path = []):
        # Método que retorna la "distancia social" de dos usuarios
        path = path + [start]
        if start == end:
            return path
        if not start in self.usuarios:
            return None
        shortest = None
        for node in self.usuarios[start].seguidos:
            if node not in path:
                newpath = self.distancia_social(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest




        # path = path + [id_usuario_1]
        # if id_usuario_1 == id_usuario_2:
        #     return path
        # if not id_usuario_1 in self.usuarios[id_usuario_1].seguidos:
        #     return None
        # shortest = None
        # for node in self.usuarios[id_usuario_1].seguidos:
        #     if node not in path:
        #         newpath = self.distancia_social(node, id_usuario_2, path)
        #         if newpath:
        #             if not shortest or len(newpath) < len(shortest):
        #                 shortest = newpath
        # return shortest


if __name__ == "__main__":
    pintogram = Pintogram()
    pintogram.cargar_red(path.join("archivos", "simple.txt"))
    print(pintogram.mis_seguidos("1"))
    print(pintogram.mis_seguidos("3"))
    print(len(pintogram.distancia_social(start="3", end="5")))

# Puedes agregar más consultas y utilizar los demás archivos para probar tu código
