import os
from yoNube import descargar
from archivos import (leer_artistas, leer_canciones, leer_usuarios, leer_ratings)
from decodificador import decodificar
from datetime import datetime
from statistics import mean

# ----- PROPUESTO: DECORADOR CONTADOR -------

def contador(consulta):
    """
    Completar para llevar la cuenta de las consultas.
    Eres libre de agregar argumentos para el desarrollo del decorador.
    """
    i = 0
    def wrapper(*args, **kwargs)
        i += 1
        return consulta(*args, **kwargs)
    return wrapper


# ------------------------------------------------------------

# ---------------------   CONSULTAS   -----------------------

# ------------------------------------------------------------


def usuarios_por_antiguedad(usuarios):
    """
    Esta consulta debe retornar un GENERADOR con los usuarios
    ordenados desde el más antiguo hasta el más nuevo.
    """
    usuarios_ordenados = []
    for usuario in usuarios:
        date = datetime.strptime(usuario.fecha_ingreso, "%d/%m/%Y")
        usuarios_ordenados.append((usuario, date))
    usuarios_ordenados.sort(key=lambda x: x[1])
    i = 0
    while True:
        yield usuarios_ordenados[i][0]
        i += 1


def ratings_usuarios(username, ratings):
    """
    Esta consulta retorna una LISTA con los ratings que el usuario
    ha emitido.
    """
    return list(filter(lambda x: x.username == username, ratings))


def canciones_artistas(nombre_artista, canciones, artistas):
    """
    Esta consulta retorna un GENERADOR con las canciones del artista
    solicitado.
    """
    ID_artista = -1
    for artista in artistas:
        if artista.nombre == nombre_artista:
            ID_artista = artista.id
            break
    canciones_artista = list(filter(lambda x: x.id == ID_artista, canciones))
    yield from canciones_artista


def rating_promedio(nombre_cancion, canciones, ratings):
    """
    Esta consulta retorna un FLOAT con el rating promedio de la cancion
    solicitada.

    OJO: puede que la canción indicada no tenga ratings asociados.
    En ese caso asume un rating promedio = 0.
    """
    rating = 0
    ID_cancion = -1
    for cancion in canciones:
        if cancion.nombre == nombre_cancion:
            ID_cancion = cancion.id
            break
    ratings_cancion = filter(lambda x: x.id_cancion == ID_cancion, ratings)
    ratings_cancion = map(lambda x: int(x.rating), ratings_cancion)
    if ratings_cancion:
        rating = mean(ratings_cancion)
    return rating

# ----- PROPUESTO: DECORADOR CONTADOR -------

def cantidad_consultas(consulta):
    """
    Recuerda que esta consulta es necesario solo si hiciste el decorador.
    """
    pass


if __name__ == "__main__":
    """
    ========= ZONA DE PRUEBAS ========
    Si deseas hacer tus propias pruebas puedes comentar esta sección
    y realizarla más abajo. NO recomendamos que la borres.
    """

    consultas = {
        "1": (usuarios_por_antiguedad, False, ["usuarios"], "usuarios_por_antiguedad"),
        "2": (ratings_usuarios, True, ["ratings"], "ratings_usuarios"),
        "3": (canciones_artistas, True, ["canciones", "artistas"], "canciones_artistas"),
        "4": (rating_promedio, True, ["canciones", "ratings"], "rating_promedio")
    }

    db_func = {
        "canciones": (leer_canciones, os.path.join("data_base", "canciones.csv")),
        "artistas": (leer_artistas, os.path.join("data_base", "artistas.csv")),
        "usuarios": (leer_usuarios, os.path.join("data_base", "usuarios.csv")),
        "ratings": (leer_ratings, os.path.join("data_base", "ratings.csv"))
    }

    with open("tests.txt", "r", encoding="utf-8") as file:
        for line in file.readlines():
            test = line.strip().split(";")
            consulta = consultas[test[0]]
            args = []

            if consulta[1]:
                args.append(test[1])

            for db in consulta[2]:
                tup = db_func[db]
                args.append(tup[0](tup[1]))
            
            respuesta = consulta[0](*args)
            print(f"\n--- Realizando consulta: {consulta[3]}{' - ' + test[1] if test[1] != '' else ''} ---")
            if test[2] == "0":
                print(respuesta)
            else:
                for i in range(int(test[2])):
                    try:
                        print(respuesta.__next__())
                    except StopIteration:
                        break

    # ----- PROPUESTO: DECORADOR CONTADOR -------
    
    print("\n--- Estadisticas de las consultas ---")
    nombres_consultas = [consulta[3] for consulta in consultas.values()]
    for consulta in nombres_consultas:
        print(consulta, ":", cantidad_consultas(consulta))

    """
    ========== FIN ZONA DE PRUEBAS ==========
    """