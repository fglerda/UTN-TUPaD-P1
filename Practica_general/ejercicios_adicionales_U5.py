# Tabla de multiplicar
def tabla_multiplicar(numero):
    lista = []
    for i in range(1, 11):
        lista.append(numero * i)
    return lista


numero = int(input("Ingrese numero de tabla: "))
print(tabla_multiplicar(numero))


# Ejercicio 2: Suma de números pares
def suma_pares():
    par = 0
    for i in lista:
        if i % 2 == 0:
            par += i
    return par


lista = [2, 5, 7, 4, 3, 9, 6, 3]
print(suma_pares())

# Ejercicio 3: Área y perímetro de un rectángulo


def rectangulo(longitud, anchura):
    area = longitud * anchura
    perimetro = 2 * (longitud + anchura)
    return f" El area del rectangulo es: {area} y su perimetro es: {perimetro}"


longitud = int(input("Ingrese la longitud: "))
anchura = int(input("Ingrese la anchura: "))
resultado_rectangulo = rectangulo(longitud, anchura)
print(resultado_rectangulo)


# Ejercicio 4: Conversión de temperatura
def convertir_temperatura(g_c, op):
    g_f = (g_c * 1.8) + 32
    g_k = g_c + 273.15
    if op == "F":
        return g_f
    else:
        return g_k


g_c = float(input("Ingrese temperatura en °C: "))
op = input("Indique si desea convertir a F o a K?. ")
print(convertir_temperatura(g_c, op))


# Ejercicio 5: Verificador de números primos
def es_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            contador += 1
    if contador == 2:
        return "Es primo"
    else:
        return "No es primo"


numero = int(input("Ingrese un numero entero: "))
print(es_primo(numero))
