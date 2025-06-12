"""Crear una función recursiva que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto."""


def ejercicio4():
    def decimal_a_binario(n):
        if n == 0:
            return ""
        else:
            return decimal_a_binario(n // 2) + str(n % 2)

    numero = int(input("Ingrese un número entero positivo: "))
    binario = decimal_a_binario(numero)
    print(f"El número {numero} en binario es {binario or '0'}")


ejercicio4()
