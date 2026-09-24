def generar_cuadrados(n: int) -> list[int]:
    """
    Genera una lista con los cuadrados de los números enteros entre 1 y N inclusive.

    pre: recibe N como un entero mayor o igual a 1.
    post: devuelve una lista con los N números al cuadrado.
    """
    cuadrados = [i**2 for i in range(1, n + 1)]
    return cuadrados


def obtener_ultimos_diez(lista: list[int]) -> list[int]:
    """
    Obtiene los últimos 10 elementos de una lista dada mediante rebanadas.

    pre: recibe una lista de enteros.
    post: devuelve una nueva lista con los últimos 10 elementos (o todos si la lista tiene menos de 10).
    """
    return lista[-10:]


def main() -> None:
    assert generar_cuadrados(5) == [1, 4, 9, 16, 25]
    assert obtener_ultimos_diez([1, 4, 9, 16, 25]) == [1, 4, 9, 16, 25]
    assert obtener_ultimos_diez(list(range(1, 16))) == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    print("Todas las pruebas del assert pasaron correctamente.\n")

    n = int(input("Ingrese un valor entero N (>= 1): "))

    if n < 1:
        print("El número ingresado debe ser mayor o igual a 1.")
    else:
        lista_cuadrados = generar_cuadrados(n)
        ultimos_diez = obtener_ultimos_diez(lista_cuadrados)

        print(f"\nLista completa generada (largo {len(lista_cuadrados)}): {lista_cuadrados}")
        print(f"Los últimos 10 valores son: {ultimos_diez}")


if __name__ == "__main__":
    main()