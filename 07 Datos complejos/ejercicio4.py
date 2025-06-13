"""Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe."""

agenda = {}
for i in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    numero = input("Ingrese número telefónico: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre a consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")
