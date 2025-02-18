import lib.gametext as gametext
import lib.funciones as f
import lib.parametros as pm
from random import random
from math import floor, ceil
from lib.entidades import Automovil, Motocicleta, Troncomovil, Bicicleta

def pits(piloto, vehiculo, menuPits):
    f.clear()
    # Se agrega el tiempo que tardan los pits
    vehiculo.ultima_vuelta += f.tiempo_pits(vehiculo)

    vehiculo.reparar()
    print(gametext.SEP3 + "\n{:^79}\n".format("VEHÍCULO REPARADO!") + gametext.SEP3)
    input("Presione ENTER para continuar...")
    power = "ZAPATILLAS" if type(vehiculo) in [Troncomovil, Bicicleta] else "MOTOR"
    while True:
        f.clear()
        print(menuPits)
        user_input = menuPits.recibir_input()
        if user_input == 1:
            if piloto.dinero < pm.MEJORAS['CHASIS']['COSTO']:
                print("No tienes el dinero suficiente para esta mejora.")
                input("Presione ENTER para continuar...")
            else:
                piloto.dinero -= pm.MEJORAS['CHASIS']['COSTO']
                vehiculo.zapatillas *= pm.MEJORAS['CHASIS']['EFECTO']

        elif user_input == 2:
            if piloto.dinero < pm.MEJORAS['CARROCERIA']['COSTO']:
                print("No tienes el dinero suficiente para esta mejora.")
                input("Presione ENTER para continuar...")
            else:
                piloto.dinero -= pm.MEJORAS['CARROCERIA']['COSTO']
                vehiculo.zapatillas *= pm.MEJORAS['CARROCERIA']['EFECTO']

        elif user_input == 3:
            if piloto.dinero < pm.MEJORAS['RUEDAS']['COSTO']:
                print("No tienes el dinero suficiente para esta mejora.")
                input("Presione ENTER para continuar...")
            else:
                piloto.dinero -= pm.MEJORAS['RUEDAS']['COSTO']
                vehiculo.zapatillas *= pm.MEJORAS['RUEDAS']['EFECTO']

        elif user_input == 4:
            if piloto.dinero < pm.MEJORAS[power]['COSTO']:
                print("No tienes el dinero suficiente para esta mejora.")
                input("Presione ENTER para continuar...")
            else:
                piloto.dinero -= pm.MEJORAS[power]['COSTO']
                if power == "MOTOR":
                    vehiculo.motor *= pm.MEJORAS[power]['EFECTO']
                elif power == "ZAPATILLAS":
                    vehiculo.zapatillas *= pm.MEJORAS[power]['EFECTO']

        elif user_input == 0:
            break
    vehiculo.reparar()


def carrera(piloto, vehiculo, pista, menuCarrera, menuPits):
    vuelta = 1
    contrincantes = pista.contrincantes
    destruido = False
    # Makes sure all vehicles start repaired
    vehiculo.reset_parameters()
    for car in map(lambda x: x.vehiculo, contrincantes):
        car.reset_parameters()

    # Contains all active vehicles
    participantes = [vehiculo, *list(map(lambda x: x.vehiculo, contrincantes))]

    while vuelta <= pista.número_vueltas:
        f.clear()
        print(gametext.SEP)
        print("{:^79}".format(f"VUELTA {vuelta} de {pista.número_vueltas}\n"))
        print(gametext.SEP2)
        # Contains disabled vehicles in THIS LAP
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
                participantes.remove(vehiculo)
        hipotermia = f.hipotermia(piloto, vehiculo, pista, vuelta)
        if hipotermia != 0:
            print(f"Estás sufriendo una hipotermia de grado {hipotermia}.")


        for contrinc in contrincantes:
            contrinc.vehiculo.chasis_actual -= f.calcular_daño( \
            contrinc.vehiculo, pista)
            if contrinc.vehiculo.chasis_actual <= 0:
                print(f"{contrinc.nombre} ha sufrido muchos daños!")
                accidentados.append(contrinc.vehiculo)
                contrincantes.remove(contrinc)
                participantes.remove(contrinc.vehiculo)
        
        print('\n' + gametext.SEP2 + '\n')

        # Calculate accident
        if random() < f.probabilidad_accidentes(piloto, vehiculo, pista, \
        vuelta) and not destruido:
            print("Has sufrido un accidente!")
            destruido = True
            accidentados.append(vehiculo)
            participantes.remove(vehiculo)

        for contrinc in contrincantes:
            if random() < f.probabilidad_accidentes(contrinc, \
            contrinc.vehiculo, pista, vuelta):
                print(f"Contrincante {contrinc.nombre} ha sufrido un accidente!")
                accidentados.append(contrinc.vehiculo)
                contrincantes.remove(contrinc)
                participantes.remove(contrinc.vehiculo)

        # Get times
        if not destruido:
            vehiculo.ultima_vuelta += f.tiempo_vuelta(piloto, vehiculo, pista, \
            vuelta)
            vehiculo.tiempo_acumulado += vehiculo.ultima_vuelta
        for contrinc in contrincantes:
            contrinc.vehiculo.ultima_vuelta = f.tiempo_vuelta(contrinc, \
            contrinc.vehiculo, pista, vuelta)
            contrinc.vehiculo.tiempo_acumulado += contrinc.vehiculo.ultima_vuelta
        
        print('\n' + gametext.SEP2 + '\n')
        
        # Show positions
        if not destruido or contrincantes:
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
            
        print(gametext.SEP2 + '\n')

        # Get money
        if not destruido:
            participantes.sort(key=lambda x: x.ultima_vuelta)
            if vehiculo.ultima_vuelta == participantes[0].ultima_vuelta:
                ganancias = f.dinero_vuelta(pista, vuelta)
                print(f"Vuelta más rápida! Obtuviste ${ganancias}")
                piloto.dinero += ganancias

        print(gametext.SEP2 + '\n')

        # Show desqualified
        if not accidentados:
            print("No hubo competidores descalificados en esta vuelta.")
        else:
            print("Competidores descalificados")
            for car in accidentados:
                print(f" - {car.dueño}")
        
        print(gametext.SEP2 + '\n')
        
        # go to pits option
        # END OF LAP HERE
        if vuelta != pista.número_vueltas:
            if not destruido:
                actions = {1 : "Siguiente vuelta", 
                2 : "Entrar a los pits", 0 : "Volver al menú principal"}
                string = menuCarrera.get_str(actions=actions)
                print(string)
                user_input = menuCarrera.recibir_input(actions=actions, \
                to_print=string)
                vehiculo.ultima_vuelta = 0
                if user_input == 0:
                    menuCarrera.active = False
                    return None
                elif user_input == 2:
                    
                    # PITS

                    pits(piloto, vehiculo, menuPits)

            else:
                print(gametext.LOSE_TITLE + '\n')
                input("Presione ENTER para volver al menú principal...")
                return None
        else:
            participantes.sort(key=lambda x: x.tiempo_acumulado)
            # Tie at first place also gives a win
            if participantes[0].tiempo_acumulado != vehiculo.tiempo_acumulado \
            or destruido:
                print(gametext.LOSE_TITLE + '\n')
                input("Presione ENTER para volver al menú principal...")
                return None
            else:
                print(gametext.WIN_TITLE + '\n')

                # Get prize money
                ultimo_lugar = participantes[-1]
                ganancias = f.dinero_ganador(pista)
                piloto.dinero += ganancias

                xp = f.experiencia_recibida(piloto, pista, \
                primero=vehiculo, ultimo=ultimo_lugar)
                piloto.experiencia += xp
                print("Primer Lugar!")
                print(f"Obtuviste ${ganancias} y {xp} puntos de experiencia")
                input("Presione ENTER para volver al menú principal...")

                return None
            
        
        vuelta += 1
