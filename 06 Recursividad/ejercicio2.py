"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""


def ejercicio2():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    num = int(
        input("Ingrese la posición hasta la que desea ver la serie de Fibonacci: ")
    )
    for i in range(num):
        print(fibonacci(i), end=" ")
    print()


ejercicio2()
