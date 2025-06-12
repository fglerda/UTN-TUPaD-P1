#!/bin/bash
suma=0
cantidad=5

echo "Calculadora de promedio ($cantidad numeros)"

for ((i=1; i<=$cantidad; i++)); do
    while true; do
        read -p "Ingrese el numero $i: " num

        # Validación mejorada para números enteros y decimales
        if [[ "$num" =~ ^-?[0-9]*\.?[0-9]+$ ]]; then
            suma=$(awk "BEGIN {print $suma + $num}")
            break
        else
            echo "Error: Ingrese un numero valido (ej. 15 o -3.7)."
        fi
    done
done

[ "$cantidad" -eq 0 ] && cantidad=1  # Protección contra división por cero
promedio=$(awk "BEGIN {printf \"%.2f\", $suma / $cantidad}")

echo "-------------------------"
echo "Suma total: $suma"
echo "Cantidad de numeros: $cantidad"
echo "El promedio es: $promedio"