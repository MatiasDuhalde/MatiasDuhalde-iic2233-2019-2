from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        super().__init__(id_cliente, nombre, contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.saldo

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        '''
        Completar: Recuerda que si el saldo es menor a 0, entonces este cliente
        si tiene un fraude
        '''
        self.saldo = nuevo_saldo
        if self.saldo < 0:
            self.tiene_fraude = True

    def deposito_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            saldo_anterior = self.saldo
            self.depositar(dinero)
            print("depositar", self.id_cliente, saldo_anterior, self.saldo, 
            sep=",", file=archivo)

    def retiro_seguro(self, dinero):
        '''
        Completar: Recuerda marcar a los clientes que cometan fraude. A modo de ayuda:
        Ten en cuenta que las properties de ClienteSeguro ya se encargan de hacer esto
        '''
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            saldo_anterior = self.saldo
            self.retirar(dinero)
            print("retirar", self.id_cliente, saldo_anterior, self.saldo, 
            sep=",", file=archivo)


class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        super().__init__()

    def cargar_clientes(self, ruta):
        with open(ruta, "r", encoding="UTF-8") as file:
            for line in file:
                id_cliente, nombre, saldo, contrasena = line.strip().split(",")
                # Notar que dejamos el id como string, no hay problema
                # mientras se sea consistente
                instancia_cliente = ClienteSeguro(id_cliente, nombre,
                                            contrasena)
                self.clientes.append(instancia_cliente)

    def realizar_transaccion(self, id_cliente, dinero, accion):
        for customer in self.clientes:
            if customer.id_cliente == id_cliente:
                if accion == "depositar":
                    customer.deposito_seguro(dinero)
                elif accion == "retirar":
                    customer.retiro_seguro(dinero)
                break

    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        for linea in historial:
            id_cliente, accion, monto = linea.split(",")
            monto = int(monto)
            self.realizar_transaccion(id_cliente, monto, accion)

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        # completar
        print(ruta)
