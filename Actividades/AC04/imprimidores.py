from threading import Thread, Lock
from utils import reloj
import random

lock_imprimir = Lock()

class Imprimidor(Thread):

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__(name=nombre, target=self.run)
        self.berlin = berlin
        self.bolsa_dinero = bolsa_dinero

    def run(self):
        '''
        Funcionalidad de Imprimidor que imprime dinero cada 5 minutos, cada
        iteración chequea si se cumple que hay problema con el dinero (20%)
        '''
        while not self.bolsa_dinero.dinero_listo.is_set():
            reloj(5)
            listo = self.imprimir_dinero(random.randint(100000, 500000))
            self.problema_papel()

    def imprimir_dinero(self, dinero):
        '''
        Llamar a este método para imprimir dinero.
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param dinero:
        :return:
        '''
        with lock_imprimir:
            print(f"{self.name}: imprimiendo €{dinero}.") 
            self.bolsa_dinero.dinero_acumulado += dinero
            if self.bolsa_dinero.dinero_acumulado >= self.bolsa_dinero.meta_dinero:
                print(f"{self.name}: Dinero listo!")   
                self.bolsa_dinero.dinero_listo.set()
            print(f"{self.name}: hay €{self.bolsa_dinero.dinero_acumulado} en la bolsa.")
        

    def problema_papel(self):
        '''
        Probabilidad de problema con el papel de 20%
        '''
        if random.random() <= 0.20:
            self.berlin.acquire()
            print(f"{self.name}: problema con papel!")   
            reloj(10)
            print(f"{self.name}: problema solucionado!") 
            self.berlin.release()

