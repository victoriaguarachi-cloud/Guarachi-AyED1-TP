import math

def calcular_raiz_cuadrada() -> None:
    """
    PRE: No recibe parámetros. Solicita al usuario un número por teclado.
    POST: Calcula e imprime la raíz cuadrada del número ingresado.
          Maneja excepciones en caso de ingresos no numéricos o números negativos.
    """
    try:
        entrada = input("\nIngrese un número para calcular su raíz cuadrada: ")
        numero = float(entrada)
        
        if numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada real de un número negativo.")
            
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")

    except ValueError as e:
        if "math domain error" in str(e):
            print("Error: No existe la raíz cuadrada de un número negativo en los números reales.")
        elif "could not convert string to float" in str(e):
            print("Error: Debe ingresar un valor numérico válido.")
        else:
            print(f"Error: {e}")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("CÁLCULO DE RAÍZ CUADRADA CON EXCEPCIONES (TP5 EJ 5)".center(cant))
    print("=" * cant)

    calcular_raiz_cuadrada()

    print("=" * cant)


if __name__ == "__main__":
    main()