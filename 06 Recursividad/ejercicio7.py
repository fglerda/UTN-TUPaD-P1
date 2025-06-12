"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos, hasta llegar al último con un bloque. Escribí una función recursiva que calcule el total de bloques necesarios."""


def ejercicio7():
    def contar_bloques(n):
        if n == 1:
            return 1
        else:
            return n + contar_bloques(n - 1)

    nivel = int(input("Ingrese el número de bloques en el nivel más bajo: "))
    print(f"Total de bloques necesarios: {contar_bloques(nivel)}")


ejercicio7()
