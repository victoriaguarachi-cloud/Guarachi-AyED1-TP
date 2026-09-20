import random as rn

def generar_lista(n: int) -> list:
    """
    Genera una lista de n numeros enteros al azar entre 1 y 100

    pre: recibe n (numeros positivos mayores a 0).
    post: devuelve una lista con n numeros aleatorios.
    """
    return [rn.randint(1,100) for _ in range(n)]

def filtrar_impares(lista:list) -> list:
    """
    Filtra los numeros impares de una lista dada usando filter y lambda

    pre: recibe una lista de enteros
    post: devuelve una nueva lista conteniendo solo los numeros impares
    """
    return list(filter(lambda x: x % 2 != 0, lista))

def main() -> None:
    lista_original= generar_lista(20)
    lista_impares= filtrar_impares(lista_original)

    print(f"Lista orginal: {lista_original}")
    print(f"Lista de impares: {lista_impares}")

main()