"""10.Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""


def calcular_promedio(a, b, c):
    sumar = a + b + c
    promedio = sumar / 3
    return promedio


a = float(input("Inrese valor n°1: "))
b = float(input("Inrese valor n°2: "))
c = float(input("Inrese valor n°3: "))

media = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {media}")
