import os

def eliminar_comentarios(ruta_origen: str, ruta_destino: str) -> None:
    """
    PRE: Recibe la ruta de un archivo fuente de Python existente y la ruta de destino.
    POST: Crea el archivo de destino copiando únicamente las líneas que no son comentarios (#).
          Captura excepciones ante errores de lectura o escritura.
    """
    try:
        with open(ruta_origen, "rt", encoding="utf-8") as f_origen, \
             open(ruta_destino, "wt", encoding="utf-8") as f_destino:
            
            lineas_totales = 0
            comentarios_eliminados = 0

            for linea in f_origen:
                lineas_totales += 1
                # Si quitando los espacios de la sangría empieza con '#', es un comentario
                if linea.lstrip().startswith("#"):
                    comentarios_eliminados += 1
                    continue
                
                f_destino.write(linea)

        print("\n--- Proceso completado ---")
        print(f"Líneas totales leídas: {lineas_totales}")
        print(f"Líneas de comentarios descartadas: {comentarios_eliminados}")
        print(f"Archivo limpio generado en: '{ruta_destino}'")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo origen '{ruta_origen}'.")
    except OSError as e:
        print(f"Error del sistema de archivos al procesar: {e}")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("ELIMINACIÓN DE COMENTARIOS EN ARCHIVOS PYTHON (TP6 EJ 4)".center(cant))
    print("=" * cant)

    directorio = "ejercicios/tp06_archivos/tp06_ej4"
    os.makedirs(directorio, exist_ok=True)
    
    ruta_entrada = os.path.join(directorio, "codigo_con_comentarios.py")
    with open(ruta_entrada, "wt", encoding="utf-8") as f:
        f.write("# Archivo de prueba con comentarios\n")
        f.write("def sumar(a: int, b: int) -> int:\n")
        f.write("    # Suma dos números enteros\n")
        f.write("    resultado = a + b\n")
        f.write("    return resultado\n")
        f.write("\n")
        f.write("# Llamada principal\n")
        f.write("print(sumar(5, 3))\n")

    print(f"Archivo de prueba generado: {ruta_entrada}")

    ruta_salida = os.path.join(directorio, "codigo_limpio.py")
    
    print(f"Generando versión sin comentarios en: {ruta_salida}...")
    eliminar_comentarios(ruta_entrada, ruta_salida)

    print("=" * cant)


if __name__ == "__main__":
    main()