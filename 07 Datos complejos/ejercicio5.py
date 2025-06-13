"""Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1
print("Frecuencia de palabras:", conteo)
