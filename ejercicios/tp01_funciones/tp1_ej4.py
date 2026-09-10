def calcular_cambio(total:int, recibido:int) -> list[str] | None:
    if recibido < total: #detecta error si paga con menos del total
        return None

    vuelto= recibido - total
    billetes= [5000,1000,500,200,100,50,10]
    resultado= []

    for billete in billetes:
        cantidad= vuelto // billete
        vuelto= vuelto % billete

        if cantidad > 0:
            resultado.append(f"{cantidad} billete/s de ${billete}")

    if vuelto != 0:
        return None #detecta el error si no se puede cubrir todo el cambio (no hay billetes de 1 peso)

    return resultado

def main() -> None:
    total= int(input("Ingrese el monto total a pagar: "))
    recibido= int(input("Ingrese el monto recibido: "))
    cambio= calcular_cambio(total,recibido)

    if cambio is None:
        print("Error: el dinero es insuficiente o no se puede entregar el vuelto exacto con los billetes disponibles.")
    else:
        print("El vuelto a entregar es:")
        for i in cambio:
            print(i)

