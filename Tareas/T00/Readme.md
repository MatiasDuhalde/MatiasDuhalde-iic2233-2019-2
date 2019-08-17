# Tarea 00: LegoSweeper :school_satchel:

## Consideraciones generales :octocat:

El programa entregado hace todo lo pedido en el enunciado, incluyendo el bonus. Para hacer uso del programa, antes de ejecutarlo hay que colocar los archivos entregados (i.e. ```parametros.py``` y ```tablero.py```) en el directorio base (los cuales no están incluidos en mi repositorio de acuerdo al enunciado). Una vez hecho esto, solo basta ejecutar el archivo principal, y el programa parte inmediatamente en el **menú de inicio**.

### Cosas implementadas y no implementadas :white_check_mark: :x:

La pauta se encuentra [aquí](https://docs.google.com/spreadsheets/d/1ndqu5lnVhCo_WYMhRzDI6HYAIJLxUfpfm4pL4uORgVg/).

* **Inicio del Programa**: Hecha completa.
    * Menú de Inicio: :heavy_check_mark:
    * Funcionalidades: :heavy_check_mark:
    * Puntajes: :heavy_check_mark:
* **Flujo del Juego**: Hecha completa.
    * Menú de Juego: :heavy_check_mark:
    * Tablero: :heavy_check_mark:
    * Legos: :heavy_check_mark:
    * Guardado de partida: :heavy_check_mark:
* **Término del Juego**: Hecha completa.
    * Fin del juego: :heavy_check_mark:
    * Puntajes: :heavy_check_mark:
* **General**: Hecha completa.
    * Menús: :heavy_check_mark:
    * Parámetros: :heavy_check_mark:
* **:sparkles:Bonus:sparkles:**: Hecha completa.
    * Descubrimiento de celdas: :heavy_check_mark:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  [```LegoSweeper.py```](LegoSweeper.py). El script creará automáticamente los siguientes directorios y archivos en el directorio base:
1. ```partidas/```
2. ```puntajes.txt```

Ámbos estarán vacíos en un principio, y se iran agregando datos según se use el programa. Los **savegames** se almacenarán dentro de ```partidas/``` según el formato pedido en el enunciado. Además, como se especificó anteriormente, los archivos entregados **deben** estar en el directorio base (junto con ```LegoSweeper.py```):
1. ```parametros.py```
2. ```tablero.py```

**Nota**: El código sólo creará ```partidas/``` y ```puntajes.txt``` si es que estos originalmente no existen en el directorio base.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```sample()```
2. ```os```: ```system(), listdir(), name``` 
3. ```math```: ```ceil()```
4. ```sys```: ```exit()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```gametext```: Contiene **constantes** que guardan texto y elementos gráficos para mostrar en el terminal (i.e. ASCII Art, opciones de los menús). Todas las constantes están en mayúsculas, siguiendo el estilo de ```parametros```.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. En el enunciado, se pide dar la opción de **salir de la partida con guardar** en el menú de juego, entre otras opciones. Si bien esta opción no aparece explícita, se muestra una vez el jugador elige la opción de **salir**. Esto para darle una estructura más clásica al menú, ya que me parecía poco natural mostrarla junto con las otras.
2. Se limitaron los caracteres y la longitud del nombre de usuario del jugador, para no tener problemas al hacer los *savefiles* según el formato del enunciado. En el enunciado no se entrega mayor información acerca de que se debe o no admitir como nombre de usuario.
3. Con respecto al punto anterior, dentro del juego se respetan las mayúsculas del nombre elegido, pero al hacer el **savefile**, el nombre del archivo queda en **minúsculas**. Esto debido a que *Windows* (no estoy seguro si es así para otros OS) no hace distinción entre las mayusculas o minúsculas para los nombres de los archivos (es decir, "username.txt" == "USERNAME.txt"). Sin embargo, debido a que se guarda un string con el nombre de usuario dentro del **savefile**, es posible recuperar las mayúsculas originales al cargar una partida.
4. El código no contempla la posibilidad de que el usuario modifique externamente los *savefiles* y el archivo ```puntajes.txt```. Es posible que al hacer esto se generen errores, si es que al modificar no se sigue el formato establecido por el código. Haber controlado esto en el código (por ejemplo, arrojar un warning cuando un **savefile** está corrupto) hubiera sido extremadamente engorroso sin el uso de *exception handling* (el cual estaba prohibido para esta tarea).

-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console : está implementado en el archivo [```LegoSweeper.py```](LegoSweeper.py) en la línea **145** y sirve para *limpiar* la pantalla del terminal, y de esa manera hacer las transiciones entre menús y dentro del mismo juego más claras.

Además, aunque no es código, saqué recursos de los siguientes lugares:
1. http://patorjk.com/software/taag/ : se usa en el archivo [```gametext.py```](gametext.py), entre las líneas **6** y **33**. Corresponde a texto ASCII Art, y se usa como elemento estético en los menús.
2. https://www.oocities.org/spunk1111/small.htm : se usa en el archivo [```gametext.py```](gametext.py), entre las líneas **35** y **41**. Corresponde a ASCII Art de un lego, y se usa como elemento estético en los menús.


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
