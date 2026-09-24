def contar_digitos(numero: int) -> int:
    """
    Cuenta la cantidad de dígitos de un entero positivo.

    pre: recibe un número entero estrictamente mayor a 0.
    post: devuelve la cantidad de dígitos que integran el número.
    """
    c = 0
    while numero > 0:
        numero = numero // 10
        c += 1
    return c


def concatenar(a: int, b: int) -> int:
    """
    Concatena numéricamente dos enteros positivos sin convertirlos a cadena (string).

    pre: recibe dos números enteros mayores a 0.
    post: devuelve un nuevo número entero formado por los dígitos de 'a' seguidos por los de 'b'.
    """
    cantidad_dig = contar_digitos(b)
    potencia = 10 ** cantidad_dig
    resultado = a * potencia + b
    return resultado


def main() -> None:
    assert concatenar(1234, 567) == 1234567
    assert concatenar(5, 9) == 59
    assert concatenar(12, 5) == 125

    print("Todas las pruebas del assert pasaron correctamente.")


if __name__ == "__main__":
    main()