"""Escribí una función recursiva contar_digito(numero, digito) que reciba un número entero positivo y un dígito, y devuelva cuántas veces aparece ese dígito dentro del número."""


def ejercicio8():
    def contar_digito(numero, digito):
        if numero == 0:
            return 0
        elif numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")


ejercicio8()
