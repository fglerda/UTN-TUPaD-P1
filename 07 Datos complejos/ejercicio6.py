"""Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno."""

alumnos = {}
for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(
        float(input(f"Ingrese nota {j+1} para {nombre}: ")) for j in range(3)
    )  # Se usa j como variable interna del bucle
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno} - Promedio: {promedio:.2f}")
