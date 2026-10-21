

def grabar_rango_alturas():
    deporte= input("Ingrese el deporte: ")
    altura= -1
    with open ("ejercicios/tp06_archivos/ALTURAS.txt", "at", encoding="utf-8") as alt:
        alt.write(f"{deporte}\n")
        while altura !=0:
            altura= float(input("Ingrese la altura: "))
            if altura == 0:
                break
            else:
                alt.write(f"{altura}\n")

def grabar_promedio():
    pass
def mostrar_mas_altos():
    pass

grabar_rango_alturas()