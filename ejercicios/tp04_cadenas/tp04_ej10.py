def reemplazar_palabra(cadena: str, a_cambiar: str, reemplazo: str) -> tuple[str, int]:
    """
    pre: Recibe la cadena original, la palabra a reemplazar y la nueva palabra
    post: Devuelve una tupla con (cadena_resultante, cantidad_reemplazos) reemplazando únicamente palabras completas
    """
    palabras = cadena.split()
    salida = []
    reemplazos = 0
    
    for palabra in palabras:
        palabra_limpia = "".join([caracter for caracter in palabra if caracter.isalnum()])
        
        if palabra_limpia.lower() == a_cambiar.lower():
            palabra_modificada = palabra.replace(palabra_limpia, reemplazo)
            salida.append(palabra_modificada)
            reemplazos += 1
        else:
            salida.append(palabra)

    return " ".join(salida), reemplazos


def main() -> None:
    centrar = 80

    print(f"{'REEMPLAZO DE PALABRAS COMPLETAS':^{centrar}}")
    
    s = input("\nIngrese la frase a trabajar: ")
    a_cambiar = input("Ingrese la palabra a reemplazar: ")
    reemplazo = input("Ingrese la palabra nueva: ")
    
    resultado, cantidad = reemplazar_palabra(s, a_cambiar, reemplazo)
    
    print("\n--- Resultado ---")
    print(f"Texto modificado: {resultado}")
    print(f"Cantidad de reemplazos realizados: {cantidad}")
    print("=" * centrar)


if __name__ == "__main__":
    main()