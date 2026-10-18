#  Utilizando sólo ciclos normales
def filtrar_palabras_ciclos(frase: str, n: int) -> str:
    """

    pre: Recibe una cadena de texto y un entero N
    post: Devuelve una cadena con las palabras que tienen N o más caracteres
    """
    palabras = frase.split()
    resultado = []
    
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
            
    return " ".join(resultado)


#  Utilizando listas por comprensión
def filtrar_palabras_comprension(frase: str, n: int) -> str:
    """
    pre: Recibe una cadena de texto y un entero N
    post: Devuelve una cadena con las palabras que tienen N o más caracteres
    """
    palabras = frase.split()
    filtradas = [palabra for palabra in palabras if len(palabra) >= n]
    return " ".join(filtradas)


#  Utilizando la función filter con lambda
def filtrar_palabras_filter(frase: str, n: int) -> str:
    """
    PRE: Recibe una cadena de texto y un entero N.
    POST: Devuelve una cadena con las palabras que tienen N o más caracteres.
    """
    palabras = frase.split()
    filtradas = filter(lambda palabra: len(palabra) >= n, palabras)
    return " ".join(filtradas)



def main() -> None:
    texto = "Hoy es un gran dia para practicar funciones en Python!!! :/"
    n = 5
    
    print(f"Frase original: '{texto}'")
    print(f"Filtrando palabras con {n} o más caracteres:\n")
    
    res_a = filtrar_palabras_ciclos(texto, n)
    res_b = filtrar_palabras_comprension(texto, n)
    res_c = filtrar_palabras_filter(texto, n)
    
    print(f"a. Ciclos normales:     '{res_a}'")
    print(f"b. Lista por comprensión: '{res_b}'")
    print(f"c. Función filter:       '{res_c}'")
    
    assert res_a == res_b == res_c, "Las tres funciones deben devolver el mismo resultado"
    print("\nLas 3 versiones funcionan exactamente igual!")


if __name__ == "__main__":
    main()