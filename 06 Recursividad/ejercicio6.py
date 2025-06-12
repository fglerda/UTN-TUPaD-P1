"""Escribí una función recursiva llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos, sin convertirlo en string."""


def ejercicio6():
    def suma_digitos(n):
        if n < 10:
            return n
        else:
            return n % 10 + suma_digitos(n // 10)

    numero = int(input("Ingrese un número entero positivo: "))
    resultado = suma_digitos(numero)
    print(f"La suma de los dígitos es: {resultado}")


ejercicio6()
