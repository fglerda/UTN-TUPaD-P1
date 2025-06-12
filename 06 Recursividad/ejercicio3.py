"""Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula n^m = n * n^(m-1)."""


def ejercicio3():
    def potencia(base, exponente):
        if exponente == 0:
            return 1
        else:
            return base * potencia(base, exponente - 1)

    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")


ejercicio3()
