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
    doctest.testmod(verbose = True)