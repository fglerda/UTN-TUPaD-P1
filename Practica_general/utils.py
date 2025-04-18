def leer_entero_validado(mensaje, min=float("-Inf"), max=float("inf")):
    n = int(input(f"{mensaje}: "))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}: "))
    return n


def es_multiplo(num1, num2):
    return num1 % num2 == 0


def sumatoria_divisores_propios(numero):
    sumatoria = 0
    for i in range(1, (numero // 2 + 1)):
        if es_multiplo(numero, i):
            sumatoria += i
    return sumatoria


def es_perfecto(numero):
    return sumatoria_divisores_propios(numero) == numero


def informar_si_numero_es_perfecto(numero):
    if es_perfecto(numero):
        print(f"El numero {numero} es perfecto")
    else:
        print(f"El numero {numero} no es perfecto")


def imprimir_simbolo(simbolo, veces):
    print(sucesion_simbolos(simbolo, veces))


def sucesion_simbolos(simbolo, veces):
    sucesion = ""
    for i in range(veces):
        sucesion += simbolo
    return sucesion


def informacion_personal(
    nombre="n", apellido="n", edad="Sin datos", residencia="Sin datos"
):
    nombre = nombre if nombre.strip() else "n"
    apellido = apellido if apellido.strip() else "n"
    edad = edad if edad.strip() else "Sin datos"
    residencia = residencia if residencia.strip() else "Sin datos"
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
