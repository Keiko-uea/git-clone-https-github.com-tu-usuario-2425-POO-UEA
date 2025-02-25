def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado.")

        elif opcion == "2":
            id_producto = int(input("ID del producto a eliminar: "))
            if inventario.eliminar_producto(id_producto):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            if inventario.actualizar_producto(id_producto, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("Producto no encontrado.")

        elif opcion == "5":
            productos = inventario.mostrar_inventario()
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("Inventario vacío.")

        elif opcion == "6":
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()