# Tarea 00: LegoSweeper :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

El código entregado hace todo lo pedido en el enunciado y la pauta (incluyendo el **bonus**). De igual manera, se deben tener ciertas consideraciones:
* En el enunciado, se pide dar la opción de **salir de la partida con guardar** en el menú de juego, entre otras opciones. Si bien esta opción no aparece explícita, se muestra una vez el jugador elige la opción de **salir**. Esto para darle una estructura más clásica al menú, ya que me parecía poco natural mostrarla junto con las otras.
* Se limitaron los caracteres y la longitud del nombre de usuario del jugador, para no tener problemas al hacer los *savefiles*.
* El código no contempla la posibilidad de que el usuario modifique externamente los *savefiles* y el archivo ```puntajes.txt```. Es posible que al hacer esto se generen errores.

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
El módulo principal de la tarea a ejecutar es  ```LegoSweeper.py```. El script creará automáticamente los siguientes directorios y archivos:
1. ```partidas/```
2. ```puntajes.txt```

Ámbos estarán vacíos en un principio, y se iran agregando datos según se use el programa. Los **savegames** se almacenarán dentro de ```partidas/``` según el formato pedido en el enunciado. Además, los archivos entregados deben estar en el directorio base (junto con ```LegoSweeper.py```):
1. ```parametros.py```
2. ```tablero.py```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```sample()```
2. ```os```: ```system(), listdir(), name``` 
3. ```math```: ```ceil()```
4. ```sys```: ```exit()```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```gametext```: Contiene **constantes** que guardan texto y elementos gráficos para mostrar en el terminal (i.e. ASCII Art, opciones de los menús). Todas las constantes están en mayúsculas, siguiendo el estilo de ```parametros```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


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
1. https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console: está implementado en el archivo ```LegoSweeper.py``` en la línea **145** y sirve para *limpiar* la pantalla del terminal, y de esa manera hacer las transiciones entre menús y dentro del mismo juego más claras.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
