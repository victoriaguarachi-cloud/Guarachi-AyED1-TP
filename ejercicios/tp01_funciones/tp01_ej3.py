def costo_viajes(viajes: int) -> float:
    """
    Calcula el costo total de viajes en subte/transporte aplicando la escala
    de descuentos escalonados según la cantidad de viajes realizados en el mes.

    pre: recibe la cantidad de viajes como un número entero no negativo (>= 0).
    post: devuelve el importe total a pagar como un valor flotante.
    """
    tarifa = 1621

    if viajes <= 20:
        total = viajes * tarifa
    elif viajes <= 30:
        total = 20 * tarifa + (viajes - 20) * (tarifa * 0.80)
    elif viajes <= 40:
        total = 20 * tarifa + 10 * (tarifa * 0.80) + (viajes - 30) * (tarifa * 0.70)
    else:
        total = 20 * tarifa + 10 * (tarifa * 0.80) + 10 * (tarifa * 0.70) + (viajes - 40) * (tarifa * 0.60)

    return total


def main() -> None:
    assert costo_viajes(10) == 16210
    assert costo_viajes(25) == 38904
    assert costo_viajes(35) == 51061.5
    assert costo_viajes(45) == 61598
    print("Todas las pruebas del assert pasaron correctamente.")

    viajes = int(input("Ingrese la cantidad de viajes realizados: "))
    total = costo_viajes(viajes)
    print(f"El total gastado en viajes fue de: ${total}")


if __name__ == "__main__":
    main()