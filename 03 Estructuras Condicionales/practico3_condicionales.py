# Lerda Fernando Gabriel

"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

edad = int(input("Indique su edad: "))
if edad >= 18:  # Incluye al 18
    print(f"usted tiene {edad}, es mayor de edad.")

"""2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado")

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar."""

numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""

edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Categoria Niño/a")
elif edad < 18:
    print("Categoria Adolescente")
elif edad < 30:
    print("Categoria Adulto/a Joven")
else:
    edad >= 30
    print("Categoria Adulto/a")

"""5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

contrasenia = input("Ingrese una contraseña entre 8 y 14 caracteres: ")
if 8 <= len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""6)Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
forma aleatoria.
"""

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print(f"Numeros aleatorios: {numeros_aleatorios}")
moda = mode(numeros_aleatorios)
print(f"mode = {moda}")
mediana = median(numeros_aleatorios)
print(f"median = {mediana}")
media = mean(numeros_aleatorios)
print(f"mean = {media}")

if media > mediana > moda:  # Sesgo positivo
    print("Sesgo positivo")
elif media < mediana < moda:  # Sesgo negativo
    print("Sesgo negativo")
elif media == mediana == moda:  # Sin sesgo
    print("Sin sesgo")
else:  # No se cumplen las condiciones para identificar el sesgo
    print("No se identifico sesgo ni ausencia del mismo.")

"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

vocales = {"a", "e", "i", "o", "u"}
palabra = (input("Ingrese una frase o palabra: ")).lower()
cantidad_caracteres = len(palabra)

if cantidad_caracteres > 0:
    ultimo_caracter = palabra[-1]  # Para obtener ultimo caracter.
    if ultimo_caracter in vocales:
        print(f"{palabra}!")
    else:
        print(palabra)
else:
    print("No se ingreso ningun caracter")

"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

nombre = input("Ingrese su nombre: ")
opcion = int(
    input(
        "Ingrese la opcion deseada:\n1. Si quiere su nombre en mayúsculas.\n2. Si quiere su nombre en minúsculas.\n3. Si quiere su nombre con la primera letra mayúscula.\n"
    )
)
if opcion == 1:
    nombre = nombre.upper()
    print(nombre)
elif opcion == 2:
    nombre = nombre.lower()
    print(nombre)
elif opcion == 3:
    nombre = nombre.title()
    print(nombre)
