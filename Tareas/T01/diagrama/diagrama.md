# Diagrama de Clases

![diagrama](./diagrama.png)

## Consideraciones:
Por simplicidad, se tomaron las siguientes libertades
 - Las flecha de agregación que viene de `Piloto` a `Vehiculo` debería estar unida a sus subclases.
 - Esto también aplica para **(2)** la flecha de agregación de `Menu` a `Piloto`, **(3)** las flechas de agregación las 3 subclases de `Menu`(`MenuPreparacionCarrera`, `MenuSelectVehiculo` y `MenuCarrera`) a `Pista`, **(4)** las flechas de agregación las 2 subclases de `Menu` (`MenuPits` y `MenuCarrera`) a `Vehculo`, y **(5)** la flecha de composición de `Contrincantes` a `Vehiculo`. 
 - Las cardinalidades no se notan mucho y pueden estar incorrectas, pero esto se permitía en el enunciado.
 - Está implicitamente expresado que los atributos que comienzan con doble guiónbajo **(`__`)** son privados de la clase. 

No se indica explicitamente, pero Menu, Vehiculo y Pista corresponden a clases abstractas (Heredan de ABC, esto no se muestra en el diagrama).

Junto con lo anterior, los métodos que se repiten en la clase Madre y sus subclases (véase **`__str__`** y **`go_to()`** de Menu) corresponden a métodos abstractos, y se declaran en ambas clases debido a que es obligatorio realizar un *override* (véase la issue [#299](https://github.com/IIC2233/syllabus/issues/299)).
 