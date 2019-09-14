import lib.gametext as gametext
from random import random

def carrera(piloto, vehiculo, pista, menuCarrera, menuPits):
    vuelta = 1
    contrincantes = pista.contrincantes
    while vuelta <= pista.número_vueltas:
        print(f"VUELTA {vuelta} de {pista.número_vueltas}")
        
        for contrincante in contrincantes:
            pass
        
        actions = {1 : "Entrar a los pits", 0 : "Volver al menú principal"}
        string = gametext.SEP + f"EVENTOS VUELTA {vuelta}"
        
        user_input = menuCarrera.recibir_input(actions=actions, to_print=string)
        if user_input == 0:
            menuCarrera.active = False
            return None
        
        vueltas += 1