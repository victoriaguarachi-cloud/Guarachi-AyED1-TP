def sumar_cadenas_reales(cadena1: str, cadena2: str) -> float:
    """
    PRE: Recibe dos cadenas de caracteres que representan números reales.
    POST: Devuelve la suma de ambos valores como un número real (float).
          Devuelve -1 si alguna de las cadenas no contiene un número válido,
          utilizando manejo de excepciones.
    """
    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        return num1 + num2
    except ValueError:
        return -1.0


def main() -> None:
    cant = 80
    print("=" * cant)
    print("SUMA DE CADENAS REALES CON EXCEPCIONES (TP5 EJ 2)".center(cant))
    print("=" * cant)

    cadena1 = input("\nIngrese el primer número real: ")
    cadena2 = input("Ingrese el segundo número real: ")

    resultado = sumar_cadenas_reales(cadena1, cadena2)

    print("\n--- Resultado ---")
    if resultado != -1.0:
        print(f"La suma de {cadena1} + {cadena2} es: {resultado}")
    else:
        print("Error: Al menos una de las cadenas ingresadas no es un número real válido. (Devolvió -1)")

    print("=" * cant)


if __name__ == "__main__":
    main()