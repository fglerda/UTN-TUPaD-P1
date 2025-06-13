"""Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos."""

agenda = {("lunes", "10:00"): "Reunión", ("martes", "14:00"): "Clase de programación"}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (HH:MM): ")

actividad = agenda.get((dia, hora), "No hay actividad programada.")
print("Actividad:", actividad)
