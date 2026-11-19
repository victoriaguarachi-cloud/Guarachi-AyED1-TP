def generar_diccionario_cuadrados() -> dict[int, int]:
    """
    PRE: No recibe parámetros.
    POST: Devuelve un diccionario donde las claves son enteros de 1 a 20 
          y los valores son sus respectivos cuadrados.
    """
    return {numero: numero ** 2 for numero in range(1, 21)}


def main() -> None:
    cant = 80
    print("=" * cant)
    print("DICCIONARIO DE CUADRADOS (TP8 EJ 8)".center(cant))
    print("=" * cant)

    cuadrados = generar_diccionario_cuadrados()
    
    print("\nNúmero -> Cuadrado:")
    for num, cuad in cuadrados.items():
        print(f"{num:2d}² = {cuad:3d}")

    print("=" * cant)


if __name__ == "__main__":
    main()