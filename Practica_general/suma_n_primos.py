# Definir si un numero es primo
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


# Recursividad
def sum_n_primos(num):
    if num == 1:
        return 0
    elif es_primo(num):
        return num + sum_n_primos(num - 1)
    else:
        return sum_n_primos(num - 1)


print(sum_n_primos(5))
