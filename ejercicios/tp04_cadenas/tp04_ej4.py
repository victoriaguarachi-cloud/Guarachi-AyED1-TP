def entero_a_romano(numero: int) -> str:
    if not (0 < numero <= 3999):
        raise ValueError("El número debe estar entre 1 y 3999.")

    tabla = {
        1000: "M",  900: "CM", 500: "D", 400: "CD",
        100: "C",   90: "XC",  50: "L",  40: "XL",
        10: "X",    9: "IX",   5: "V",   4: "IV",
        1: "I"
    }
    
    romano = ""
    
    for valor, simbolo in tabla.items():
        while numero >= valor:
            romano += simbolo
            numero -= valor
            
    return romano

def main() -> None:
    ejemplos = [1, 4, 9, 49, 99, 400, 1987, 2024, 3999]
    
    print("- CONVERSION A NUMEROS ROMANOS -")
    for num in ejemplos:
        print(f"{num:4d} -> {entero_a_romano(num)}")

    print("\n- Proba con tu propio numero -")
    try:
        val = int(input("Ingresa un entero entre 1 y 3999: "))
        print(f"Resultado: {entero_a_romano(val)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()