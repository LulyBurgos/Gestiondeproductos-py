import os

# Lista para almacenar los productos
productos = []

def cargar_datos():
    """Cargar los datos de productos desde un archivo."""
    if os.path.exists('productos.txt'):
        with open('productos.txt', 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(', ')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })

def guardar_datos():
    """Guardar los datos de productos en un archivo."""
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']}, {producto['precio']}, {producto['cantidad']}\n")

def añadir_producto():
    """Añadir un nuevo producto a la lista."""
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad del producto: "))
    
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    """Mostrar todos los productos en la lista."""
    if not productos:
        print("No hay productos en la lista.")
        return
    
    print("Lista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    """Actualizar los detalles de un producto existente."""
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            nuevo_nombre = input("Introduce el nuevo nombre (deja vacío para no cambiar): ")
            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            nuevo_precio = input("Introduce el nuevo precio (deja vacío para no cambiar): ")
            if nuevo_precio:
                producto['precio'] = float(nuevo_precio)
            nuevo_cantidad = input("Introduce la nueva cantidad (deja vacío para no cambiar): ")
            if nuevo_cantidad:
                producto['cantidad'] = int(nuevo_cantidad)
            print(f"Producto '{nombre}' actualizado exitosamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    """Eliminar un producto de la lista."""
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado exitosamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def menu():
    """Mostrar el menú y manejar las opciones del usuario."""
    cargar_datos()
    
    while True:
        print("\nMenu:")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Datos guardados. Saliendo...")
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Iniciar el programa
if __name__ == "__main__":
    menu()