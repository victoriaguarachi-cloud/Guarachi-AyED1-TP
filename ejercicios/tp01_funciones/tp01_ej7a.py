def bisiesto(anio: int) -> bool:
    """
    Determina si un año dado es bisiesto.

    pre: recibe un año entero positivo.
    post: devuelve True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


def dias_del_mes(mes: int, anio: int) -> int:
    """
    Devuelve la cantidad de días que tiene un mes en un año determinado.

    pre: recibe un mes (1 a 12) y un año entero positivo.
    post: devuelve un entero entre 28 y 31 con la cantidad de días del mes.
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif mes in (4, 6, 9, 11):
        return 30
    elif mes == 2:
        if bisiesto(anio):
            return 29
        else:
            return 28
    return 0


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple[int, int, int]:
    """
    Calcula la fecha correspondiente al día siguiente de la fecha ingresada.

    pre: recibe una fecha válida expresada en tres enteros (día, mes, año).
    post: devuelve una tupla (día, mes, año) con la fecha del día posterior.
    """
    if dia < dias_del_mes(mes, anio):
        dia += 1
    elif mes < 12:
        dia = 1
        mes += 1
    else:
        dia = 1
        mes = 1
        anio += 1

    return dia, mes, anio


def sumar_dias(dia: int, mes: int, anio: int, n: int) -> tuple[int, int, int]:
    """
    Suma una cantidad N de días a una fecha determinada.

    pre: recibe día, mes, año válidos y N entero no negativo.
    post: devuelve una tupla (día, mes, año) con la fecha resultante tras sumar N días.
    """
    for _ in range(n):
        dia, mes, anio = dia_siguiente(dia, mes, anio)

    return dia, mes, anio


def main() -> None:
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))
    n = int(input("¿Cuántos días quiere sumar?: "))

    dia_final, mes_final, anio_final = sumar_dias(dia, mes, anio, n)

    print(f"La fecha es: {dia_final}/{mes_final}/{anio_final}")


if __name__ == "__main__":
    main()