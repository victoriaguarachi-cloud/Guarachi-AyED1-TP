def eliminar_claves(diccionario: dict, claves_a_eliminar: list) -> int:
    """
    PRE: Recibe un diccionario y una lista con las claves que se desean eliminar.
    POST: Modifica el diccionario eliminando las claves existentes y devuelve
          la cantidad total de claves eliminadas con éxito.
    """
    eliminadas = 0

    for clave in claves_a_eliminar:
        try:
            del diccionario[clave]
            eliminadas += 1
        except KeyError:
            pass

    return eliminadas


def pedir_claves_a_eliminar() -> list[str]:
    """
    PRE: No recibe parámetros.
    POST: Solicita al usuario una por una las claves que desea eliminar
          hasta que presione Enter vacío. Devuelve la lista de claves.
    """
    claves = []
    print("\n--- Ingrese las claves a eliminar (Enter vacío para finalizar) ---")
    
    while True:
        clave = input("Clave a eliminar: ").strip()
        if not clave:
            break
        claves.append(clave)
        
    return claves


def main() -> None:
    cant = 80
    print("=" * cant)
    print("ELIMINACIÓN DE CLAVES EN UN DICCIONARIO (TP8 EJ 10)".center(cant))
    print("=" * cant)

    datos = {
        "nombre": "Victoria",
        "legajo": "1219320",
        "materia": "AyED1",
        "turno": "Tarde",
        "sede": "Pinamar",
        "estado": "en las ultimas :)"
    }

    print("\nDiccionario disponible para pruebas:")
    for k, v in datos.items():
        print(f"- {k}: {v}")

    claves_eliminar = pedir_claves_a_eliminar()

    if not claves_eliminar:
        print("\nNo se ingresaron claves para eliminar.")
    else:
        cant_eliminadas = eliminar_claves(datos, claves_eliminar)

        print("\n--- Resultado de la operación ---")
        print(f"Claves ingresadas para borrar: {claves_eliminar}")
        print(f"Cantidad de claves eliminadas con éxito: {cant_eliminadas}")
        print(f"Diccionario resultante ({len(datos)} elementos restantes): {datos}")

    print("=" * cant)


if __name__ == "__main__":
    main()