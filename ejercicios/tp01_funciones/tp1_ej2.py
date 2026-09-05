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


    return dia >= 1 and dia <= dias_del_mes and dias_del_mes != 0

assert fecha_valida(15, 6, 2023) == True
assert fecha_valida(31, 4, 2023) == False
assert fecha_valida(29, 2, 2024) == True
assert fecha_valida(29, 2, 2023) == False
assert fecha_valida(10, 13, 2023) == False


