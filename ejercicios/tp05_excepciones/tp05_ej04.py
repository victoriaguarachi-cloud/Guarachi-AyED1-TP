def contar_con_interrupcion() -> None:
    """
    PRE: No recibe parámetros.
    POST: Imprime números enteros entre 1 y 100000. Si el usuario presiona Ctrl-C,
          captura KeyboardInterrupt y solicita confirmación antes de salir.
    """
    i = 1
    limite = 100000

    while i <= limite:
        try:
            print(f"Número: {i}")
            i += 1
        except KeyboardInterrupt:
            # Capturamos la interrupción de teclado Ctrl-C
            print("\n\n[!] Se detectó la pulsación de Ctrl-C.")
            
            try:
                respuesta = input("¿Está seguro de que desea detener la ejecución? (s/n): ").strip().lower()
                if respuesta == "s":
                    print("Ejecución cancelada por el usuario.")
                    break
                else:
                    print("Continuando con la impresión...\n")
            except KeyboardInterrupt:
                # Si vuelve a presionar Ctrl-C durante el prompt, salimos limpiamente
                print("\nInterrupción forzada. Saliendo...")
                break


def main() -> None:
    cant = 80
    print("=" * cant)
    print("CONTROL DE INTERRUPCIÓN CON CTRL-C (TP5 EJ 4)".center(cant))
    print("=" * cant)
    
    print("\nIniciando conteo del 1 al 100000. Presioná Ctrl-C para pausar/interrumpir.\n")
    contar_con_interrupcion()

    print("\n" + "=" * cant)


if __name__ == "__main__":
    main()