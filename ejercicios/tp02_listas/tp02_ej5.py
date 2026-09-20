def ordenada(lista:list) -> bool:
    """
    Verifica si una lista esta ordenada de menor a mayor.

    Pre: recibe una lista.
    Post: devuelve True si esta ordenada o False si no.
    """
    return lista == sorted(lista)

assert ordenada([1,2,3]) == True
assert ordenada(["b","a"]) == False
assert ordenada([10,2,30]) == False
assert ordenada([]) == True

print("Los assert funcionaron bien.")