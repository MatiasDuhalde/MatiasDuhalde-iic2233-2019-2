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
        base_dict = {
            "command": dict_["command"],
            "send": False
        }
        if base_dict["command"] == "login":
            base_dict.update({
                "username": dict_["username"],
                "send": True
            })
        elif base_dict["command"] == "start":
            base_dict.update({
                "user": dict_["user"]
            })
        elif base_dict["command"] == "logout":
            base_dict.update({
                "send": True
            })
        elif base_dict["command"] == "enter":
            base_dict.update({
                "send": True,
                "room": dict_["room"]
            })
        elif base_dict["command"] == "enter_text":
            base_dict.update({
                "send": True,
                "room": dict_["room"],
                "text": dict_["text"]
            })
        return base_dict
