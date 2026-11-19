import random

def jugar_adivinanza() -> None:
    """
    PRE: No recibe parámetros.
    POST: Genera un número al azar entre 1 y 500. Solicita ingresos al usuario
          hasta adivinarlo, indicando si es mayor o menor. Cuenta la cantidad
          de intentos e incluye los ingresos inválidos como intentos consumidos.
    """
    numero_secreto = random.randint(1, 500)
    intentos = 0
    adividado = False
    
    print("\n¡Pense un número entero entre 1 y 500! Intenta adivinarlo.\n")
    
    while not adividado:
        intentos += 1
        try:
            entrada = input(f"[Intento {intentos}] Ingrese su número: ")
            intento_usuario = int(entrada)
            
            if intento_usuario == numero_secreto:
                adividado = True
                print(f"\n¡Felicidades! Adivinaste el número {numero_secreto}.")
                print(f"Te tomó un total de {intentos} intento(s).")
            elif intento_usuario < numero_secreto:
                print("El número a adivinar es MAYOR.")
            else:
                print("El número a adivinar es MENOR.")

        except ValueError:
            print("Error: Ingresaste algo que no es un número entero válido. (Este intento también suma).")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("JUEGO: ADIVINA EL NÚMERO (TP5 EJ 7)".center(cant))
    print("=" * cant)

    jugar_adivinanza()

    print("=" * cant)


if __name__ == "__main__":
    main()