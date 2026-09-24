def maximo_unico(a: int, b: int, c: int) -> int:
    numeros = [a,b,c]
    mayor= max(numeros)
    cantidad= numeros.count(mayor)

    if cantidad == 1:
        return mayor
    else:
        return -1

def main():
    primero= int(input("Ingrese el primer numero: "))
    segundo= int(input("Ingrese el segundo numero: "))
    tercero= int(input("Ingrese el tercer numero: "))

    resultado= maximo_unico(primero,segundo,tercero)

    if resultado == -1:
        print("No hay maximo unico")
    else:
        print(f"El valor maximo es: {resultado}")

main()
