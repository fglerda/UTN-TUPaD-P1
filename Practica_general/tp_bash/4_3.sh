#!/bin/bash
key="secreto"
intentos=0 #Se agrega un contador de intentos fallidos

until [ "$intento" == "$key" ]; do
	read -sp "Ingrese la contraseña: " intento #la s se utiliza para ocultar caracteres tipeados
	echo "" #salto de linea
	intentos=$((intentos + 1))

	if [ "$intento" != "$key" ]; then
		echo "Contraseña incorrecta. Intente nuevamente."
	fi
done

echo -e "\n¡Acceso concedido!"
echo "Intentos realizados: $intentos"
