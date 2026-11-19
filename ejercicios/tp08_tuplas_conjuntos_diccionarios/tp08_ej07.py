def eliminar_elementos_conjunto(conjunto: set[int]) -> None:
    """
    PRE: Recibe un conjunto mutable de enteros.
    POST: Solicita valores por teclado y los elimina del conjunto utilizando el
          método .remove(). Captura KeyError si el elemento no existe y ValueError
          ante ingresos no numéricos. Finaliza al ingresar -1 o si el conjunto queda vacío.
    """
    print("\n--- Eliminación de elementos (ingrese -1 para terminar) ---")

    while conjunto:
        print(f"\nEstado actual del conjunto ({len(conjunto)} elementos): {sorted(conjunto)}")
        
        try:
            entrada = input("Ingrese número a eliminar: ")
            valor = int(entrada)

            if valor == -1:
                print("Finalizando ingreso a pedido del usuario.")
                break

            conjunto.remove(valor)
            print(f"El número {valor} fue eliminado con éxito.")

        except KeyError:
            print(f"Error: El número {valor} no se encuentra en el conjunto.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    if not conjunto:
        print("\nEl conjunto se ha quedado sin elementos.")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("ELIMINACIÓN EN CONJUNTOS CON .remove() (TP8 EJ 7)".center(cant))
    print("=" * cant)

    numeros = set(range(10))
    print(f"Conjunto inicial: {numeros}")

    eliminar_elementos_conjunto(numeros)

    print("\n--- Resultado final ---")
    print(f"Contenido final del conjunto: {sorted(numeros) if numeros else 'Conjunto vacío'}")
    print("=" * cant)


if __name__ == "__main__":
    main()