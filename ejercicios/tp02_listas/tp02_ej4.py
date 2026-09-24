import random as rn

def generar_lista(n: int) -> list:
    """
    genera una lista de n numeros enteros al azar entre 1 y 10.

    pre: recibe n (entero mayor a 0)
    post: devuelve una lista con n numeros aleatorios.
    """
    return [rn.randint(1,10) for _ in range(n)]

def eliminar_elementos(original: list[int], a_eliminar: list[int]) -> None:
    """
    Elimina de la lista original los elementos presentes en la segunda lista.
    Modifica la lista original.

    pre: recibe dos listas de numeros enteros
    post: la lista original queda modificada sin los elementos de la segunda
    """
    for elemento in a_eliminar:
        while elemento in original:
            original.remove(elemento)

def main() -> None:
    lista_original= generar_lista(10)
    valores_a_eliminar= generar_lista(3)

    print(f"Lista original:{lista_original}")
    print(f"Valores a eliminar: {valores_a_eliminar}")

    eliminar_elementos(lista_original, valores_a_eliminar)

    print(f"lista resultante: {lista_original}")

main()
