def contar_subcadena_ordenada(cadena: str, subcadena: str) -> int:
    """
    PRE: Recibe la cadena principal y la subcadena a buscar.
    POST: Devuelve la cantidad de veces que aparece la subcadena en orden,
          sin requerir que las letras sean consecutivas e ignorando mayúsculas.
    """
    if not cadena or not subcadena:
        return 0

    cadena = cadena.lower()
    subcadena = subcadena.lower()

    # conteos[0] = 1 (representa la cadena vacía)
    # conteos[1..N] se inicializan en 0
    conteos = [1] + [0] * len(subcadena)

    for caracter_texto in cadena:
        # Recorremos la subcadena de atrás hacia adelante para no sobreescribir
        for i in range(len(subcadena) - 1, -1, -1):
            if caracter_texto == subcadena[i]:
                conteos[i + 1] += conteos[i]

    return conteos[-1]


def main() -> None:
    texto = (
        "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, "
        "que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos "
        "escarabajos de cristal negro."
    )
    sub = "UADE"

    cantidad = contar_subcadena_ordenada(texto, sub)

    print("--- CONTADOR DE SUBCADENAS NO CONSECUTIVAS ---")
    print(f"Subcadena buscada: '{sub}'")
    print(f"Cantidad encontrada: {cantidad}")


if __name__ == "__main__":
    main()