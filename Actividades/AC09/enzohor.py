import pickle
import re


class Piloto:
    def __init__(self, nombre, alma, edad, *args, **kwargs):
        self.nombre = nombre
        self.alma = alma
        self.edad = edad

    def __setstate__(self, state):
        # Usar aumentar_sincronizacion
        self.__dict__ = aumentar_sincronizacion(state)

def cargar_almas(ruta):
    """
    Carga el archivo cuyo path es ruta, el cual contiene la información de los
    pilotos, serializado mediante pickle. Retorna una lista de instancias de
    Piloto.
    """
    with open(ruta, "rb") as file_:
        list_ = pickle.load(file_)
    return list_

def aumentar_sincronizacion(estado):
    """
    Recibe el estado (dict) que será deserializado en la función __setstate__.
    Esta función elimina todo substring presente en el atributo alma que cumpla
    con estas 3 condiciones simultáneamente:
        - comienza con una E (mayúscula), y solo contiene esa E
        - termina con una O (mayúscula), y solo contiene esa O
        - contiene al menos una G (mayúscula)
    Retorna un nuevo estado con los cambios realizados
    """
    estado["alma"] = re.sub(r'E[^EO]*G+[^EO]*O', '', estado["alma"])
    return estado

if __name__ == '__main__':
    try:
        pilotos = cargar_almas('pilotos.magi')
        if pilotos:
            print("ENZOHOR200: Sincronizacion de los pilotos ESTABLE.")

    except Exception as error:
        print(f'Error: {error}')
        print("ENZOHOR501: CRITICO Sincronizacion de los pilotos INESTABLE")
