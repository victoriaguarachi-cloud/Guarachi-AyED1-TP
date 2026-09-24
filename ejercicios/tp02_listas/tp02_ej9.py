def generar_no_multiplos_de_cinco(a: int, b: int) -> list[int]:
    """
    Genera una lista por comprensión entre A y B (inclusive) con los números
    que NO son múltiplos de 5.

    pre: recibe dos enteros A y B.
    post: devuelve una lista de enteros en el rango [min(A,B), max(A,B)] que no son divisibles por 5.
    """
    inicio = min(a, b)
    fin = max(a, b)

    return [num for num in range(inicio, fin + 1) if num % 5 != 0]


def main() -> None:
    assert generar_no_multiplos_de_cinco(1, 10) == [1, 2, 3, 4, 6, 7, 8, 9]
    assert generar_no_multiplos_de_cinco(10, 1) == [1, 2, 3, 4, 6, 7, 8, 9]
    assert generar_no_multiplos_de_cinco(5, 5) == []

    print("Todas las pruebas del assert pasaron correctamente.")

    print("--filtrar numeros no multiplos de 5--")
    a = int(input("Ingrese el valor de A: "))
    b = int(input("Ingrese el valor de B: "))

    resultado = generar_no_multiplos_de_cinco(a, b)

    print(f"Lista generada entre {min(a, b)} y {max(a, b)} (sin múltiplos de 5):")
    print(resultado)


if __name__ == "__main__":
    main()