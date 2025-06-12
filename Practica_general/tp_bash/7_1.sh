#!/bin/bash

read -p "Ingrese su nombre: " nombre
read -p "Ingrese su edad: " edad

if [ $edad -ge 16 ]; then
	echo "$nombre tiene edad suficiente para votar."
else
	echo "$nombre no tiene edad suficiente para votar."
fi
