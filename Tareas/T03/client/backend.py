"""
Funcionamiento de la parte de usuario del programa
"""

class Backend():
    """
    Esta clase maneja el funcionamiento del programa client-side.
    """

    @staticmethod
    def handle_gui_signal(dict_):
        """
        Revisa un estado enviado desde el frontend al cliente.
        new_dict["send"] determina si el estado será enviado al server o no.

        Retorna otro diccionario que será enviado al server.
        """
        new_dict = {
            "username": dict_["username"],
            "command": dict_["command"],
            "send": False
        }
        if not "username" is None:
            new_dict["send"] = True
        return new_dict
