from threading import Thread, Lock
from utils import reloj
import random



class Excavador(Thread):

    lock_avanzar = Lock()

    def __init__(self, nombre, berlin, tunel):
        super().__init__(name=nombre, target=self.run)
        self.berlin = berlin
        self.tunel = tunel

    def run(self):
        '''
        Funcionalidad de Excavador que crea x metros de túnel cada 10 min,
        cada iteración chequea si se cumple que hay problema con la picota (10%)
        '''
        while not self.tunel.tunel_listo.is_set():
            reloj(10)
            self.avanzar(random.randint(50,100))
            self.problema_picota()

    def problema_picota(self):
        '''
        Probabilidad de problema con la picota de 10%
        Se llama a berlin para resolverlo
        '''
        if random.random() <= 0.10:
            self.berlin.acquire()
            print(f"{self.name}: problema con picota!")
            reloj(5)
            print(f"{self.name}: problema solucionado!")
            self.berlin.release()


    def avanzar(self, metros):
        '''
        Usar este método para avanzar en la excavación del túnel
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param metros: int
        '''
        with self.lock_avanzar:
            print(f"{self.name}: avanzando {metros} metros.")
            self.tunel.metros_avanzados += metros
            if self.tunel.metros_avanzados >= self.tunel.largo:
                print(f"{self.name}: tunel listo!")
                self.tunel.tunel_listo.set()
            print(f"{self.name}: el tunel lleva {self.tunel.metros_avanzados} metros.")
            
