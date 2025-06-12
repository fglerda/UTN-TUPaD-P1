#!/bin/bash

while true; do
	echo -n "Ingrese su contraseña: "
	read -s password
	echo
	if [ -z "$password" ]; then
		echo "Error, la contraseña no puede estar vacia. Intente nuevamente."
	else
		echo "Contraseña ingresada correctamente."
		break
	fi
done
