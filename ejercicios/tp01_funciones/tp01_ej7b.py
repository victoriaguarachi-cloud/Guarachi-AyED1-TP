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

def dias_entre_fechas(dia1:int,mes1:int,anio1:int,dia2:int,mes2:int,anio2:int) -> int:
    contador=0
    while dia1 != dia2 or mes1 != mes2 or anio1 != anio2:
        dia1,mes1,anio1 = dia_siguiente(dia1,mes1,anio1)
        contador += 1
    return contador

def main():
    print("-"*50)
    print("Primera fecha".center(50))
    dia1=int(input("Ingrese el dia: "))
    mes1=int(input("Ingrese el mes: "))
    anio1=int(input("Ingrese el anio: "))
    print("-"*50)
    print("Segunda fecha".center(50))
    dia2=int(input("Ingrese el dia: "))
    mes2=int(input("Ingrese el mes: "))
    anio2=int(input("Ingrese el anio: "))
    print("-"*50)
    diferencia= dias_entre_fechas(dia1,mes1,anio1,dia2,mes2,anio2)

    print(f"Hay {diferencia} dias de diferencia entre esas fechas.")

main()
