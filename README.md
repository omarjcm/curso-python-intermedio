# Curso Intermedio de Python

## Curiosidades

- Con el siguiente comando se obtiene informacion acerca del Zen de Python.

> import this

    Bello es mejor que feo.
    Explicito es mejor que implícito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.
    Plano es mejor que anidado.
    Espaciado es mejor que denso.
    La legibilidad es importante.

## Creación de un entorno virtual

En Windows:

> mkdir vcs
> cd vcs

Se crea el entorno virtual.

> python -m venv venv

Luego, se activa el entorno virtual.

> .\venv\Scripts\activate

Para crear un alias a la linea de comando anterior se realiza lo siguiente:

> doskey avenv=.\venv\Scripts\activate

Por ende, para activar el entorno virtual tan solo se escribe:

> avenv

Para desactivar el entorno virtual, se escribe la siguiente linea de comando:

> deactivate

## Instalacion de dependencias con PIP

El siguiente comando es para revisar que comandos se encuentran instalados.

> pip freeze

> pip install pandas

Para tener un documento que se desee compartir con otra persona que se encuentre implementando lo mismo, se puede crear un archivo donde se almacenaran todos los paquetes que se esten utilizando en un proyecto en particular.

> pip freeze > requirements.txt

> pip install -r requirements.txt

## Funciones anonimas

lambda argumentos : expresion

palindromo = lambda cadena : cadena == cadena[::-1]

def palindromo(cadena):
    return cadena == cadena[::-1]

## High order functions: filter, map y reduce

Es una funcion que recibe como parametros otra funcion.

> def saludo(fn):
>   fn()
>
> def hola():
>   print('Hola!')
>
> def adios():
>   print('Adios!')
>
> saludo(hola)
> saludo(adios)






