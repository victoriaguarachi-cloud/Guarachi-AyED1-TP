def bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and anio % 100 !=0 or anio % 400 == 0

def dias_del_mes(mes: int,anio:int) -> int:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        return 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    elif mes == 2:
        if bisiesto(anio):
            return 29
        else:
            return 28

def dia_siguiente(dia: int,mes: int,anio:int) -> tuple:
    if dia < dias_del_mes(mes,anio):
        dia += 1
    elif mes < 12:
        dia = 1
        mes= mes + 1
    else:
        dia = 1
        mes = 1
        anio = anio + 1

    return dia,mes,anio


def sumar_dias(dia:int,mes:int,anio:int,n:int)-> tuple:
    for _ in range(n):
        dia,mes,anio= dia_siguiente(dia,mes,anio)

    return dia,mes,anio

def main():
    dia=int(input("Ingrese el dia: "))
    mes=int(input("ingrese el mes: "))
    anio=int(input("Ingrese el anio: "))
    n= int(input("Cuantos dias quiere sumas?: "))

    dia_final, mes_final, anio_final = sumar_dias(dia,mes,anio,n)

    print(f"La fecha es: {dia_final}/{mes_final}/{anio_final}")
    
main()