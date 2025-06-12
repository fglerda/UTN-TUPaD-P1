#!/bin/bash

echo "Por favor, ingrese su edad: "
read edad

if [ "$edad" -gt 17 ]; then
	echo "Usted es mayor de edad."
else
	echo "Usted es menor de edad."
fi
