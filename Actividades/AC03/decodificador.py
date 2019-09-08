from itertools import chain


def decodificar(string):
    CODEWORD = "arquetipos"
    CLAVE = {str(i): CODEWORD[i] for i in range(len(CODEWORD))}
    CLAVE = dict(CLAVE, **{val : key for key, val in CLAVE.items()})
    string = ''.join([CLAVE[i] if i in CLAVE.keys() else i for i in string])
    return string


if __name__ == "__main__":
    tests = [
        "66cqquu", 
        "P18g10m0c68n 0v0nz0d0 qaro-q",
        "E950 49 3n0 7134b0 d4l d4c8d6f6c0d81",
        "S6 734d49 l441 4958, 58d8 h0 90l6d8 m3y b64n!!"]


    print("  ---  PRUEBA DE DECODIFICADO ---  ")
    for test in tests:
        print(decodificar(test), "\n")