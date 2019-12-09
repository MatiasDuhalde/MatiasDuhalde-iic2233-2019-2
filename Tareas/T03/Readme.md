# Tarea 03: DCClub :school_satchel:

## Consideraciones generales :octocat:

Si bien no se pudo hacer todo lo pedido en el enunciado y la pauta, el programa es ejecutable y se puede acceder a todas las ventanas y funcionalidades base. Para hacer uso del programa, antes de ejecutarlo hay que asegurarse que se encuentren los archivos entregados que, de acuerdo al enunciado, no vienen en el repositorio. Estos son ```amigos.json``` y ```usuarios.json``` los cuales deben ir en el directorio ```./server/```, y todos los elementos gráficos de la interfaz, esto es, la carpeta `sprites` y todos sus contenidos, los cuales deben ser ubicados en el directorio base. La forma de partir el programa se explica en el apartado de [ejecución](https://github.com/IIC2233/MatiasDuhalde-iic2233-2019-2/tree/master/Tareas/T03#ejecuci%C3%B3n-computer)

### Cosas implementadas y no implementadas :white_check_mark: :x:

La pauta se encuentra [aquí](https://docs.google.com/spreadsheets/d/10NghnXWn9wzEYtm6kFUrG1616janfOSROJ-4z9pqbhE/edit).

* **Networking**: Hecha completa.
    * Protocolo: :heavy_check_mark:
    * Correcto uso de sockets: :heavy_check_mark:
    * Conexión: :heavy_check_mark:
    * Manejo de Clientes: :heavy_check_mark:
* **Arquitectura Cliente - Servidor**: Hecha parcialmente.
    * Roles
    * Consistencia
    * Logs
* **Manejo de Bytes**: No implementado
    * Codificación
    * Decodificación
    * Integración
* **Interfaz gráfica**: Hecha completa (con ciertos detalles).
    * Modelación
    * Ventana de inicio
    * Ventana principal
    * Ventana de chat
* **Grafo**: Hecha completa (con detalles)
    * Archivo
    * Amistades
    * Consultas
    * Integración
* **General**: Hecha completa (con detalles)
    * Parámetros (JSON) :heavy_check_mark:
        * Se creó un módulo extra `parámetros.py` (en `server` y `client`) para poder extraer los parámetros del archivo JSON. Este módulo crea el diccionario `PARAMETROS` que es importado para ser ocupado en las otras partes del programa
* **:sparkles:Bonus:sparkles:**: Hecho parcialmente.
    * Foto de perfil :x:
    * Regex :heavy_check_mark:
    * Palabras bobba :x:
    * Movimiento personaje :x:
    * Mensaje con foto :x:
    * DCCMascota :x:
    * DCCPalabra :x:
    * Robustez :heavy_check_mark:

## Ejecución :computer:

Como el foco de esta tarea era *Networking*, el programa se divide en dos partes una del servidor (en `./server/`) y otra del cliente (en `./client/`). El archivo principal a ejecutar en ámbas partes es `main.py`. Para que funcione el programa, ámbos archivos deben ser ejecutados desde sus respectivos directorios, **no desde el directorio base**. Se debe primero iniciar el server, dado que si se inicia primero el cliente y no se puede detectar el servidor, el programa terminará, informando al usuario.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. `PyQt5`: Varias funciones y clases / Usado sólo en la parte `client`, en los archivos `gui_*.py` (elementos gráficos), `main.py`, y `client.py` (app y señales). **Debe instalarse**
2. ```threading```: Usado para implementar comportamiento paralelo en el uso de sockets, mediante `Locks` y `Threads`, en `client.py` y `server.py`
3. `socket`: Base de *Networking* usada en `client.py` y `server.py`
4. `pickle`: Serializar los mensajes de acuerdo al protocolo de envío, usada en `client.py` y `server.py`
5. `json`: Lectura y escritura de archivos en formato `JSON` usado en `parametros.py`
6. `time`: Usado en los logs de `client.py` y `server.py`
7. `random`: `choice`, para elegir un fondo random (ver consideraciones) en `gui_principal.py`
8. `os`: `path.join`, trabajo con paths en `parametros.json`
9. `re`: `match`, detección de comandos usando expresiones regulares en `server_backend.py`

**Nota:** se importa `sys` pero no se usa, se me olvidó quitarlo

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```parametros```: Carga los archivos `parametros.json`. Posee el diccionario ```PARAMETROS```, que guarda sus contenidos. En `client` y `server`.
2. `backend`: Contiene un método que ayuda a manejar los comandos recibidos desde la interfaz. En `client`.
3. `client`: Funcionamiento base del *Networking* del programa client-side. En `client`.
4. `gui_chat`: Interfaz ventana de chat. En `client`.
5. `gui_error`: Interfaz ventana de error. En `client`.
6. `gui_inicio`: Interfaz ventana de inicio. En `client`.
7. `gui_principal`: Interfaz ventana principal. En `client`.
8. `rooms`: Modela las salas de chat. En `client` y `server`.
9. `usuarios`: Modela los usuarios, cada uno referenciando a sus amigos (estructura de nodos). En `client` y `server`.
10. `server`: Funcionamiento base del *Networking* del programa server-side. En `server`.
11. ``server_backend`: Contiene métodos auxiliares que ayudan a procesar los mensajes recibidos desde en cliente. En `server`.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En el pié de página de la página 7 del enunciado se comenta que el botón (X) también puede ser valido para volver a la ventana de inicio. Personalmente decidí añadir un botón aparte para volver a la ventana de inicio. El botón (X) sigue con su comportamiento normal, es decir, cerrar la aplicación client-side.
2. `server` y `client` tienen algunas librerías que son idénticas entre sí. Estas son `parametros`, `rooms`, y `usuarios`. Me pareció que copiarlos y pegarlos en cada directorio por separado se apegaba mejor a una arquitectura server-client que hacer que ámbos importaran desde un directorio externo. Si se va a revisar el código de estas librerías solo basta con revisar un lado (`server` o `client`), ya que ámbas tienen el mismo contenido.
3. 

## Referencias de código externo :book:

1. Base inicialmente mi código en la estructura que ocupa la ayudantía 08 ([Japonizador](https://github.com/IIC2233/syllabus/tree/master/Ayudantias/AY08/Ejemplo%20json%20(Japonizador))), por si es que existe alguna similitud.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
