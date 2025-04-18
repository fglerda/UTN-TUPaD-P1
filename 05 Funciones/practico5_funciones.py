# Lerda Fernando Gabriel

"""1. Crear una función llamada imprimir_hola_mundo que imprima por
pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
programa principal.
"""


# Definicion de funciones
def imprimir_hola_mundo():
    return print("Hola Mundo!")


# Programa principal
saludar = imprimir_hola_mundo()

"""2. Crear una función llamada saludar_usuario(nombre) que reciba
como parámetro un nombre y devuelva un saludo personalizado.
Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
principal solicitando el nombre al usuario.
"""


# Definicion de funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}"


# Programa principal
print(saludar_usuario(input("¿Cual es tu nombre? ")))

"""3. Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
"""


# Definicion de funciones
def informacion_personal(
    nombre="n", apellido="n", edad="Sin datos", residencia="Sin datos"
):
    # Con la funcion strip() se eliminan los espacios vacios al comienzo y final.
    # Con la condicion se controla que no sea una cadena vacio.
    nombre = nombre if nombre.strip() else "N"
    apellido = apellido if apellido.strip() else "N"
    edad = edad if edad.strip() else "S/D"
    residencia = residencia if residencia.strip() else "S/D"
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"


# Programa principal
identidad = informacion_personal(
    nombre=input("Indique su nombre: "),
    apellido=input("Indique su apellido: "),
    edad=input("Indique su edad: "),
    residencia=input("Lugar de residencia: "),
)
print(identidad)

"""4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

import math


def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


radio = float(input("Ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El area del circulo es: {area:.2f}")  # se limita el numero de decimales a 2
print(
    f"El perimetro del circulo es: {perimetro:.2f}"
)  # se limita el numero de decimales a 2

"""5. Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
"""


def segundos_a_horas(segundos):
    return segundos / 3600  # 1h = 3600 segundos


segundos = int(input("Ingrese cantidad de segundo: "))
print(
    f"{segundos} segundos son: {segundos_a_horas(segundos):.2f} horas."
)  # Se limita el decimal a 2 digitos

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un
número como parámetro y imprima la tabla de multiplicar de ese
número del 1 al 10. Pedir al usuario el número y llamar a la función.
"""

# Este codigo solo imprime lo resuelto en la funcion
# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         multiplicacion = numero * i
#         print(f"{numero} X {i} = {multiplicacion}")


# numero = int(input("Ingrese numero a multiplicar: "))
# tabla_multiplicar(numero)


# Este codigo retorna el valor de la funcion y es guardado en una variable "multiplica" y luego se imprime.
def tabla_multiplicar(numero):
    resultado = []  # Lista para almacenar resultados de la tabla.
    for i in range(1, 11):
        multiplicacion = numero * i
        resultado.append(
            f"{numero} X {i} = {multiplicacion}"
        )  # Agrega los elementos al final de la lista
    return "\n".join(resultado)  # Retorna las líneas unidas por saltos de línea


numero = int(input("Ingrese numero a multiplicar: "))
multiplica = tabla_multiplicar(numero)
print(multiplica)

"""7. Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
"""


def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multi = a * b
    if b != 0:
        div = a / b
    else:
        div = "No se puede dividir por 0"
    return (suma, resta, multi, div)  # Se devuelve una tupla con los resultados


a = int(input("Ingrese primer numero: "))
b = int(input("Ingrese primer numero: "))
resultado = operaciones_basicas(a, b)
print(f"El resultado de la suma es: {resultado[0]}")
print(f"El resultado de la resta es: {resultado[1]}")
print(f"El resultado de la multiplicacion es: {resultado[2]}")
print(f"El resultado de la divicion es: {resultado[3]}")

"""8. Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
"""


def calcular_imc(peso, altura):
    imc = peso / altura**2  # peso en kg y altura en metros
    return round(imc, 2)


peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es de {imc}")

"""9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""


def celsius_a_fahrenheit(grados_c):
    grados_f = 1.8 * grados_c + 32
    return grados_f


grados_c = float(input("Ingrese temperatura en °C. "))
grados_f = celsius_a_fahrenheit(grados_c)
print(f"{grados_c}°C son equivalentes a {grados_f}°F")

"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""


def calcular_promedio(a, b, c):
    """sdhfsadkdf"""
    sumar = a + b + c
    promedio = sumar / 3
    return promedio


a = float(input("Inrese valor n°1: "))
b = float(input("Inrese valor n°2: "))
c = float(input("Inrese valor n°3: "))

media = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {media}")
