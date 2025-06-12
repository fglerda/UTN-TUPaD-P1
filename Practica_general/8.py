contador = 1
suma = 0
bandera = True

num1 = 3

while bandera:
    num2 = 5
    suma = suma + num2
    contador = contador + 1

    while contador <= num1:
        print(suma, end=",")
        bandera = False

        if contador == num1:
            bandera = True
        break
