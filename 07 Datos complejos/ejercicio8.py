"""Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

stock = {"Leche": 10, "Pan": 5, "Huevos": 30}

producto = input("Ingrese el producto a consultar: ")

if producto in stock:
    print(f"Stock actual: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades desea agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)
