import random as rn

def cargar_lista() -> list[int]: 
    """
    carga una lista con n numeros enteros al azar de 4 digitos, la cantidad n de elementos es un numero al azar de 2 digitos.
    pre:ninguna.
    post: devuelve una lista con n enteros aleatorios de cuatro digitos.
    """
    cantidad = rn.randint(10,99)
    return [rn.randint(1000,9999) for _ in range(cantidad)]
    
def calcular_producto(lista:list[int]) -> int:
    """
    calcula el producto de todos los elementos de una lista de enteros.

    pre: recibe una lista de enteros no vacia.
    post: devuelve el resultado de multiplicar todos los elementos entre si.
    """

    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista: list[int], valor: int) -> None:
    """
    Elimina todas las apariciones de un valor en la lista recibida.
    Modifica la lista sin utilizar lineas auxiliares.
    
    pre: recibe una lista de enteros y el valor entero a eliminar.
    post: la lista queda modificada sin ninguna ocurrencia de tal valor.
    
    """
    while valor in lista:
        lista.remove(valor)

def es_capicua(lista:list) -> bool:
    """
    Determina si el contenido de una lista es capicua comparando los elementos desde los extremos hacia el centro sin usar listas auxiliares.

    pre: recibe una lista de cualquier tipo de elementos
    post: devuelve True si es capicua, False si no lo es.
    """
    i = 0 
    j = len(lista) - 1

    while i < j:
        if lista[i] != lista[j]:
            return False
        i += 1
        j -= 1

    return True

def main() -> None:
    numeros= cargar_lista()
    print(f"Lista cargada: {numeros} ")

    producto = calcular_producto(numeros)
    print(f"Producto de los elementos: {producto}")

    valor_a_buscar= int(input("Ingrese un valor a buscar y eliminar: "))
    eliminar_valor(numeros, valor_a_buscar)
    print(f"Lista luego de eliminar el valor: {numeros}")

    print(f"La lista actual es capicua?: {es_capicua(numeros)}")

if __name__ == "__main__":
    main()