"""# para frase_recursiva.py
from frase_recursiva import repetir_frase as repetir

num = int(
    input("Ingrese el numero de veces que quiere imprimir la frase: ")
)
frase = input("Ingrese la frase que decea repetir: ")
repetir(num, frase)"""

"""# para suma_n_valores.py
from suma_n_valores import suma_recursiva as numero

num = int(
    input("Ingrese el numero de veces que quiere sumar el valor: ")
)
print(
    f"La suma de los primeros {num} numeros es: {numero(num)}"
) """

# Fibonacci
from fibonacci import fibonacci_recursivo

num_calcular = int(input("ingrese numero a calcular Fibonacci: "))

for i in range(num_calcular):
    print(
        f"el Fibonacci de {num_calcular} en la posicion {i} es: {fibonacci_recursivo(i)}"
    )
