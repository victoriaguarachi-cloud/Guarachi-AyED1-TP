def tabla_multiplicar(n: int) -> dict[int, int]:
    """
    PRE: Recibe un número entero N.
    POST: Devuelve un diccionario generado por comprensión con la tabla 
          de multiplicar de N del 1 al 12.
    """
    return {factor: n * factor for factor in range(1, 13)}


def main() -> None:
    cant = 80
    print("=" * cant)
    print("TABLA DE MULTIPLICAR CON DICCIONARIO POR COMPRENSIÓN (TP8 EJ 9)".center(cant))
    print("=" * cant)

    try:
        n = int(input("\nIngrese un número entero para calcular su tabla: "))
        tabla = tabla_multiplicar(n)

        print(f"\n--- Tabla del {n} ---")
        for factor, resultado in tabla.items():
            print(f"{n} x {factor:2d} = {resultado}")

    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

    print("=" * cant)


if __name__ == "__main__":
    main()