n = int(input("Ingrese el valor de N: "))

cuadrados = [i**2 for i in range(1, n + 1)]

print(f"Lista de cuadrados: {cuadrados}")
print(f"Ultimos 10 valores: {cuadrados[-10:]}")