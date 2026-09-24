def cargar_pacientes() -> tuple[list[int], list[int]]:
    """
    Solicita el ingreso de pacientes hasta que se ingresa -1 como número de afiliado.
    Clasifica a los pacientes según su condición (urgencia o turno).

    pre: el usuario ingresa enteros de 4 dígitos para afiliados y 0/1 para tipo de atención.
    post: devuelve una tupla con dos listas: (urgencias, turnos).
    """
    urgencias = []
    turnos = []

    afiliado = int(input("Ingrese número de afiliado (-1 para finalizar): "))
    while afiliado != -1:
        tipo = int(input("Ingrese tipo de atención (0: Urgencia, 1: Turno): "))

        if tipo == 0:
            urgencias.append(afiliado)
        elif tipo == 1:
            turnos.append(afiliado)
        else:
            print("Tipo de atención inválido. Se ignora el ingreso.")

        afiliado = int(input("\nIngrese número de afiliado (-1 para finalizar): "))

    return urgencias, turnos


def mostrar_listados(urgencias: list[int], turnos: list[int]) -> None:
    """
    Muestra los listados de pacientes atendidos por urgencia y por turno en orden de llegada.

    pre: recibe las dos listas de enteros.
    post: imprime las dos listas por pantalla.
    """
    print("--Listado de Pacientes por Urgencia--")
    if len(urgencias) == 0:
        print("No se registraron urgencias.")
    else:
        print(urgencias)

    print("--Listado de Pacientes por Turno--")
    if len(turnos) == 0:
        print("No se registraron turnos.")
    else:
        print(turnos)


def buscar_atenciones(afiliado: int, urgencias: list[int], turnos: list[int]) -> tuple[int, int]:
    """
    Cuenta cuántas veces fue atendido un afiliado por urgencia y cuántas por turno.

    pre: recibe el número de afiliado a buscar y ambas listas.
    post: devuelve una tupla (cant_urgencias, cant_turnos).
    """
    cant_urgencias = urgencias.count(afiliado)
    cant_turnos = turnos.count(afiliado)
    return cant_urgencias, cant_turnos


def realizar_busquedas(urgencias: list[int], turnos: list[int]) -> None:
    """
    Permite buscar afiliados repetidamente e informa sus atenciones hasta ingresar -1.

    pre: recibe las dos listas de atenciones.
    post: imprime el resumen de atenciones por afiliado.
    """
    print("--Búsqueda de Afiliados--")
    afiliado = int(input("Ingrese número de afiliado a buscar (-1 para terminar): "))

    while afiliado != -1:
        cant_u, cant_t = buscar_atenciones(afiliado, urgencias, turnos)
        print(f"Afiliado {afiliado}: Atendido {cant_u} vez/veces por urgencia y {cant_t} vez/veces por turno.")
        afiliado = int(input("\nIngrese número de afiliado a buscar (-1 para terminar): "))


def main() -> None:
    urgencias, turnos = cargar_pacientes()

    mostrar_listados(urgencias, turnos)

    realizar_busquedas(urgencias, turnos)


if __name__ == "__main__":
    main()