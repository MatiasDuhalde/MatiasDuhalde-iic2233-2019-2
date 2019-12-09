# Tarea 03: DCClub :school_satchel:

## Consideraciones generales :octocat:

Si bien no se pudo hacer todo lo pedido en el enunciado y la pauta, el programa es ejecutable y se puede acceder a todas las ventanas y funcionalidades base. Para hacer uso del programa, antes de ejecutarlo hay que asegurarse que se encuentren los archivos entregados que, de acuerdo al enunciado, no vienen en el repositorio. Estos son ```amigos.json``` y ```usuarios.json``` los cuales deben ir en el directorio ```./server/```, y todos los elementos gráficos de la interfaz, esto es, la carpeta `sprites` y todos sus contenidos, los cuales deben ser ubicados en el directorio base. La forma de partir el programa se explica en el apartado de [ejecución](https://github.com/IIC2233/MatiasDuhalde-iic2233-2019-2/tree/master/Tareas/T03#ejecuci%C3%B3n-computer)

### Cosas implementadas y no implementadas :white_check_mark: :x:

* <Nombre item pauta<sub>1</sub>>: Hecha completa
* <Nombre item pauta<sub>2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * <Nombre subitem pauta<sub>2.1</sub>>: Hecha completa 
    * <Nombre subitem pauta<sub>2.2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * ...
* <Nombre item pauta<sub>3</sub>>: Me faltó hacer <insertar qué cosa faltó>
* ...
* <Nombre item pauta<sub>n</sub>>: Me faltó hacer <insertar qué cosa faltó>

## Ejecución :computer:

Como el foco de esta tarea era *Networking*, el programa se divide en dos partes una del servidor (en `./server/`) y otra del cliente (en `./client/`). El archivo principal a ejecutar en ámbas partes es `main.py`. Para que funcione el programa, ámbos archivos deben ser ejecutados desde sus respectivos directorios, **no desde el directorio base**. Se debe primero iniciar el server, dado que si se inicia primero el cliente y no se puede detectar el servidor, el programa terminará, informando al usuario.


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```función() / módulo```
2. ```librería_2```: ```función() / módulo``` (debe instalarse)
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```librería_1```: Contiene a ```ClaseA```, ```ClaseB```, (ser general, tampoco es necesario especificar cada una)...
2. ```librería_2```: Hecha para <insertar descripción **breve** de lo que hace o qué contiene>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>

En el pié de página de la página 7 del enunciado se comenta que el botón (X) también puede ser valido para volver a la ventana de inicio. Personalmente decidí añadir un botón aparte para volver a la ventana de inicio. El botón (X) sigue con su comportamiento normal, es decir, cerrar la aplicación client-side.

-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
