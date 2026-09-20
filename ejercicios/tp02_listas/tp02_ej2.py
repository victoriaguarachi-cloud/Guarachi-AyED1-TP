import random as rn

def generar_lista(n: int) -> list:
    """
    Genera una lista de N numeros aleatorios entre 1 y 100.
    pre: recibe N(un entero positivo mayor a 0).
    post: devuelve una lista con N numeros enteros al azar.

    """
    return [rn.randint(1,100) for _ in range(n)]

def tiene_repetidos(lista:list) -> bool:
    """
    Verifica si una lista contiene elementos duplicados.

    pre: recibe una lista.
    post: devuelve True si hay elementos repetidos o False si no.
    """
    return len(lista) != len(set(lista))

def obtener_unicos(lista:list) -> list:
    """
    Genera una nueva lista solo con los elementos unicos de la original.

    pre: recibe una lista.
    post: devuelve una nueva lista sin elementos duplicados.
    """
    return list(set(lista))

assert tiene_repetidos([1,2,3,1]) == True
assert tiene_repetidos([1,2,3,4]) == False

assert sorted(obtener_unicos([1,2,2,3])) == [1,2,3]

assert len(generar_lista(5)) == 5

print("los assert funcionaron.")