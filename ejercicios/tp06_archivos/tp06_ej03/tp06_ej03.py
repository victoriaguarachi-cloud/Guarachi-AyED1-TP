import os

def procesar_promedios(ruta_origen: str, ruta_destino: str) -> None:
    """
    PRE: Recibe la ruta del archivo origen con formato 'Nombre,Nota1,Nota2,...' y la ruta destino.
    POST: Calcula el promedio de calificaciones por alumno y genera el archivo destino
          con formato 'Nombre,Promedio'. Captura excepciones de archivo y formato numérico.
    """
    try:
        with open(ruta_origen, "rt", encoding="utf-8") as entrada, \
             open(ruta_destino, "wt", encoding="utf-8") as salida:

            for linea in entrada:
                linea_limpia = linea.strip()
                if not linea_limpia:
                    continue

                partes = linea_limpia.split(",")
                nombre = partes[0].strip()
                notas = [float(nota) for nota in partes[1:] if nota.strip()]

                if notas:
                    promedio = sum(notas) / len(notas)
                    salida.write(f"{nombre},{promedio:.2f}\n")

        print(f"\nArchivo procesado con éxito. Resultados guardados en:\n{ruta_destino}")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_origen}'.")
    except OSError as e:
        print(f"Error del sistema de archivos: {e}")
    except ValueError as e:
        print(f"Error al convertir calificaciones a números: {e}")


def main() -> None:
    cant = 80
    print("=" * cant)
    print("PROMEDIO DE ALUMNOS EN ARCHIVOS (TP6 EJ 3)".center(cant))
    print("=" * cant)

    directorio = "ejercicios/tp06_archivos/tp06_ej03"
    ruta_datos = os.path.join(directorio, "alumnos_notas.txt")
    ruta_promedios = os.path.join(directorio, "alumnos_promedios.txt")

    with open(ruta_datos, "wt", encoding="utf-8") as f:
        f.write("Gomez Juan,7,8,9\n")
        f.write("Perez Maria,4,6,5\n")
        f.write("Lopez Carlos,10,9,8,10\n")

    print(f"Leyendo desde: {ruta_datos}")
    procesar_promedios(ruta_datos, ruta_promedios)

    print("=" * cant)


if __name__ == "__main__":
    main()