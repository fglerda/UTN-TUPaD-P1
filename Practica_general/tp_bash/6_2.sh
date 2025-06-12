#!/bin/bash

#definiendo variable de ejemplo
texto="Hubo un error en el sistema. El error fue critico. Por favor, revisar el error."

#reemplazar error por problemita
texto_modificado="${texto//error/problemita}" #la doble // reemplaza todas las palabras error, no solo la primera.

#Mostramos el resultado
echo "texto original"
echo "$texto"
echo
echo "texto modificado"
echo "$texto_modificado"
