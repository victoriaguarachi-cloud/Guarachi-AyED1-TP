def calcular_cambio(total: int, recibido: int) -> list[str] | None:
    """
    Calcula el vuelto a entregar desglosado en billetes utilizando un algoritmo goloso (greedy).

    pre: recibe dos enteros no negativos (total a pagar y monto recibido).
    post: devuelve una lista de cadenas indicando la cantidad y denominación de billetes a entregar,o None si el pago es insuficiente o si no se puede entregar el vuelto exacto.
    """
    if recibido < total:
        return None

    vuelto = recibido - total
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    resultado = []

    for billete in billetes:
        cantidad = vuelto // billete
        vuelto = vuelto % billete

        if cantidad > 0:
            resultado.append(f"{cantidad} billete/s de ${billete}")

    if vuelto != 0:
        return None  # detecta si no se puede cubrir todo el cambio (ej. faltante de billetes menores)

    return resultado


def main() -> None:
    total = int(input("Ingrese el monto total a pagar: "))
    recibido = int(input("Ingrese el monto recibido: "))
    cambio = calcular_cambio(total, recibido)

    if cambio is None:
        print("Error: el dinero es insuficiente o no se puede entregar el vuelto exacto con los billetes disponibles.")
    else:
        print("El vuelto a entregar es:")
        for item in cambio:
            print(item)


if __name__ == "__main__":
    main()