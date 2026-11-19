def obtener_nombre_mes(numero_mes: int) -> str:
    """
    PRE: Recibe un número entero correspondiente al número de mes.
    POST: Devuelve el nombre del mes si existe en el diccionario.
          Devuelve una cadena vacía si el número de mes es inválido,
          capturando la excepción KeyError.
    """
    meses = {
        1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
        5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
        9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
    }
    
    try:
        # Si numero_mes no está entre 1 y 12, esta línea lanza un KeyError
        return meses[numero_mes]
    except (KeyError, TypeError):
        return ""


def main() -> None:
    cant = 80
    print("=" * cant)
    print("OBTENER NOMBRE DEL MES CON DICCIONARIO (TP5 EJ 3)".center(cant))
    print("=" * cant)

    try:
        num = int(input("\nIngrese el número de mes (1-12): "))
        nombre = obtener_nombre_mes(num)
        
        print("\n--- Resultado ---")
        if nombre:
            print(f"El mes número {num} corresponde a: {nombre}")
        else:
            print(f"Error: El número {num} no corresponde a un mes válido.")
    except ValueError:
        print("\nError: Debe ingresar un número entero válido.")

    print("=" * cant)


if __name__ == "__main__":
    main()