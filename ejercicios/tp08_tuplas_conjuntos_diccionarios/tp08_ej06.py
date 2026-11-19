def obtener_palabras_unicas_por_longitud(frase: str) -> list[str]:
    """
    PRE: Recibe una cadena de texto (frase).
    POST: Devuelve una lista con las palabras únicas en minúsculas,
          ordenadas de menor a mayor según su longitud.
    """
    if not frase.strip():
        return []

    palabras = [palabra.strip(".,;:¡!¿?()\"'") for palabra in frase.lower().split()]
    palabras_limpias = [p for p in palabras if p]

    palabras_unicas = set(palabras_limpias)

    return sorted(palabras_unicas, key=len)


def main() -> None:
    cant = 80
    print("=" * cant)
    print("PALABRAS ÚNICAS ORDENADAS POR LONGITUD (TP8 EJ 6)".center(cant))
    print("=" * cant)

    frase = input("\nIngrese una frase o texto: ").strip()

    resultado = obtener_palabras_unicas_por_longitud(frase)

    print("\n--- Resultado ---")
    if resultado:
        print(f"Total de palabras únicas encontradas: {len(resultado)}")
        print("\nPalabras ordenadas por longitud:")
        for palabra in resultado:
            print(f"  • {palabra:<15} ({len(palabra)} letras)")
    else:
        print("No se ingresaron palabras válidas.")

    print("=" * cant)


if __name__ == "__main__":
    main()