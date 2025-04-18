import utils


# Definicion de funciones
def imprimir_matriz_de_simbolos(nro_columnas, nro_filas, simbolo="X"):
    for i in range(nro_filas):
        utils.imprimir_simbolo(simbolo, nro_columnas)


# Programa principal
ancho = utils.leer_entero_validado("Ingrese el ancho", 1)
alto = utils.leer_entero_validado("Ingrese el alto", 1)
imprimir_matriz_de_simbolos(ancho, alto, "-")
