def es_capicua(cadena: str) -> bool:
    """
    Determina si una numero/palabra/frase es capicua.
    pre:recibe una cadena de texto como parametro 
    post: devuelve False en caso de no ser capicua y True si es capicua
    """

    cadena_limpia = cadena.lower().replace(" ", "")
    
    inicio = 0
    fin = len(cadena_limpia) - 1
    
    while inicio < fin:
        if cadena_limpia[inicio] != cadena_limpia[fin]:
            return False 
        
        inicio += 1
        fin -= 1
        
    return True 

def main()-> None:
    ejemplos = [
        "Neuquen",
        "12321",
        "Anilina",
        "Anita lava la tina",
        "Python",
        "123456"
    ]
    
    print("-VERIFICACION DE CADENAS CAPICUA-")
    for texto in ejemplos:
        resultado = es_capicua(texto)
        print(f"'{texto}' -> {'Es capicua' if resultado else 'NO es capicua'}")


    print("\n--- Proba con tu propia frase o numero ---")
    usuario_input = input("Ingresa un texto o numero: ")
    if es_capicua(usuario_input):
        print(f"'{usuario_input}' es capicua")
    else:
        print(f"'{usuario_input}' no es capicua.")

if __name__ == "__main__":
    main()