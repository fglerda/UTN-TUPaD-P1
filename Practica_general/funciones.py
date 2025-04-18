# Definicion de funciones
def leer_entero_validado(mensaje, min=float("-Inf"), max=float("inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


def es_multiplo(num1, num2):
    return num1 % num2 == 0


# def obtener_resto(num1, num2):
#     return num1 - num2 * (num1 // num2)  # Sin usar operador %


# def es_multiplo(x, y):
#     return obtener_resto(x, y) == 0


def es_primo(numero):
    cont = 2
    mitad = numero // 2
    while cont <= mitad and not es_multiplo(numero, cont):
        cont += 1
    return cont > mitad  # Devuelve True si se cumple la igualdad


def informar_si_numero_es_primo(numero):
    if es_primo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")


# Programa principal
num = leer_entero_validado("Ingresar un numero natural: ", 1)
print(f"Seguimos adelante con el numero {num}")
informar_si_numero_es_primo(num)
