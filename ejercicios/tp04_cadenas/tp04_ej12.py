def generar_baraja_espanola() -> list[str]:
    """
    pre: No recibe parámetros.
    post: Devuelve una lista de cadenas de texto con las 48 cartas de la baraja española.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    baraja = [f"{numero} {palo}" for palo in palos for numero in range(1, 13)]
    
    return baraja


def main() -> None:
    mazo = generar_baraja_espanola()
    
    print("BARAJA ESPAÑOLA COMPLETA")
    print(mazo)
    print(f"\nTotal de cartas generadas: {len(mazo)}")


if __name__ == "__main__":
    main()