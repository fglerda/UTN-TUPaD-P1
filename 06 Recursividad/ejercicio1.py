"""Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario."""


def ejercicio1():
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i} es {factorial(i)}")


ejercicio1()
