import lib.gametext as gametext
import lib.funciones as f
from random import random

def carrera(piloto, vehiculo, pista, menuCarrera, menuPits):
    vuelta = 1
    contrincantes = pista.contrincantes
    destruido = False
    # Makes sure all vehicles start repaired
    for car in map(lambda x: x.vehiculo, contrincantes):
        car.reset_parameters()

    while vuelta <= pista.número_vueltas:
        f.clear()
        print(gametext.SEP)
        print("{:^79}".format(f"VUELTA {vuelta} de {pista.número_vueltas}\n"))
        print(gametext.SEP2)
        accidentados = []

        # Get damage
        daño = f.calcular_daño(vehiculo, pista)
        vehiculo.chasis_actual -= daño
        if daño == 0:
            print("No has recibido daño esta vuelta")
        else:
            porcentaje = vehiculo.chasis_actual//vehiculo.chasis
            print(f"Recibiste {daño} de daño esta vuelta")
            print(f"Chasis: {vehiculo.chasis_actual} %{porcentaje}")
            if vehiculo.chasis_actual <= 0:
                print("Sufriste muchos daños!")
                destruido = True
                accidentados.append(vehiculo)
        
        for contrincante in contrincantes:
            contrincante.vehiculo.chasis_actual -= f.calcular_daño( \
            contrincante.vehiculo, pista)
            if contrincante.vehiculo.chasis_actual <= 0:
                print(f"{contrincante.nombre} ha sufrido muchos daños!")
                accidentados.append(vehiculo)
                contrincantes.remove(contrincante)
        
        print('\n' + gametext.SEP2 + '\n')

        # Calculate accident
        if random() < f.probabilidad_accidentes(piloto, vehiculo, pista, \
        vuelta) and not destruido:
            print("Has sufrido un accidente!")
            destruido = True
            accidentados.append(vehiculo)

        for contrincante in contrincantes:
            if random() < f.probabilidad_accidentes(contrincante, \
            contrincante.vehiculo, pista, vuelta):
                print(f"Contrincante {contrincante.nombre} ha sufrido un accidente!")
                accidentados.append(contrincante.vehiculo)
                contrincantes.remove(contrincante)

        # Get times
        
        # Update times
        vehiculo.tiempo_anterior = vehiculo.tiempo_acumulado
        for contrincante in contrincantes:
            contrincante.vehiculo.tiempo_anterior = contrincante.vehiculo.tiempo_acumulado
        vehiculo.tiempo_acumulado += f.tiempo_vuelta(piloto, vehiculo, pista, vuelta)
        
        # Calculate new times
        if not destruido:
            vehiculo.tiempo_acumulado += f.tiempo_vuelta(piloto, vehiculo, \
            pista, vuelta)
        for contrincante in contrincantes:
            tiempo = f.tiempo_vuelta(contrincante, contrincante.vehiculo, pista, vuelta)
            contrincante.vehiculo.tiempo_acumulado += tiempo
        vehiculo.tiempo_acumulado += f.tiempo_vuelta(piloto, vehiculo, pista, vuelta)
        
        print('\n' + gametext.SEP2 + '\n')
        
        # Show positions
        if not destruido and contrincantes:
            participantes = [vehiculo, *list(map(lambda x: x.vehiculo, \
            contrincantes))]
            participantes.sort(key=lambda x: x.tiempo_acumulado)
            print("Posiciones:")
            # 9 chars
            print("{:2} | {:38.38} | {:15} | {:15}".format("N°", "Nombre", \
            "Tiempo Vuelta", "Tiempo Acumulado"))
            for index in range(1, len(participantes) + 1):
                print("{:2} | {:38.38} | {:15} | {:15}".format(index, \
                participantes[index - 1].dueño, \
                participantes[index - 1].tiempo_acumulado - \
                participantes[index - 1].tiempo_anterior, \
                participantes[index - 1].tiempo_acumulado))
            

        # Get money

        print('\n' + gametext.SEP2 + '\n')

        # Show desqualified
        if not accidentados:
            print("No hubo competidores descalificados en esta vuelta.")
        else:
            print("Competidores descalificados")
            for car in accidentados:
                print(f" - {car.dueño}")
        
        # go to pits option
        if not destruido:
            actions = {1 : "Siguiente vuelta", 
            2 : "Entrar a los pits", 0 : "Volver al menú principal"}
            string = menuCarrera.get_str(actions=actions)
            print(string)
            user_input = menuCarrera.recibir_input(actions=actions, to_print=string)
            if user_input == 0:
                menuCarrera.active = False
                return None
            elif user_input == 2:
                print("GOING TO THE PITS!")
                pass
        else:
            print(gametext.LOSE_TITLE)
            input("Presione ENTER para volver al menú principal...")
            return None
        vuelta += 1