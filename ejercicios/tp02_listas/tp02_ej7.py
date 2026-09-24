def intercalar_elementos(lista1: list[int], lista2: list[int]) -> None:
    """
    Intercala los elementos de la segunda lista dentro de la primera usando rebanadas.
    Modifica la primera lista in-place.

    pre: recibe dos listas de enteros positivos.
    post: la primera lista queda modificada con los elementos intercalados.
    """
    for i, e in enumerate(lista2):
        pos = i * 2 + 1
        if pos < len(lista1):
            lista1[pos:pos] = [e]
        else:
            lista1.append(e)


def main() -> None:
    lista1 = [8, 1, 3]
    lista2 = [5, 9, 7]

    print("Lista 1 original:", lista1)
    print("Lista 2 original:", lista2)

    intercalar_elementos(lista1, lista2)

    print("Lista 1 intercalada:", lista1)


if __name__ == "__main__":
    main()