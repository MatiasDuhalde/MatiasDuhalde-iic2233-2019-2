"""
Modela a los Usuarios de la aplicación. Carga a estos a partir de los json.
"""
import json
from parametros import PARAMETROS

class Usuario:
    """
    Modela a un usuario.

    Atributos:
     - Nombre
     - Personaje
    """
    def __init__(self, nombre, personaje):
        self.nombre = nombre
        self.personaje = personaje
        self.amigos = get_amigos(self.nombre)

    def __repr__(self):
        return self.nombre


def get_usuarios():
    """
    Retorna una lista de instancias de la clase Usuario según los contenidos
    de usuarios.json.
    """
    with open(PARAMETROS["path usuarios"], 'r', encoding='utf-8-sig') as file_usuarios:
        usuarios = []
        for info in json.load(file_usuarios):
            usuarios.append(Usuario(**info))

    return usuarios

def get_amigos(usuario):
    """
    Retorna una lista que contiene los nombres de usuario de los amigos del
    nombre de usuario pedido, según los contenidos de amigos.json
    """
    if isinstance(usuario, Usuario):
        usuario = usuario.nombre
    elif isinstance(usuario, str):
        pass
    else:
        raise TypeError
    with open(PARAMETROS["path amigos"], 'r', encoding='utf-8-sig') as file_usuarios:
        dict_amigos = json.load(file_usuarios)
        if usuario in dict_amigos:
            amigos = dict_amigos[usuario]
        else:
            amigos = []
    return amigos
