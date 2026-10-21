
def extraer_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: Recibe una cadena, una posición de inicio (índice 0) y la cantidad de caracteres
    post: Devuelve la subcadena extraída usando rebanadas
    """
    fin = posicion + cantidad
    return cadena[posicion:fin]


def extraer_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: Recibe una cadena, una posición de inicio (índice 0) y la cantidad de caracteres
    post: Devuelve la subcadena extraída concatenando caracter por caracter
    """
    subcadena = ""
    limite = posicion + cantidad
    
    # Validamos no exceder el largo total de la cadena
    if limite > len(cadena):
        limite = len(cadena)
        
    for i in range(posicion, limite):
        subcadena += cadena[i]
        
    return subcadena


def main() -> None:
    texto = "El numero de telefono es 4356-7890"
    pos = 25
    cant = 9
    
    print(f"Cadena original: '{texto}'")
    print(f"Extraer desde la posicion {pos}, {cant} caracteres:\n")
    
    res_a = extraer_subcadena_rebanadas(texto, pos, cant)
    res_b = extraer_subcadena_sin_rebanadas(texto, pos, cant)
    
    print(f"a. Con rebanadas: '{res_a}'")
    print(f"b. Sin rebanadas: '{res_b}'")
    

    assert res_a == res_b == "4356-7890", "Ambas funciones deben devolver '4356-7890'"
    print("\n Ambas funciones extrajeron el telefono correctamente!")


if __name__ == "__main__":
    main()