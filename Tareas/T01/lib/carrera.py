import lib.gametext as gametext
import lib.funciones as f
from random import random
from math import floor, ceil

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
        vehiculo.chasis_actual = max(vehiculo.chasis_actual - daño, 0)
        if daño == 0:
            print("No has recibido daño esta vuelta")
        else:
            porcentaje = floor((vehiculo.chasis_actual/vehiculo.chasis)*100)
            print(f"Recibiste {daño} de daño esta vuelta")
            print(f"Chasis: {vehiculo.chasis_actual} ({porcentaje}%)")
            if vehiculo.chasis_actual <= 0:
                print("Sufriste muchos daños!")
                destruido = True
                accidentados.append(vehiculo)
        
        for contrinc in contrincantes:
            contrinc.vehiculo.chasis_actual -= f.calcular_daño( \
            contrinc.vehiculo, pista)
            if contrinc.vehiculo.chasis_actual <= 0:
                print(f"{contrinc.nombre} ha sufrido muchos daños!")
                accidentados.append(vehiculo)
                contrincantes.remove(contrinc)
        
        print('\n' + gametext.SEP2 + '\n')

        # Calculate accident
        if random() < f.probabilidad_accidentes(piloto, vehiculo, pista, \
        vuelta) and not destruido:
            print("Has sufrido un accidente!")
            destruido = True
            accidentados.append(vehiculo)

        for contrinc in contrincantes:
            if random() < f.probabilidad_accidentes(contrinc, \
            contrinc.vehiculo, pista, vuelta):
                print(f"Contrincante {contrinc.nombre} ha sufrido un accidente!")
                accidentados.append(contrinc.vehiculo)
                contrincantes.remove(contrinc)

        # Get times
        if not destruido:
            vehiculo.ultima_vuelta = f.tiempo_vuelta(piloto, vehiculo, pista, \
            vuelta)
            vehiculo.tiempo_acumulado += vehiculo.ultima_vuelta
        for contrinc in contrincantes:
            contrinc.vehiculo.ultima_vuelta = f.tiempo_vuelta(contrinc, \
            contrinc.vehiculo, pista, vuelta)
            contrinc.vehiculo.tiempo_acumulado += contrinc.vehiculo.ultima_vuelta
        
        print('\n' + gametext.SEP2 + '\n')
        
        # Show positions
        if not destruido or contrincantes:
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
                participantes[index - 1].ultima_vuelta, \
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
            print(gametext.LOSE_TITLE + '\n')
            input("Presione ENTER para volver al menú principal...")
            return None
        vuelta += 1