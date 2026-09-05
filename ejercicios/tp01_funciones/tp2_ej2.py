def bisiesto(anio):
    return anio % 4 == 0 and anio % 100 !=0 or anio % 400 == 0

def fecha_valida(dia,mes,anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_del_mes= 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_del_mes= 30
    elif mes == 2:
        if bisiesto(anio):
            dias_del_mes=29
        else:
            dias_del_mes=28
    else:
        dias_del_mes=0
        print("Ingrese una fecha valida.")


    return dia >= 1 and dia <= dias_del_mes and dias_del_mes != 0

def main():
    dia=int(input("Ingrese a un dia: "))
    mes=int(input("Ingrese a un mes: "))
    anio=int(input("Ingrese a un anio: "))
    
    if bisiesto(anio):
        print(f"El año {anio} es bisiesto. ")
    else:
        print(f"El año {anio} no es bisiestro.")
        
    fecha= fecha_valida(dia,mes,anio)
    
    if fecha:
        print("La fecha es valida.")
    else:
        print("La fecha no es valida.")

main()