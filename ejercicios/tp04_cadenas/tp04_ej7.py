
def eliminar_subcadena_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: Recibe una cadena, una posición de inicio y la cantidad de caracteres a eliminar
    post: Devuelve una nueva cadena con la subcadena eliminada usando rebanadas
    """
    parte_inicial = cadena[:posicion]
    parte_final = cadena[posicion + cantidad:]
    return parte_inicial + parte_final


def eliminar_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """
    pre: Recibe una cadena, una posición de inicio y la cantidad de caracteres a eliminar
    post: Devuelve una nueva cadena concatenando caracter por caracter sin usar rebanadas
    """
    resultado = ""
    inicio_borrado = posicion
    fin_borrado = posicion + cantidad

    for i in range(len(cadena)):
        if not (inicio_borrado <= i < fin_borrado):
            resultado += cadena[i]

    return resultado


def main() -> None:
    texto = "El numero de telfono es 4356-7890"
    pos = 25
    cant = 10
    
    print(f"Cadena original: '{texto}'")
    print(f"Eliminar desde la posicion {pos}, {cant} caracteres:\n")
    
    res_a = eliminar_subcadena_rebanadas(texto, pos, cant)
    res_b = eliminar_subcadena_sin_rebanadas(texto, pos, cant)
    
    print(f"a. Con rebanadas: '{res_a}'")
    print(f"b. Sin rebanadas: '{res_b}'")
    
    assert res_a == res_b, "Ambas funciones deben devolver el mismo resultado"
    print("Ambas funciones eliminaron el tramo correctamente!")


if __name__ == "__main__":
    main()