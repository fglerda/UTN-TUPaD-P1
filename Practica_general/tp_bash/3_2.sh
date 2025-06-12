#!/bin/bash
read -p "Ingrese el nombre del archivo a verificar: " archivo
if [ -e "$archivo" ]; then
	if [ -f "$archivo" ]; then
		echo "El archivo regular existe."
	elif [ -d "$archivo" ]; then
		echo "Esto es un directorio, no un archivo regular."
	else
		echo "Existe pero no es un archivo regular ni un directorio."
	fi
else
	echo "El archivo/directorio no existe."
fi
