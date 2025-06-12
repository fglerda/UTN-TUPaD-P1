"""Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es."""


def ejercicio5():
    def es_palindromo(palabra):
        if len(palabra) <= 1:
            return True
        if palabra[0] != palabra[-1]:
            return False
        return es_palindromo(palabra[1:-1])

    palabra = input("Ingrese una palabra sin espacios ni tildes: ").lower()
    print("Es palíndromo" if es_palindromo(palabra) else "No es palíndromo")


ejercicio5()
