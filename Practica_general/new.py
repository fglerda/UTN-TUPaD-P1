lista = ["UTN", 2, 3.5, True]
lista_2 = ["kki367", "dme357", "pkl367"]
lista_anidada = [2, 4, "tomy", 1204, ["usuario", 74]]
print(lista)
print(lista[1])
lista.append("juancito")  # append es un metodo
lista.append(35)
print(lista)
lista.remove(2)  # es un metodo
print(lista)
lista[2] = "Nuevo dato"
print(lista)

rango_lista = lista[2:]
lista_final = lista + lista_2
print(rango_lista)
print(lista_final)
print("kki367" in lista_final)
print(lista_anidada)
print(
    lista_anidada[4][1]
)  # con el indice 4 me ubico en la sub lista y con el indice 1 en el elemento que deseo dentro de ella
