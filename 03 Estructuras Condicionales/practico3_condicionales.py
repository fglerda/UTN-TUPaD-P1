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
