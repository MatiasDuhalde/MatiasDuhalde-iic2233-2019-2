def reparar_comunicacion(ruta):
    """
    Recibe la ruta del archivo visual a reparar.
    Escribe los bits procesados en el archivo Docengelion.bmp
    """
    with open(ruta, 'rb') as bytes_file:
        # Procesar los bytes corrompidos
        byte_string = bytes_file.read()
        modified_bytes = bytearray()
        for i in range(0, len(byte_string), 16):
            chunk = bytearray(byte_string[i:i+16])
            # Utilizar el primer byte del chunk como pivote
            pivote = chunk[0]
            # Eliminar todos aquellos bytes del chunk cuyo valor numérico sea
            # mayor o igual al pivote
            chunk = bytearray(byte for byte in chunk if byte < pivote)
            modified_bytes += chunk

    with open('Docengelion.bmp', 'wb') as bytes_file:
        # Guardar los bytes arreglados
        bytes_file.write(modified_bytes)

if __name__ == '__main__':
    try:
        reparar_comunicacion('EVA.xdc')
        print("PINTOSAR201: Comunicacion con pilotos ESTABLE")
    except Exception as error:
        print(f'Error: {error}')
        print("PINTOSAR301: CRITICO pilotos incomunicados DESCONEXION INMINENTE")
