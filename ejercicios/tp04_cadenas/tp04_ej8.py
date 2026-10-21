def ultimos_n_caracteres(cadena: str, n: int) -> str:
    """
    pre: Recibe una cadena de caracteres y un entero N
    post: Devuelve una subcadena formada por los últimos N caracteres
    """
    if n <= 0:
        return ""
    
    return cadena[-n:]

def main() -> None:
    texto = "Programacion en Python"
    
    print(f"Cadena original: '{texto}' (Largo: {len(texto)})")
    print("-" * 45)
    
    casos = [6, 12, 1, 0, 50]
    
    for cantidad in casos:
        resultado = ultimos_n_caracteres(texto, cantidad)
        print(f"Ultimos {cantidad:2d} caracteres -> '{resultado}'")


if __name__ == "__main__":
    main()