# Tarea 2: DCCampo

## Consideraciones generales :octocat:

Si bien no se pudo hacer todo lo de la pauta, el programa es ejecutable y se puede acceder a todas las ventanas pedidas. El detalle de lo implementado y no implementado está en la siguiente sección.
Para hacer uso del programa, antes de ejecutarlo hay que asegurarse que se encuentren los archivos entregados que, de acuerdo al enunciado, no vienen en el repositorio (i.e. ```parametros_acciones.py```, ```parametros_plantas.py```, y ```parametros_precios.py```) y los directorios conteniendo los sprites (i.e. ```/sprites/```). Solo hice uso de los sprites proporcionados, por lo que no hay que agregar nada extra. Una vez hecho esto, solo basta ejecutar el archivo principal, y el programa parte inmediatamente en el **menú de inicial**.

### Cosas implementadas y no implementadas :white_check_mark: :large_blue_circle: :x: 

La pauta se encuentra [aquí](https://docs.google.com/spreadsheets/d/1ZbDvQttRDK--0EIfqrPCtl-3OwJgd1kMu9bagGJb-7Q/edit#gid=2067244711).

* **Ventanas**: Hecha completa (con ciertos detalles).
    * Ventana de Inicio: :heavy_check_mark:
    * Ventana de juego: :large_blue_circle: :warning:
        * **(Punto 2)** El inventario del frontend es estático, los elementos visuales no cambian dependiendo de las compras (el inventario del backend si es actualizable).
        * **(Punto 3)** Si bien existe la barra de energía, no se implementaron algunas acciones que afectan su estado (el detalle más adelante)
    * Inventario: :heavy_check_mark: :heavy_check_mar
    * Tienda: :heavy_check_mark:
* **Entidades**: Hecha parcialmente.
    * Jugador: :large_blue_circle:  :warning:
        * **(Punto 2)** Como se informó antes, se implementó la barra de energía, pero no se implementaron las acciones que provocan su cambio.
        * **(Punto 3)** No se pueden recoger recursos.
    * Recursos: :x: 
    * Herramientas: :large_blue_circle: 
        * No se implementaron los árboles, pero el programa **si** revisa si es que el usuario compró una azada para arar.
* **Tiempo**: No implementado
    * Reloj: :x:
* **Funcionalidades Extra**: Hecha completa (con ciertos detalles).
    * K+I+P: :heavy_check_mark: :warning:
    * M+N+Y: :heavy_check_mark: :warning:
    * Pausa: :large_blue_circle: 
        * Si bien se puso un botón de pausa, este no hace nada, debido a que no se implementó el reloj.
* **General**: Hecha completa (con detalles)
    * Modularización: :heavy_check_mark:
    * Dependencia circular: :heavy_check_mark:
    * Archivos: :heavy_check_mark:
    * Consistencia: :heavy_check_mark:
    * `parametros.py` :heavy_check_mark:
* **:sparkles:Bonus:sparkles:**: No implementado
    * Pesca: :x:
    * Casa: :x:

**Nota**: aquellas líneas marcadas con :warning:, tienen detalles extra en [supuestos y consideraciones adicionales](#Supuestos-y-consideraciones-adicionales-:thinking:).

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  [```main.py```](main.py).
Los archivos necesarios deben estar en sus respectivos directorios, según se indica en el inicio de este documento.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: Varias y más de las funciones hechas en clases, en todos los módolos creados.
2. ```os```: ```path.join()```
3. ```sys```: ```exit()```
4. ```time```: ```sleep()```
5. ```random```: ```choice()```
6. ```itertools```: ```cycle()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```backend```: Contiene `BackendInicio`, el backend de la ventana de inicio
2. ```frontend```: Contiene `DraggableLabel` (del *drag and drop*), `VentanaPrincipal` y `MainGame`, elementos del frontend del mapa principal.
3. ```main```: Archivo principal
4. ```mapa```: Contiene la clase `Mapa`, y sus tipos de tiles. Construye el mapa.
6. ```parametros_generales```: Contiene los parámetros pedidos en el enunciado y algunos extra (ver consideraciones)
7. ```player```: Contiene la clase `Player`, y corresponde al backend del jugador (Enzo).
8. ```ventana_inicio```: Contiene las clases `VentanaInicio` y `WidgetCargar`, que corresponden al frontend de la ventana de inicio.
8. ```ventana_tienda```: Contiene las clases `VentanaTienda` y `WidgetTienda`, que corresponden al frontend de la ventana de tienda.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. :warning: Hice los pastos tal que exista una cierta continuidad en los bordes, pero algunos casos de adyacencia no se implementaron y se toma otro sprite (tambien de pasto) del esperado. Sin embargo, esto no afecta a la jugabilidad.
2. :warning: El movimiento se hizo con las teclas WASD. Existe un bug que sucede al presionar los botones de movimiento muy rapido, que provoca que el jugador atraviese paredes (rocas). Por esto, se recomienda no *spammear* las teclas de movimiento.
3. :warning: Las teclas de las funcionalidades extra funcionan solo si se presionan (mantienen presionados) los tres botones a la vez (no uno tras otro). Esto de acuerdo a las issues y el correo enviado.
4. El módulo [```parámetros_generales```](./parametros_generales.py) contiene más parámetros que los pedidos en el enunciado, como auxiliares para el código (principalmente rutas de los sprites).

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. [Drag'n'Drop](https://stackoverflow.com/questions/50232639/drag-and-drop-qlabels-with-pyqt5): mi código está un poco distinto, pero fuertemente basado en esta fuente. Implementa el *drag and drop* de las semillas. Está implementado en el archivo [```frontend.py```](./frontend.py) entre las líneas **23-52** y en el archivo [```mapa.py```](./mapa.py) entre las líneas **65-75**. Esto también se encuentra correctamente comentado en el código.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
