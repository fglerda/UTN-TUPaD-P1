def es_multiplo(num1, num2):
    return num1 % num2 == 0


num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))
if es_multiplo(num1, num2):  # No hace falta colocar "== True"
    print("Es primo")


######################################
def sumar_al_numero(numero):
    return numero + 1


# Llamada 1
numero = int(input("Ingrese un numero: "))
print(sumar_al_numero(numero))
# Llamada 2 otra manera
resultado = sumar_al_numero(15)
print(f"el resultado es: {resultado}")
