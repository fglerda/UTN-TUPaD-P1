#ejercicio: 1.1
#!/bin/bash
echo "Y si, es nuestro primer programa"

#ejercicio: 1.2
#!/bin/bash
echo "Lista larga de archivos y directorios en formato largo:"
ls -l

#ejercicio: 1.3
#!/bin/bash
mkdir -p backup
cp -v *.txt backup/
echo "Se han copiado todos los archivos .txt al directorio backup"

#ejercicio: 2.1
#!/bin/bash
num1=15
num2=3

suma=$((num1 + num2))
resta=$((num1 - num2))
multiplicacion=$((num1 * num2))
division=$((num1 / num2))

echo "Numeros utilizados para operar: $num1 y $num2"
echo "Suma: $num1 + $num2 = $suma"
echo "Resta: $num1 - $num2 = $resta"
echo "Multiplicacion: $num1 * $num2 = $multiplicacion"
echo "Division: $num1 / $num2 = $division"

#ejercicio: 2.2
#!/bin/bash
base=3
altura=7
area=$((base * altura))

echo "El area del triangulo de base = $base y altura = $altura es de: $area"

#ejercicio: 2.3
#!/bin/bash
nombre=Fernando
edad=37
ciudad=Cordoba

echo "Usted es $nombre, tiene $edad años y vive en $ciudad."

#ejercicio: 3.1
#!/bin/bash
echo "Por favor, ingrese su edad: "
read edad

if [ "$edad" -gt 17 ]; then
	echo "Usted es mayor de edad."
else
	echo "Usted es menor de edad."
fi

#ejercicio: 3.2
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

#ejercicio: 3.3
#!/bin/bash
read -p "Ingrese una nota del (1 - 10)." nota

#Validar el numero ingresado
if ! [[ "$nota" =~ ^[0-9]+$ ]] || [ "$nota" -gt 10 ] || [ "$nota" -lt 0 ]; then
	echo "Error: Debe ingresar un numero entre 0 y 10"
	exit 1
fi

#Evaluar la nota
if [ "$nota" -lt 6 ]; then
	echo "Reprobado"
elif [ "$nota" -ge 6 ] && [ "$nota" -le 8 ]; then
	echo "Aprobado"
elif [ "$nota" -ge 9 ]; then
	echo "Excelente"
fi

#ejercicio: 4.1
#!/bin/bash
for i in {1..10}; do
	echo "Numero $i"; done

#ejercicio: 4.2
#!/bin/bash
contador=1
suma=0

while [ $contador -le 100 ]; do
	suma=$((suma + contador))
	contador=$((contador + 1))
done

echo "La suma de los numeros del 1 al 100 es: $suma"

#ejercicio: 4.3
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

#ejercicio: 5.1
#!/bin/bash
read -p "Ingrese su nombre: " nombre
read -p "Ingrese su apellido " apellido

echo "Su nombre completo en mayuscula es: ${nombre^^} ${apellido^^}"

#ejercicio: 5.2
#!/bin/bash
read -p "Ingresar una palabra: " palabra

#calcular cantidad de caracteres
longitud=${#palabra} #sintaxis especial de bash que devuelve cantidad de caracteres/arrays

echo "La palabra "$palabra" tiene $longitud caracteres"

#ejercicio: 5.3
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

#ejercicio: 6.1
#!/bin/bash
read -p "Ingrese una cadena de texto: " cadena

if [ "${#cadena}" -lt 8 ]; then
	echo "La cadena" $cadena "tiene menos de 8 caracteres."
else
	primeros_8="${cadena:0:8}"
	echo "Los primeros 8 caracteres son: " $primeros_8
fi

#ejercicio: 6.2
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

#ejercicio: 6.3
#!/bin/bash
read -p "Ingrese un texto: " texto

echo "Texto en minusculas: ${texto,,}"

#ejercicio: 7.1
#!/bin/bash
read -p "Ingrese su nombre: " nombre
read -p "Ingrese su edad: " edad

if [ $edad -ge 16 ]; then
	echo "$nombre tiene edad suficiente para votar."
else
	echo "$nombre no tiene edad suficiente para votar."
fi

#ejercicio: 7.2
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

#ejercicio: 7.3
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
