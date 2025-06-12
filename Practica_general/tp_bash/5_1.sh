#!/bin/bash
read -p "Ingrese su nombre: " nombre
read -p "Ingrese su apellido " apellido

echo "Su nombre completo en mayuscula es: ${nombre^^} ${apellido^^}"
