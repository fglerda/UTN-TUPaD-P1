#!/bin/bash
read -p "Ingresar una palabra: " palabra

#calcular cantidad de caracteres
longitud=${#palabra} #sintaxis especial de bash que devuelve cantidad de caracteres/arrays

echo "La palabra "$palabra" tiene $longitud caracteres"
