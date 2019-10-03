from carga_archivos import cargar_datos
from dcconductor import DCConductor
from excepcion_patente import ErrorPatente

'''
Para cada uno de los conductores chequea si su información está correcta.
Si no está correcta, se informa en pantalla que el conductor no pudo ser
registrado y la razón, y si no, se informa que fue inscrito exitosamente.
En este archivo la idea es capturar y manejar las excepciones.
También deberás contar la cantidad total de errores.
'''

registro_oficial, conductores = cargar_datos("regiztro_ofizial.json", "conductores.csv")
registro_oficial, conductores = cargar_datos("registro_oficial.json", "conductores.csv")

dcconductor = DCConductor(registro_oficial, conductores)

'''
Editar desde aquí
'''
if registro_oficial and conductores:
    contador = 0
    for conductor in dcconductor.conductores:
        is_valid = True
        
        try:
            dcconductor.chequear_celular(conductor)
        except ValueError as err:
            print(f"Error: {err}")
            is_valid = False
            contador += 1
        
        try:
            dcconductor.chequear_rut(conductor)
        except:
            print(f"Error: {err}")
            is_valid = False
            contador += 1
        
        try:
            dcconductor.chequear_nombre(conductor)
        except:
            print(f"Error: {err}")
            is_valid = False
            contador += 1
        
        try:
            dcconductor.chequear_patente(conductor)
        except ErrorPatente as err:
            print(f"Error: {err}")
            is_valid = False
            contador += 1
        
        if is_valid:
            dcconductor.seleccionados.append(conductor)
