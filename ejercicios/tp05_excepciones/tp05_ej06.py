def cargar_lista() -> list[int]:
    """
    PRE: No recibe parámetros.
    POST: Devuelve una lista de enteros ingresados por teclado.
          La carga finaliza al ingresar el valor -1.
    """
    lista = []
    print("--- Carga de la lista (ingrese -1 para finalizar) ---")
    
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            if num == -1:
                break
            lista.append(num)
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
            
    return lista


def buscar_elementos(lista: list[int]) -> None:
    """
    PRE: Recibe la lista de enteros previamente cargada.
    POST: Permite buscar elementos usando .index() y muestra su posición.
          Captura ValueError si no existe el elemento.
          Aborta el proceso al detectar 3 errores de búsqueda.
    """
    errores = 0
    max_errores = 3
    
    print("\n--- Búsqueda de elementos ---")
    
    while errores < max_errores:
        try:
            buscado = int(input(f"\n[{errores}/{max_errores} errores] Ingrese un número a buscar: "))
            
            # Usamos directamente .index() sin consultar con 'in'
            posicion = lista.index(buscado)
            print(f"¡Encontrado! El número {buscado} está en la posición (índice) {posicion}.")
            
        except ValueError as e:
            if "is not in list" in str(e):
                errores += 1
                print(f"Error ({errores}/{max_errores}): El número {buscado} no pertenece a la lista.")
            else:
                errores += 1
                print(f"Error ({errores}/{max_errores}): Ingreso inválido. Debe ingresar un entero.")

    print(f"\nProceso abortado por alcanzar el límite de {max_errores} errores.")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("BÚSQUEDA EN LISTA CON INDEX Y EXCEPCIONES (TP5 EJ 6)".center(cant))
    print("=" * cant)

    numeros = cargar_lista()
    
    if numeros:
        print(f"\nLista cargada con éxito: {numeros}")
        buscar_elementos(numeros)
    else:
        print("\nLa lista quedó vacía. Fin del programa.")

    print("=" * cant)


if __name__ == "__main__":
    main()