# Tarea 01: Initial P :school_satchel:

## Consideraciones generales :octocat:

El programa entregado hace todo lo pedido en el enunciado, menos el segundo bonus (Power-Ups). Para hacer uso del programa, antes de ejecutarlo hay que asegurarse que se encuentren los archivos estáticos entregados que, de acuerdo al enunciado, no vienen en el repositorio (i.e. ```pistas.csv``` y ```contrincantes.csv```) en el directorio ```./databases/static``` (esta carpeta debe ser creada, se me pasó añadir un ```.keep```). Una vez hecho esto, solo basta ejecutar el archivo principal, y el programa parte inmediatamente en el **menú de sesión**.


### Cosas implementadas y no implementadas :white_check_mark: :x:

La pauta se encuentra [aquí](https://docs.google.com/spreadsheets/u/1/d/1SgNPF-wmvrBQ6HNAKa9fM_VBH0cTcX1gHbcQ3K74P3M/edit?usp=sharing).

* **Programación Orientada a Objetos**: Hecha completa.
    * Diagrama: :heavy_check_mark:
    * Definición de clases: :heavy_check_mark:
        * :ledger: [```entidades.py```](lib/entidades.py) | Vehículos: Líneas **9-130**
        * :ledger: [```entidades.py```](lib/entidades.py) | Pistas: Líneas **133-189**
        * :ledger: [```entidades.py```](lib/entidades.py) | Pilotos: Líneas **191-284**
    * Relaciones entre clases: :heavy_check_mark:
        * :ledger: [```entidades.py```](lib/entidades.py) | Clases abstractas: Líneas **9-62**, **133-156**, y también el archivo [``mainmenu.py``](lib/mainmenu.py)
        * :ledger: [```menu.py```](lib/menu.py) | Agregación: Múltiples líneas (ver atributos de las clases).
        * :ledger: [```menu.py```](lib/menu.py), [```mainmenu.py```](lib/menumenu.py), [```entidades.py```](lib/entidades.py) | Herencia y multi-herencia: Múltiples líneas (ver definición de clase y uso de ``super``).
* **Cargar y guardar partidas**: Hecha completa.
    * Cargar: :heavy_check_mark:
        * :ledger: [```funciones.py```](lib/funciones.py) | Lectura de archivos .csv: Líneas **18-64**, **99-108**. También en [```menu.py```](lib/menu.py) (líneas **20-38**)
    * Guardar: :heavy_check_mark:
* **Initial P**: Hecha completa.
    * Crear Partida: :heavy_check_mark:
    * Pits: :heavy_check_mark:
    * Carrera: :heavy_check_mark:
        * :ledger: [```funciones.py```](lib/funciones.py) | Cálculo velocidad: Líneas **195-213**
        * :ledger: [```funciones.py```](lib/funciones.py) | Cálculo hipotermia: Líneas **181-185**
        * :ledger: [```funciones.py```](lib/funciones.py) | Cálculo daño: Líneas **217-220**
        * :ledger: [```funciones.py```](lib/funciones.py) | Cálculo probabilidad de accidente: Líneas **229-234** :warning:
    * Fin Carrera: :heavy_check_mark:
        * :ledger: [```funciones.py```](lib/funciones.py) | Cálculo experiencia y dinero: Líneas **226-227**, **242-245**, **253-258**
* **Consola**: Hecha completa.
    * Menú sesión: :heavy_check_mark:
    * Menú principal: :heavy_check_mark: :warning:
    * Menú compra vehículos: :heavy_check_mark:
    * Menú preparación carrera: :heavy_check_mark:
    * Menú carrera: :heavy_check_mark:
    * Menú Pits: :heavy_check_mark:
    * Menú Robustez: :heavy_check_mark:
* **Archivos**: Hecha completa
    * Archivos CSV: :heavy_check_mark:
        * :ledger: [```funciones.py```](lib/funciones.py) | Manejo CSV: Líneas **18-172**
    * [```parametros.py```](lib/parametros.py): :heavy_check_mark:
        * :ledger: [```parametros.py```](lib/parametros.py) | Uso del módulo: Múltiples líneas de los archivos [```carrera.py```](lib/carrera.py), [```entidades.py```](lib/entidades.py), [```funciones.py```](lib/funciones.py), [```menu.py```](lib/carrera.py). 
* **:sparkles:Bonus:sparkles:**: Hecha a medias (5/8).
    * Buenas prácticas: :heavy_check_mark:
        * :ledger: [```funciones.py```](lib/funciones.py), [```menu.py```](lib/menu.py), [```mainmenu.py```](lib/mainmenu.py) | Clase Menu y módulo funciones: Las **fórmulas** se usan en [```carrera.py```](lib/carrera.py) :warning:
    * *Power ups*: :x:

**Nota**: aquellas líneas marcadas con :warning:, tienen detalles extra en [supuestos y consideraciones adicionales](#Supuestos-y-consideraciones-adicionales-:thinking:).


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  [```main.py```](main.py).


## Librerías :books:
### Librerías externas utilizadas

La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```sample()```
2. ```os```: ```system(), listdir(), name``` 
3. ```math```: ```ceil()```
4. ```sys```: ```exit()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes (todos se encuentran dentro de [lib](./lib)):

1. [```mainmenu```](lib/mainmenu.py)-> Contiene la clase abstracta ```Menu```.
2. [```menu```](lib/menu.py)-> Contiene las subclases de la clase ```Menu``` (```MenuSesion```, ```MenuInicio```, etc.), según lo pedido en la parte 1 del bonus.
3. [```funciones```](lib/funciones.py)-> Contiene las fórmulas usadas en el programa en forma de funciones, según lo pedido en la parte 1 del bonus. Además, contiene funciones auxiliares.
4. [```gametext```](lib/gametext.py)-> Contiene constantes (```strings```) que describen los elementos gráficos de la interfaz.
5. [```carrera```](lib/carrera.py)-> Contiene el flujo de la carrera y los pits.
6. [```entidades```](lib/entidades.py)-> Contiene las entidades/clases que usa el programa (```Vehiculo```, ```Pista```, ```Piloto```, ```Contrincante```).
7. [```parametros```](lib/parametros.py)-> Contiene los parámetros/constantes que se usan en el programa según el enunciado.
4. [```__init__```](lib/__init__.py)-> Está vacío, permite usar la carpeta [lib](./lib) como un package.


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>

...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. patorjk.com/software/taag/: No es código, pero con esta página se generó el ASCII art que se usa en el módulo [```gametext```](lib/gametext.py).



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).