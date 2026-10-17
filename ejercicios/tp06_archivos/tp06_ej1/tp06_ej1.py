try:
    with open("ejercicios/tp06_archivos/personas.txt", "rt", encoding="utf-8") as datos:
        for linea in datos:
            linea_limpia = linea.strip()
            if not linea_limpia or "," not in linea_limpia:
                continue
            
            apellido, nombre = linea_limpia.split(",")
            apellido_mayus = apellido.strip().upper()
            
            if apellido_mayus.endswith("IAN"):
                with open("ejercicios/tp06_archivos/ARMENIA.txt", "a", encoding="utf-8") as arm:
                    arm.write(linea_limpia + "\n")
            elif apellido_mayus.endswith("INI"):
                with open("ejercicios/tp06_archivos/ITALIA.txt", "a", encoding="utf-8") as it:
                    it.write(linea_limpia + "\n")
            elif apellido_mayus.endswith("EZ"):
                with open("ejercicios/tp06_archivos/ESPANIA.txt", "a", encoding="utf-8") as esp:
                    esp.write(linea_limpia + "\n")

except FileNotFoundError:
    print('No se encuentra el archivo personas.txt')
except OSError:
    print("Error al abrir el archivo")
except:
    print("error de los datos")
else:
    print("Arhivo creado")