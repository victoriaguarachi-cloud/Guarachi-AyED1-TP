def maximo_unico(a: int, b: int, c: int) -> int:
    """
    Devuelve el valor máximo de tres enteros si es único.
    Si el máximo se repite, devuelve -1.

    pre: recibe tres números enteros a, b y c.
    post: devuelve el mayor entero si no hay empates en la primera posición, o -1 si el máximo está repetido.
    """
    numeros = [a, b, c]
    mayor = max(numeros)
    cantidad = numeros.count(mayor)

    if cantidad == 1:
        return mayor
    else:
        return -1


def main() -> None:
    primero = int(input("Ingrese el primer numero: "))
    segundo = int(input("Ingrese el segundo numero: "))
    tercero = int(input("Ingrese el tercer numero: "))

    resultado = maximo_unico(primero, segundo, tercero)

    if resultado == -1:
        print("No hay maximo unico")
    else:
        print(f"El valor maximo es: {resultado}")


if __name__ == "__main__":
    main()