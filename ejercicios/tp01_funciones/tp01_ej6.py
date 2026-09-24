def contar_digitos(numero: int) -> int:
    c=0
    while numero > 0:
        numero= numero // 10
        c += 1
    return c

def concatenar(a: int ,b: int ) -> int:
    cantidad_dig= contar_digitos(b)
    potencia= 10 ** cantidad_dig
    resultado= a * potencia + b
    return resultado

assert concatenar(1234,567) == 1234567
assert concatenar(5,9) == 59
assert concatenar(12,5) == 125

print("Los asserts funcionan ;)")
