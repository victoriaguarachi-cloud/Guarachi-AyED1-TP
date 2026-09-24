def normalizar(lista: list[int | float]) -> list[float]:
    """
    Devuelve una nueva lista con sus elementos normalizados de modo que
    la suma total sea igual a 1.0, manteniendo las proporciones relativas.

    pre: recibe una lista de números enteros o flotantes, con suma total distinta de cero.
    post: devuelve una nueva lista de números flotantes que suman 1.0.
    """
    total = sum(lista)
    if total == 0:
        return []
    return [x / total for x in lista]


def main() -> None:
    lista_ejemplo = [1, 1, 2]
    lista_normalizada = normalizar(lista_ejemplo)

    print("Lista original:", lista_ejemplo)
    print("Lista normalizada:", lista_normalizada)
    print("Suma de la lista normalizada:", sum(lista_normalizada))


if __name__ == "__main__":
    main()