def centrar_cadena(cadena: str, ancho: int = 80) -> str:
    """
    pre: recibe una cadena de texto y un ancho total de pantalla (por defecto 80).
    post: devuelve la cadena centrada con espacios a los lados.
    """
    return cadena.center(ancho)


def main() -> None:
    texto = input("Ingresa una cadena de texto: ")
    texto_centrado = centrar_cadena(texto)
    
    print("-" * 80)  
    print(texto_centrado)
    print("-" * 80)


if __name__ == "__main__":
    main()