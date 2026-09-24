def generar_impares() -> list[int]:
    """
    Genera una lista con todos los números impares entre 100 y 200 inclusive
    utilizando comprensión de listas.

    pre: ninguna.
    post: devuelve una lista de enteros impares dentro del rango [100, 200].
    """
    return [num for num in range(101, 201, 2)]


def main() -> None:
    impares = generar_impares()
    assert len(impares) == 50
    assert impares[0] == 101
    assert impares[-1] == 199
    assert all(num % 2 != 0 for num in impares)

    print("Todas las pruebas del assert pasaron correctamente.\n")

    print(f"Lista de impares entre 100 y 200 (Total: {len(impares)}):")
    print(impares)


if __name__ == "__main__":
    main()