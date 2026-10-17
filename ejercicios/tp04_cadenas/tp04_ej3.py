def obtener_claves(clave_maestra: int) -> tuple[int, int]:
    """
    PRE: Recibe un número entero representando la clave maestra.
    POST: Devuelve una tupla (clave1, clave2) donde:
          - clave1 tiene los dígitos en posiciones impares (desde la izquierda).
          - clave2 tiene los dígitos en posiciones pares.
    """
    clave_str = str(clave_maestra)
    
    clave1_str = clave_str[0::2]
    
    clave2_str = clave_str[1::2]
    
    return int(clave1_str), int(clave2_str)


def main() -> None:
    clave_maestra = 18293
    c1, c2 = obtener_claves(clave_maestra)
    
    print(f"Clave maestra: {clave_maestra}")
    print(f"Clave 1 (posiciones impares): {c1}")
    print(f"Clave 2 (posiciones pares):   {c2}")
    
    print("\n- Proba con otra clave maestra -")
    try:
        entrada = int(input("Ingresa un numero de clave maestra: "))
        clave1, clave2 = obtener_claves(entrada)
        print(f"Clave 1: {clave1}")
        print(f"Clave 2: {clave2}")
    except ValueError:
        print("Error: Ingrese un numero entero valido.")


if __name__ == "__main__":
    main()