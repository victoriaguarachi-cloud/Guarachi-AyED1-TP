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


def dias_entre_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int) -> int:
    """
    Calcula la cantidad de días de diferencia entre dos fechas distintas.

    pre: recibe dos fechas válidas donde la primera fecha es cronológicamente anterior o igual a la segunda.
    post: devuelve un entero con la cantidad de días transcurridos entre ambas fechas.
    """
    contador = 0
    while dia1 != dia2 or mes1 != mes2 or anio1 != anio2:
        dia1, mes1, anio1 = dia_siguiente(dia1, mes1, anio1)
        contador += 1
    return contador


def main() -> None:
    print("-" * 50)
    print("Primera fecha".center(50))
    dia1 = int(input("Ingrese el dia: "))
    mes1 = int(input("Ingrese el mes: "))
    anio1 = int(input("Ingrese el anio: "))

    print("-" * 50)
    print("Segunda fecha".center(50))
    dia2 = int(input("Ingrese el dia: "))
    mes2 = int(input("Ingrese el mes: "))
    anio2 = int(input("Ingrese el anio: "))

    print("-" * 50)
    diferencia = dias_entre_fechas(dia1, mes1, anio1, dia2, mes2, anio2)
    print(f"Hay {diferencia} dias de diferencia entre esas fechas.")


if __name__ == "__main__":
    main()
