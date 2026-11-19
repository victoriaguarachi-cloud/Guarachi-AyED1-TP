import os

def dividir_archivo(ruta_origen: str, tamano_maximo: int) -> None:
    """
    PRE: Recibe la ruta del archivo a dividir y el tamaño máximo en bytes de cada parte.
    POST: Genera partes numeradas del archivo respetando los saltos de línea y sin
          cargar el archivo completo en memoria. Informa si ocurre un error.
    """
    if tamano_maximo <= 0:
        raise ValueError("El tamaño máximo debe ser mayor a 0 bytes.")

    nombre_base, extension = os.path.splitext(ruta_origen)

    try:
        with open(ruta_origen, "rt", encoding="utf-8") as archivo_origen:
            numero_parte = 1
            tamano_actual = 0
            archivo_parte = None

            try:
                for linea in archivo_origen:
                    bytes_linea = len(linea.encode("utf-8"))

                    if bytes_linea > tamano_maximo:
                        raise ValueError(
                            f"Existe un registro que supera el tamaño máximo permitido ({bytes_linea} > {tamano_maximo} bytes)."
                        )

                    # Si sumar la línea excede el tope y el archivo actual ya tiene contenido, cambiamos de parte
                    if archivo_parte is not None and (tamano_actual + bytes_linea > tamano_maximo):
                        archivo_parte.close()
                        numero_parte += 1
                        archivo_parte = None
                        tamano_actual = 0

                    if archivo_parte is None:
                        nombre_salida = f"{nombre_base}_parte{numero_parte}{extension}"
                        archivo_parte = open(nombre_salida, "wt", encoding="utf-8")

                    archivo_parte.write(linea)
                    tamano_actual += bytes_linea

            finally:
                if archivo_parte is not None:
                    archivo_parte.close()

        print(f"\nProceso finalizado: se generaron {numero_parte} archivo(s) de salida.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_origen}'.")
    except OSError as e:
        print(f"Error del sistema de archivos al procesar: {e}")
    except ValueError as e:
        print(f"Error en la partición: {e}")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("DIVISIÓN DE ARCHIVO EN PARTES (TP6 EJ 2)".center(cant))
    print("=" * cant)

    directorio = "ejercicios/tp06_archivos/tp06_ej2"
    os.makedirs(directorio, exist_ok=True)

    ruta_archivo = os.path.join(directorio, "archivo_prueba.txt")

    with open(ruta_archivo, "wt", encoding="utf-8") as f:
        f.write("Primera línea de prueba corta.\n")
        f.write("Segunda línea con un texto un poco más extenso para sumar volumen.\n")
        f.write("Tercera línea.\n")
        f.write("Cuarta línea final.\n")

    print(f"Archivo de prueba creado en: {ruta_archivo}")


    limite = 70
    print(f"Dividiendo en partes de hasta {limite} bytes...\n")
    dividir_archivo(ruta_archivo, limite)

    print("=" * cant)


if __name__ == "__main__":
    main()