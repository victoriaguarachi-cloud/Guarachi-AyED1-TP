def ingresar_numero_natural() -> int:
    """
    PRE: No recibe parámetros. Solicita al usuario el ingreso de un dato por teclado.
    POST: Devuelve un número entero estrictamente mayor que 0 (número natural).
          Rechaza ingresos no numéricos, flotantes o menores/iguales a 0 notificando
          la razón exacta del error.
    """
    while True:
        try:
            entrada = input("Ingrese un número natural: ")
            numero = int(entrada)
            
            if numero <= 0:
                raise ValueError(f"El número {numero} no es natural (debe ser mayor que 0).")
                
            return numero
            
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Error de ingreso: Debe ingresar un número entero válido (sin letras ni decimales).")
            else:
                print(f"Error de ingreso: {e}")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("VALIDACIÓN DE NÚMEROS NATURALES (TP5 EJ 1)".center(cant))
    print("=" * cant)
    
    print("\nSolicitando ingreso de número natural...")
    numero_valido = ingresar_numero_natural()
    
    print("\n--- Resultado ---")
    print(f"¡Número ingresado con éxito!: {numero_valido}")
    print("=" * cant)


if __name__ == "__main__":
    main()