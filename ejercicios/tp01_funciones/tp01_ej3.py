def costo_viajes(viajes: int) -> float:
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

def main():
    viajes = int(input("Ingrese la cantidad de viajes realizados: "))
    total = costo_viajes(viajes)
    print(f"El total gastado en viajes fue de: ${total}")

assert costo_viajes(10) == 16210
assert costo_viajes(25) == 38904
assert costo_viajes(35) == 51061.5
assert costo_viajes(45) == 61598
main()