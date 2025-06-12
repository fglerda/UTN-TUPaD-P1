# Definicion de funciones
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f


def factorial_recur(x):
    if x == 0:
        return 1
    else:
        return x * factorial_recur(x - 1)


# Programa principal
print(factorial(5))
print(factorial_recur(5))
