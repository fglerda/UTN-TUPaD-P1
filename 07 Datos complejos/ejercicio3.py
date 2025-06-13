"""Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios"""

precios_frutas = {
    "Banana": 1330,
    "Ananá": 2500,
    "Melón": 2800,
    "Uva": 1450,
    "Naranja": 1200,
    "Manzana": 1700,
    "Pera": 2300,
}
solo_frutas = list(precios_frutas.keys())
print(solo_frutas)
