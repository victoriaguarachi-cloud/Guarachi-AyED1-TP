def ordenada(lista: list) -> bool:
    """
    Verifica si los elementos de una lista están ordenados de forma ascendente.

    pre: recibe una lista de elementos comparables entre sí (números, cadenas, etc.).
    post: devuelve True si la lista está ordenada ascendentemente, False en caso contrario.
    """
    es_ascendente = True
    i = 0

    while i < len(lista) - 1 and es_ascendente:
        if lista[i] > lista[i + 1]:
            es_ascendente = False
        i += 1

    return es_ascendente


def main() -> None:
    assert ordenada([1, 2, 3]) == True
    assert ordenada(['b', 'a']) == False
    assert ordenada([1, 1, 2, 5]) == True
    assert ordenada([10, 5, 20]) == False
    assert ordenada([]) == True
    assert ordenada([5]) == True

    print("Todas las pruebas del assert pasaron correctamente.\n")

    ejemplo_numeros = [2, 4, 8, 15, 20]
    ejemplo_desordenado = [5, 1, 9, 3]
    ejemplo_letras = ['a', 'b', 'c', 'd']

    print(f"La lista {ejemplo_numeros} ¿está ordenada?: {ordenada(ejemplo_numeros)}")
    print(f"La lista {ejemplo_desordenado} ¿está ordenada?: {ordenada(ejemplo_desordenado)}")
    print(f"La lista {ejemplo_letras} ¿está ordenada?: {ordenada(ejemplo_letras)}")


if __name__ == "__main__":
    main()