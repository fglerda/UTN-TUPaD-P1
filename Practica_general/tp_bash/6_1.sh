#!/bin/bash

read -p "Ingrese una cadena de texto: " cadena

if [ "${#cadena}" -lt 8 ]; then
	echo "La cadena" $cadena "tiene menos de 8 caracteres."
else
	primeros_8="${cadena:0:8}"
	echo "Los primeros 8 caracteres son: " $primeros_8
fi

