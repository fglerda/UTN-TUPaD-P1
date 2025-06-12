"""Fibonacci es la suma de los dos numeros antecedentes. 0,1,1,2,3,5,8,13"""


def fibonacci_recursivo(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)


if __name__ == "__main__":
    print(fibonacci_recursivo(7))
