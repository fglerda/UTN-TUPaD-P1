"""1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range(101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

# Version del codigo contando los digitos de una cadena de texto
numero = str(abs(int(input("Ingrese un numero entero: "))))
valor = len(numero)
print(f"el numero {numero} tiene {valor} digitos.")

# version del codigo dividiendo los numeros por 10 para obtener digitos ya que es base decimal.
numero = abs(int(input("Ingrese un numero entero: ")))  # abs para valor absolito.
if numero == 0:
    cantidad_dogitos = 1
else:
    cantidad_dogitos = 0
    while numero > 0:
        cantidad_dogitos += 1
        numero = numero // 10
print(f"El numero tiene {cantidad_dogitos} digitos.")

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

print("sumar valores entre numero 1 y numero 2.")
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

num_mayor = num1
if num2 > num1:
    num_mayor = num2

num_menor = num1
if num2 < num1:
    num_menor = num2

suma = 0
for i in range(num_menor + 1, num_mayor):
    suma += i

print(f"suma total {suma}")

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

print("Ingrese numero para sumar (ingrese 0 para salir): ")
numero = int(input("Ingrese un numero: "))
suma = 0

while numero != 0:
    suma += numero
    numero = int(input("ingrese otro numero: "))
print(f"suma acumulada: {suma}")

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

print("Adivina un numero del 0 al 9.")
import random

numero_aleatorio = random.randint(0, 9)
print(numero_aleatorio)  # esto es para prueba, luego se quita.
intento = 0

while True:
    numero_usuario = int(input("Ingrese un numero del 0 al 9: "))
    intento += 1
    if numero_usuario == numero_aleatorio:
        break
    print("¡Incorrecto! Vuelve a intentarlo.")

print(
    f"¡Correcto! Adivinaste en {intento} intentos. El numero era: {numero_aleatorio}."
)

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

for i in range(100, -1, -2):  # Incluyendo el 100 y el 0.
    print(i)
