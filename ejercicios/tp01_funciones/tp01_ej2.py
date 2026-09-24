def bisiesto(anio: int) -> bool:
    """
    Determina si un año dado es bisiesto.

    pre: recibe un año entero positivo.
    post: devuelve True si el año es bisiesto, False en caso contrario.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0


def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Verifica si una fecha compuesta por día, mes y año es válida.

    pre: recibe día, mes y año como números enteros.
    post: devuelve True si la fecha existe en el calendario, False en caso contrario.
    """
    if mes in (1, 3, 5, 7, 8, 10, 12):
        dias_del_mes = 31
    elif mes in (4, 6, 9, 11):
        dias_del_mes = 30
    elif mes == 2:
        if bisiesto(anio):
            dias_del_mes = 29
        else:
            dias_del_mes = 28
    else:
        dias_del_mes = 0

    return 1 <= dia <= dias_del_mes and dias_del_mes != 0


def main() -> None:
    assert fecha_valida(15, 6, 2023) == True
    assert fecha_valida(31, 4, 2023) == False
    assert fecha_valida(29, 2, 2024) == True
    assert fecha_valida(29, 2, 2023) == False
    assert fecha_valida(10, 13, 2023) == False

    print("Todas las pruebas del assert pasaron correctamente.")


if __name__ == "__main__":
    main()
