import os
import json
import time # Ocupe time.strftime para obtener fecha y hora


class DocengelionEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Docengelion):
            return {
                'modelo': obj.modelo,
                'nucleo': obj.nucleo,
                'estado': 'reparacion',
                'registro_reparacion': time.strftime(r"%Y-%m-%d %H:%M:%S")
            }
        return super().default(obj)


class Docengelion:
    def __init__(self, modelo, nucleo, *args, **kwargs):
        self.modelo = modelo
        self.nucleo = nucleo
        self.estado = 'funcional'
        self.registro_reparacion = None


def recibir_eva(ruta):
    """
    Carga el archivo cuyo path es ruta, que contiene la información de las
    Unidades Docengelion, serializada como un archivo JSON. Retorna una lista
    de instancias de Docengelion cuyos modelos correspondan a los del archivo.
    """
    with open(ruta, "rb") as file_:
        instances_ = [Docengelion(**args) for args in json.load(file_)]
    return instances_


def reparar_eva(docengelion):
    """
    Recibe una instancia de Docengelion a reparar. Serializa en JSON la
    instancia recibida y crea una copia con los siguientes cambios:
        - cambia el atributo estado por el valor 'reparacion'
        - agrega el atributo registro_reparacion con el string fecha y hora 
    Guarda el objeto serializado en el archivo "Unidad-{modelo}.json", dentro
    de la carpeta Daniar/
    """
    new_instance = Docengelion(**docengelion.__dict__.copy())
    if not "Daniar" in os.listdir():
        os.mkdir("Daniar")
    path_ = os.path.join("Daniar", f"Unidad-{new_instance.modelo}")
    with open(path_, "w") as output_file:
        json.dump(new_instance, output_file, cls=DocengelionEncoder)
    return new_instance



if __name__ == '__main__':
    try:
        dcngelions = recibir_eva('docent.json')
        if dcngelions:
            print("DANIAR200: Ha cargado las unidades Docengelion")
        try:
            for unidad in dcngelions:
                reparar_eva(unidad)
            print("DANIAR201: Se estan reparando las unidades Docengelion")
        except Exception as error:
            print(f'Error: {error}')
            print("DANIAR501: No ha podido reparar las unidades Docengelion")
    except Exception as error:
        print(f'Error: {error}')
        print("DANIAR404: No ha podido cargar las unidades Docengelion")
