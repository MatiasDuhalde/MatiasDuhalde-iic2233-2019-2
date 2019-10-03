import csv
from conductores import Conductor
from excepcion_patente import ErrorPatente
import os

class DCConductor:

    def __init__(self, registro_oficial, conductores):
        '''
        El constructor crea las estructuras necesarias para almacenar los datos
         proporcionados, recibe la información necesaria para el funcionamiento de la clase.
        '''
        self.registro_oficial = registro_oficial
        self.conductores = conductores
        self.seleccionados = list()


    def chequear_rut(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su rut no siga
        el formato correcto
        '''
        if "." in conductor.rut:
            raise ValueError(f"El rut {conductor.rut} no debe contener puntos.")
        if conductor.rut.count('-') != 1:
            raise ValueError(f"El rut {conductor.rut} debe contener un solo guión.")
        numero, digito_verificador = conductor.rut.split('-')
        if not (len(digito_verificador) == 1 and 
        (digito_verificador.isdecimal() or digito_verificador.upper() == "K")):
            raise ValueError(f"El dígito verificador {digito_verificador} " +
                "no es válido.")
        if not(numero.isdecimal() and int(numero) >= 10000000):
            raise ValueError(f"El número {numero} no es válido.")



    def chequear_nombre(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su nombre no
        exista en el registro oficial.
        '''
        if not conductor.nombre in self.registro_oficial.keys():
            raise(NameError(f"{conductor.nombre} no está en el registro oficial."))


    def chequear_celular(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su celular
        no siga el formato correcto
        '''
        if len(conductor.celular) != 9:
            raise ValueError(f"El teléfono {conductor.celular} debe tener 9 dígitos.")
        if not conductor.celular.isdecimal():
            raise ValueError(f"El teléfono {conductor.celular} no es válido.")
        if conductor.celular[0] != "9":
            raise ValueError(f"El teléfono {conductor.celular} debe comenzar por un 9.")


    def chequear_patente(self, conductor):
        '''
        Recibe un conductor y levanta una excepción en caso de que su patente no
        coincida con la información del registro oficial.
        '''
        patente_oficial = self.registro_oficial[conductor.nombre]
        if patente_oficial != conductor.patente:
            raise ErrorPatente(conductor, patente_oficial)
