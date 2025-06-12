#!/bin/bash
read -p "Ingrese una nota del (1 - 10)." nota

#Validar el numero ingresado
if ! [[ "$nota" =~ ^[0-9]+$ ]] || [ "$nota" -gt 10 ] || [ "$nota" -lt 0 ]; then
	echo "Error: Debe ingresar un numero entre 0 y 10"
	exit 1
fi

#Evaluar la nota
if [ "$nota" -lt 6 ]; then
	echo "Reprobado"
elif [ "$nota" -ge 6 ] && [ "$nota" -le 8 ]; then
	echo "Aprobado"
elif [ "$nota" -ge 9 ]; then
	echo "Excelente"
fi