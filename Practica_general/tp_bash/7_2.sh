#!/bin/bash

# Verificar si el archivo existe
if [ ! -f "nombres.txt" ]; then
	echo "Error: El archivo nombres.txt no existe."
    	exit 1
fi

# Verificar si el archivo está vacío
if [ ! -s "nombres.txt" ]; then
	echo "El archivo nombres.txt está vacío."
    	exit 0
fi

# Leer el archivo línea por línea
echo "=== Saludos personalizados ==="
while IFS= read -r nombre; do
	# Eliminar espacios en blanco al inicio/final
    	nombre_limpio=$(echo "$nombre" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

	# Ignorar líneas vacías
	if [ -n "$nombre_limpio" ]; then
        	echo "¡Hola $nombre_limpio! Espero que tengas un excelente día."
    	fi
done < "nombres.txt"
echo "=== Fin de la lista ==="