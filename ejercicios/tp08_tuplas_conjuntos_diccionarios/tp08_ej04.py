def encajan_fichas(ficha1: tuple[int, int], ficha2: tuple[int, int]) -> bool:
    """
    PRE: Recibe dos tuplas que representan fichas de dominó, ej: (3, 4) y (5, 4).
    POST: Devuelve True si las fichas comparten al menos un número, False en caso contrario.
          Utiliza el método nativo .intersection() de conjuntos para determinar coincidencias.
    """
    conjunto1 = set(ficha1)
    conjunto2 = set(ficha2)

    interseccion = conjunto1.intersection(conjunto2)
    return len(interseccion) > 0


def ingresar_ficha(numero_ficha: int) -> tuple[int, int]:
    """
    PRE: Recibe el número identificador de la ficha a cargar.
    POST: Solicita y devuelve una tupla (n1, n2) con valores válidos de dominó (0 a 6).
    """
    while True:
        try:
            print(f"\n--- Ingrese los valores de la Ficha {numero_ficha} ---")
            lado_a = int(input("Primer valor (0-6): "))
            lado_b = int(input("Segundo valor (0-6): "))

            if not (0 <= lado_a <= 6 and 0 <= lado_b <= 6):
                raise ValueError("Los valores del dominó deben estar entre 0 y 6.")

            return (lado_a, lado_b)
        except ValueError as e:
            print(f"Error de ingreso: {e}. Intente nuevamente.")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("ENCASTRE DE FICHAS DE DOMINÓ CON CONJUNTOS (TP8 EJ 4)".center(cant))
    print("=" * cant)

    f1 = ingresar_ficha(1)
    f2 = ingresar_ficha(2)

    resultado = encajan_fichas(f1, f2)

    print("\n--- Resultado ---")
    print(f"Ficha 1: {f1} | Ficha 2: {f2}")
    if resultado:
        print("Las fichas SÍ encajan (comparten al menos un valor).")
    else:
        print("Las fichas NO encajan (no tienen números en común).")

    print("=" * cant)


if __name__ == "__main__":
    main()