# Segunda tarea de APA 2026: Manejo de números primos

> [!Caution]
>
> El objetivo de esta tarea es manejar los tipos de datos y las estructuras de control de flujo de
> Python. Existen bibliotecas que resuelven los apartados del enunciado de una manera más eficiente
> y, sin duda, más sencilla, pero su uso está prohibido.
>
> Además, se valorará también el uso de Markdown en la redacción del fichero README.md; en concreto,
> la inclusión de código fuente con las herramientas propias de Markdown para su realce sintáctico, y
> la inclusión de imágenes con las capturas de pantalla solicitadas. El fichero README.md deberá ser
> visualizado correctamente desde la página principal del repositorio GitHub del alumno sin ninguna
> intervención por parte del profesor.
>
> Dispone del fichero MARKDOWN.md con información básica para el uso de Markdown, así como con enlaces
> a la documentación oficial del mismo.
>
> ¿Quiere saber más?, consulte con el profesorado.
  
## Nombre y Apellidos

> [!Important]
> Introduzca a continuación su nombre y apellidos:
>
> Eloi Belmonte Alcalá

## Fichero `primos.py`

- El alumno debe escribir el fichero `primos.py` que incorporará distintas funciones relacionadas con el manejo
  de los números primos.

- El fichero debe incluir una cadena de documentación que incluirá el nombre del alumno y los tests unitarios
  de las funciones incluidas.

- Cada función deberá incluir su propia cadena de documentación que indicará el cometido de la función, los
  argumentos de la misma y la salida proporcionada.

- Se valorará lo pythónico de la solución; en concreto, su claridad y sencillez, y el uso de los estándares marcados
  por PEP-8. También se valorará su eficiencia computacional.

### Determinación de la *primalidad* y descomposición de un número en factores primos

Incluya en el fichero `primos.py` las tres funciones siguientes:

- `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
  - Se debe considerar que `numero` es un número natural y mayor que uno.
  - En caso contrario, la función debe elevar la excepción `TypeError` y finalizar la ejecución.
- `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
- `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.

### Obtención del mínimo común múltiplo y el máximo común divisor

Usando las tres funciones del apartado anterior (y cualquier otra que considere conveniente añadir), escriba otras
dos que calculen el máximo común divisor y el mínimo común múltiplo de sus argumentos:

- `mcm(numero1, numero2)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(numero1, numero2)`:  Devuelve el máximo común divisor de sus argumentos.

Estas dos funciones deben cumplir las condiciones siguientes:

- Aunque se trate de una solución sub-óptima, en ambos casos deberá partirse de la descomposición en factores
  primos de los argumentos usando las funciones del apartado anterior.

- Aunque también sea sub-óptimo desde el punto de vista de la programación, ninguna de las dos funciones puede
  depender de la otra; cada una debe programarse por separado.

### Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos

Modifique las funciones `mcm()` y `mcd()`, para que calculen el mínimo común múltiplo y el máximo común divisor
para un número arbitrario de argumentos:

- `mcm(*numeros)`:  Devuelve el mínimo común múltiplo de sus argumentos.
- `mcd(*numeros)`:  Devuelve el máximo común divisor de sus argumentos.

### Tests unitarios

La cadena de documentación del fichero debe incluir los tests unitarios de las cinco funciones. En concreto, deberán
comprobarse las siguientes condiciones:

- `esPrimo(numero)`:  Al ejecutar `[ numero for numero in range(2, 50) if esPrimo(numero) ]`, la salida debe ser
                      `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]`.
- `primos(numeor)`: Al ejecutar `primos(50)`, la salida debe ser `(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)`.
- `descompon(numero)`: Al ejecutar `descompon(36 * 175 * 143)`, la salida debe ser `(2, 2, 3, 3, 5, 5, 7, 11, 13)`.
- `mcm(num1, num2)`: Al ejecutar `mcm(90, 14)`, la salida debe ser `630`.
- `mcd(num1, num2)`: Al ejecutar `mcd(924, 780)`, la salida debe ser `12`.
- `mcm(numeros)`: Al ejecutar `mcm(42, 60, 70, 63)`, la salida debe ser `1260`.
- `mcd(numeros)`: Al ejecutar `mcd(840, 630, 1050, 1470)`, la salida debe ser `210`.

### Entrega

#### Ejecución de los tests unitarios

![Ejecución de los tests unitarios](verbose.png)

#### Código desarrollado

```python
"""
primos.py
==========

Autor: Eloi Belmonte

Funciones para trabajar con números primos, descomposición factorial,
mínimo común múltiplo (mcm) y máximo común divisor (mcd).

Tests unitarios (doctest)
-------------------------

>>> [numero for numero in range(2, 50) if esPrimo(numero)]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcm(42, 60, 70, 63)
1260

>>> mcd(840, 630, 1050, 1470)
210
"""


from math import isqrt
from collections import Counter


# ----------------------------------------------------------------------
# PRIMALIDAD
# ----------------------------------------------------------------------

def esPrimo(numero):
    """
    Determina si un número natural mayor que uno es primo.

    Args:
        numero (int): número natural mayor que 1.

    Returns:
        bool: True si es primo, False en caso contrario.

    Raises:
        TypeError: si el argumento no es un natural > 1.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1.")
    

    if numero == 2:
        return True

    if numero % 2 == 0:
        return False

    limite = isqrt(numero)
    for i in range(3, limite + 1, 2):
        if numero % i == 0:
            return False

    return True


# ----------------------------------------------------------------------
# LISTA DE PRIMOS
# ----------------------------------------------------------------------

def primos(numero):
    """
    Devuelve todos los números primos menores que numero.

    Args:
        numero (int): límite superior.

    Returns:
        tuple: tupla de números primos menores que numero.
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))


# ----------------------------------------------------------------------
# DESCOMPOSICIÓN EN FACTORES PRIMOS
# ----------------------------------------------------------------------

def descompon(numero):
    """
    Devuelve la descomposición en factores primos de un número.

    Args:
        numero (int): número natural mayor que 1.

    Returns:
        tuple: factores primos ordenados.
    """
    if not isinstance(numero, int) or numero <= 1:
        raise TypeError("El argumento debe ser un número natural mayor que 1.")

    factores = []
    divisor = 2

    while divisor * divisor <= numero:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1

    if numero > 1:
        factores.append(numero)

    return tuple(factores)


# ----------------------------------------------------------------------
# MÍNIMO COMÚN MÚLTIPLO
# ----------------------------------------------------------------------

def mcm(*numeros):
    """
    Calcula el mínimo común múltiplo de uno o más números.

    Se basa en la descomposición en factores primos.

    Args:
        *numeros (int): uno o más números naturales.

    Returns:
        int: mínimo común múltiplo.
    """
    if not numeros:
        raise TypeError("Debe proporcionarse al menos un número.")

    maximos = Counter()

    # Apuntes 
    # Counter es un tipo especial de diccionario
    # Counter ({clave:valor, clave:valor, clave:valor...}) 
    # dic.keys(), claves
    # dic.values(), valores
    # dic.items(), iterable de tuplas (pares clave-valor):  ([(clave,valor), (clave,valor), (clave,valor), (clave,valor)... ])
    #                                                        0^             1^             2^             3^   
    
    for n in numeros:
        factores = Counter(descompon(n))
        for primo, exp in factores.items(): 
            
            # La coma --> desempaquetado de tuplas en (primo, exp)
            # factores.items() devuelve pares (primo, exponente)
            # Pasamos de la tupla larga a parejas de clave/valor
            
            maximos[primo] = max(maximos[primo], exp) 
            
            # Coge el max exponente del mismo primo para las dos descomposiciones

    resultado = 1
    for primo, exp in maximos.items():
        resultado *= primo ** exp

    return resultado


# ----------------------------------------------------------------------
# MÁXIMO COMÚN DIVISOR
# ----------------------------------------------------------------------

def mcd(*numeros):
    """
    Calcula el máximo común divisor de uno o más números.

    Se basa en la descomposición en factores primos.

    Args:
        *numeros (int): uno o más números naturales.

    Returns:
        int: máximo común divisor.
    """
    if not numeros:
        raise TypeError("Debe proporcionarse al menos un número.")

    contadores = [Counter(descompon(n)) for n in numeros]

    # Counter(descompon(n))
        # n: Cada número recibido
        # numeros: Los argumentos
        # descompon(n): Factores primos de n
        # Counter(...): Cuenta cuántas veces aparece cada primo. En mi caso por Navidad y los cumpleaños de mis abuelos.
    # "contadores = [Counter(descompon(n)) for n in numeros]"  Crea una lista "contadores" y añade (append) a la lista cada Counter.

    comunes = contadores[0].copy() # En el 1º contador respecto a él mismo, todos los primos son comunes.

    for contador in contadores[1:]:
        for primo in list(comunes):
            comunes[primo] = min(comunes[primo], contador.get(primo, 0))

    # [primo] devuelve el valor del exponente del primo en cuestión
    # comunes[primo]: Dame el exponente actual de "primo"
    # contador.get(primo, 0): Dame el exp del primo si existe, sinó 0.
    # Finalmente nos quedamos con el mínimo y lo insertamos en comunes[primo] 
            
            if comunes[primo] == 0:
                del comunes[primo]

    resultado = 1
    for primo, exp in comunes.items():
        resultado *= primo ** exp

    return resultado


# Permite ejecutar los doctests directamente
if __name__ == "__main__":
    import doctest
    doctest.testmod()

```

#### Subida del resultado al repositorio GitHub ¿y *pull-request*?

El fichero `primos.py`, la imagen con la ejecución de los tests unitarios y este mismo fichero, `README.md`, deberán
subirse al repositorio GitHub mediante la orden `git push`. Si los profesores de la asignatura consiguen montar el
sistema a tiempo, la entrega se formalizará realizando un *pull-request* al propietario del repositorio original.

El fichero `README.md` deberá respetar las reglas de los ficheros Markdown y visualizarse correctamente en el repositorio,
incluyendo la imagen con la ejecución de los tests unitarios y el realce sintáctico del código fuente insertado.
