"""
Este módulo se encarga de leer los parámetros del cliente, ubicados en el
archivo parametros.json.
"""

import json
import os

PATH_JSON = os.path.join("parametros.json")
with open(PATH_JSON) as parametros_file:
    PARAMETROS = json.load(parametros_file)
